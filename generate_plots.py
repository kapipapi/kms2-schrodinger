import sys
import numpy as np
import matplotlib.pyplot as plt

prefix = "simulation/sim" + sys.argv[1] + "/"
print(prefix)

data = np.genfromtxt(prefix + 'additional.dat', delimiter='\t', skip_header=1, dtype=[('tau', 'f8'),
                                                                                      ('N_greek', 'f8'),
                                                                                      ('x', 'f8'),
                                                                                      ('epsilon', 'f8')])
plt.plot(data['tau'], data['epsilon'], 'o', color='b')
plt.grid()
plt.xlabel('tau')
plt.ylabel('Energy')
plt.ylim([0, max(data['epsilon']) + 1])
plt.savefig(prefix + 'epsilon.png')

plt.figure().clear()
plt.close()
plt.cla()
plt.clf()

plt.plot(data['tau'], data['x'], 'o', color='b')
plt.grid()
plt.xlabel('tau')
plt.ylabel('Average x')
plt.ylim([0, 1])
plt.savefig(prefix + 'avgx.png')

plt.figure().clear()
plt.close()
plt.cla()
plt.clf()

plt.plot(data['tau'], data['N_greek'], 'o', color='b')
plt.grid()
plt.xlabel('tau')
plt.ylabel('Norm')
plt.ylim([0.9, 1.1])
plt.savefig(prefix + 'norm.png')
plt.close()
