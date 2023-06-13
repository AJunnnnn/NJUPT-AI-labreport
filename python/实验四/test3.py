import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
z = np.linspace(0, 30, 100)
x = np.sin(z)
y = np.cos(z)
ax.plot(x, y, z, color="red")
# plt.show()

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(1, 1, 1, projection='3d')
x = np.arange(-3, 3, 0.1)
y = np.arange(-3, 3, 0.1)
z = 1 / ((np.sqrt((1 - x) ** 2 + y ** 2)) + (np.sqrt((1 + x) ** 2 + y ** 2)))
ax2.plot(x, y, z)
# plt.show()

fig3 = plt.figure(3)
ax3 = fig3.add_subplot(1, 1, 1, projection='3d')
X, Y = np.meshgrid(x, y)
Z = 1 / ((np.sqrt((1 - X) ** 2 + Y ** 2)) + (np.sqrt((1 + X) ** 2 + Y ** 2)))
ax3.plot_surface(X, Y, Z, cmap=cm.jet)
# plt.show()

# X，Y，Z准备完毕
plt.figure(4)
CS = plt.contour(X, Y, Z, 6)  # 制作等高线，横砍10刀
plt.clabel(CS, inline=1, fontsize=10)  # inline控制画标签，移除标签下的线
plt.title('Simplest default with labels')
plt.show()
