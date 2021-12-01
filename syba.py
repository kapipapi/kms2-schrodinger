import pandas as pd
import numpy as np


def read_input(filename: str):
    file = open(filename, "r")
    N = int(file.readline().split("#")[0])
    n = int(file.readline().split("#")[0])
    dtau = float(file.readline().split("#")[0])
    K = int(file.readline().split("#")[0])
    omega = int(file.readline().split("#")[0])
    N_sim = int(file.readline().split("#")[0])
    S_out = int(file.readline().split("#")[0])
    S_dat = int(file.readline().split("#")[0])

    return [N, n, dtau, K, omega, N_sim, S_out, S_dat]


N, n, dtau, K, omega, N_sim, S_out, S_dat = read_input("../../Downloads/KMS_zadanie2/input.txt")

# N, n, dtau, K, Omega, N_sim, S_out, S_dat
x_phi_table = np.zeros((N + 1, 3), dtype=float)
hamiltonian_table = np.zeros((N + 1, 2), dtype=float)

# init
for k in range(N + 1):
    x_phi_table[k][0] = k / N
    x_phi_table[k][1] = np.sqrt(2) * np.sin(n * np.pi * x_phi_table[k][0])

for k in range(N + 1):
    if k == 0 or k == N:
        hamiltonian_table[k] = 0
    else:
        hamiltonian_table[k][0] = (x_phi_table[k - 1][1] + x_phi_table[k + 1][1] - 2 * x_phi_table[k][1]) / (
                2 / (N) ** 2) + K * (x_phi_table[k][0] - 1 / 2) * x_phi_table[k][1] * np.sin(
            omega * dtau)
        hamiltonian_table[k][1] = (x_phi_table[k - 1][2] + x_phi_table[k + 1][2] - 2 * x_phi_table[k][2]) / (
                2 / (N) ** 2) + K * (x_phi_table[k][0] - 1 / 2) * x_phi_table[k][2] * np.sin(
            omega * dtau)

print(x_phi_table)
print(hamiltonian_table)
