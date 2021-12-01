import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

data = np.zeros((100, 101), dtype=float)

file = open("phi.xyz", "r")
i = 0
for line in file:
    data[i] = line.strip("\n").split('\t')
    i += 1

fig, ax = plt.subplots()


def update(i):
    xs = [k*0.01 for k in range(101)]
    ys = data[i]
    print(data[i])
    ax.clear()
    ax.scatter(xs, ys)


a = anim.FuncAnimation(fig, update, frames=100, interval=20)
# a.save(f'rho.mp4', fps=20, dpi=600)
plt.show()
