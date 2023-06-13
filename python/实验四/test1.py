import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
x = np.arange(-np.pi, np.pi, 0.1)
plt.plot(x, np.sin(x), color='blue', linewidth=4.0, linestyle='-')
plt.plot(x, np.cos(x), color='red', linewidth=5.0, linestyle='-.')
plt.xlabel("x")  # 横轴标识
plt.ylabel("y")  # 纵轴标识
plt.grid(True)

plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), color='blue', linewidth=4.0, linestyle='-', label='sin')
plt.legend(loc="upper left")
plt.grid(True)
plt.xlabel("x")  # 横轴标识
plt.ylabel("y")  # 纵轴标识

plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), color='red', linewidth=5.0, linestyle='-.', label='cos')
plt.legend(loc="upper left")
plt.grid(True)
plt.xlabel("x")  # 横轴标识
plt.ylabel("y")  # 纵轴标识
plt.show()
