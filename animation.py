import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

data = np.zeros((500, 101), dtype=float)

prefix = "simulation/sim" + sys.argv[1] + "/"
print(prefix)

file = open(prefix + "phi.xyz", "r")
i = 0
for line in file:
    data[i] = line.strip("\n").split('\t')
    i += 1

fig, ax = plt.subplots()


def update(i):
    xs = [k * 0.01 for k in range(101)]
    ys = data[i]
    print(i)
    ax.clear()
    ax.set_xlabel("x")
    ax.set_ylabel("psi")
    ax.scatter(xs, ys)


a = anim.FuncAnimation(fig, update, frames=500, interval=20)
# a.save(f'rho.mp4', fps=60, dpi=600)
plt.show()
