import numpy as np
import matplotlib.pyplot as plt
data = np.array([
    [-2, -1],
    [25, 6],
    [17, 4],
    [-15, -6]
])
all_y_trues = np.array([
    1,
    0,
    0,
    1
])

# x = np.linspace(-40, 40, 160)
# y = np.linspace(-10, 10, 40)

plt.scatter(data[:, 0], data[:, 1], c=all_y_trues)
plt.show()
