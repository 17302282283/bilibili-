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


def get_model(deg, data, y):
    return np.polyfit(data, y, deg)


x0 = get_model(3, data[:, 0], all_y_trues)
x1 = get_model(3, data[:, 1], all_y_trues)

y0 = np.poly1d(x0)
y1 = np.poly1d(x1)

# for i in range(4):
#     print(all_y_trues[i], y0(data[i, 0]), y1(data[i, 1]))

# for i in range(4):
#     print(all_y_trues[i], np.polyval(
#         x0, data[i, 0]), np.polyval(x1, data[i, 1]))

data_test = [-7, -3]
data_true = 1
print(data_true, np.polyval(x0, data_test[0]), np.polyval(x1, data_test[1]))
print(y0)
print(y1)
print(data_true, y0(data_test[0]), y1(data_test[1]))
''' 
'''
