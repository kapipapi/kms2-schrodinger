import numpy as np


def read_input(filename: str):
    file = open(filename, "r")
    N = int(file.readline().split("#")[0])
    n = int(file.readline().split("#")[0])
    tau = float(file.readline().split("#")[0])
    k = int(file.readline().split("#")[0])
    omega = int(file.readline().split("#")[0])
    N_sim = int(file.readline().split("#")[0])
    S_out = int(file.readline().split("#")[0])
    S_dat = int(file.readline().split("#")[0])

    return [N, n, tau, k, omega, N_sim, S_out, S_dat]


N, n, tau, k, omega, N_sim, S_out, S_dat = read_input("input.txt")

phi = np.zeros((N + 1, 3), dtype=float)
H = np.zeros((N + 1, 2), dtype=float)
