import numpy as np
import sys

prefix = "simulation/sim"+sys.argv[1]+"/"

print(prefix)

def read_input(filename: str):
    file = open(filename, "r")
    N = int(file.readline().split("#")[0])
    n = int(file.readline().split("#")[0])
    dtau = float(file.readline().split("#")[0])
    K = int(file.readline().split("#")[0])
    omega = float(file.readline().split("#")[0])
    N_sim = int(file.readline().split("#")[0])
    S_out = int(file.readline().split("#")[0])
    S_dat = int(file.readline().split("#")[0])

    return [N, n, dtau, K, omega, N_sim, S_out, S_dat]


N, n, dtau, K, omega, N_sim, S_out, S_dat = read_input(prefix + "input.txt")

dat_file = open(prefix + "additional.dat", "w")
dat_file.write(f"tau\tN_greek\tx\tepsilon\n")
out_file = open(prefix + "phi.xyz", "w")

x_k = np.zeros((N + 1, 1), dtype=float)
phi_R = np.zeros((N + 1, 1), dtype=float)
phi_I = np.zeros((N + 1, 1), dtype=float)

delta_x = 1 / N


# chwila początkowa - stan stacjonarny (29)
def init():
    for k in range(N + 1):
        # set x_k
        x_k[k] = k / N

        # phi_R
        phi_R[k] = np.sqrt(2) * np.sin(n * np.pi * x_k[k])

        # phi_I
        phi_I[k] = 0


# calculate hamiltionian
def hamiltonian(phi):
    global tau, omega, delta_x

    H = np.zeros((N + 1, 1), dtype=float)

    for k in range(N + 1):
        if k == 0 or k == N:
            continue
        else:
            # eq (30)
            H[k] = float(- 0.5 * ((phi[k + 1] + phi[k - 1] - 2 * phi[k]) / (delta_x ** 2)) + K * (
                    x_k[k] - 0.5) * phi[k] * np.sin(omega * tau))
    return H


# simulation step
def step():
    global phi_R, phi_I

    HI = hamiltonian(phi_I)
    phi_R += HI * dtau / 2

    HR = hamiltonian(phi_R)
    phi_I -= HR * dtau

    HI2 = hamiltonian(phi_I)
    phi_R += HI2 * dtau / 2


# calculate additional data
def additional_data():
    global phi_R, phi_I, delta_x
    rho = phi_R ** 2 + phi_I ** 2

    # norma
    N_greek = delta_x * sum(rho)

    # sr polozenie
    x = delta_x * sum(x_k * rho)

    # energia
    epsilon = delta_x * sum(phi_R * hamiltonian(phi_R) + phi_I * hamiltonian(phi_I))

    return float(N_greek), float(x), float(epsilon)


init()

tau = 0

for i in range(N_sim):
    step()
    tau += dtau

    print(f"{i/N_sim*100}%")

    if i % S_dat == 0:
        N_greek, x, epsilon = additional_data()
        dat_file.write(f"{tau}\t{N_greek}\t{x}\t{epsilon}\n")

    if i % S_out == 0:
        for k in range(0, N + 1):
            out_file.write(f"{float(phi_R[k] ** 2 + phi_I[k] ** 2)}")
            if k != N:
                out_file.write("\t")
        out_file.write("\n")

dat_file.close()
out_file.close()
