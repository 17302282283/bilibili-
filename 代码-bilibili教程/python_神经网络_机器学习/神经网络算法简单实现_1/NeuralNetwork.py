import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derive_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)


def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()


class OurNeuralNetwork():
    def __init__(self):
        self.w_hide1_1 = np.random.normal()  # w1
        self.w_hide1_2 = np.random.normal()  # w2

        self.w_hide2_1 = np.random.normal()  # w3
        self.w_hide2_2 = np.random.normal()  # w4

        self.w_out_1 = np.random.normal()  # w5
        self.w_out_2 = np.random.normal()  # w6

        self.b_hide1 = np.random.normal()  # b1
        self.b_hide2 = np.random.normal()  # b2

        self.b_out = np.random.normal()  # b3

    def feedforward(self, x):
        hide_1 = sigmoid(self.w_hide1_1 *
                         x[0] + self.w_hide1_2 * x[1] + self.b_hide1)
        hide_2 = sigmoid(self.w_hide2_1 *
                         x[0] + self.w_hide2_2 * x[1] + self.b_hide2)

        out_1 = sigmoid(self.w_out_1 * hide_1 +
                        self.w_out_2 * hide_2 + self.b_out)

        return out_1

    def f(self, x1, x2, w1, w2, b):
        return (x1 * w1 + x2 * w2 + b)

    def train(self, data, all_y_trues):
        learn_rate = 0.1
        epochs = 1000

        for epoch in range(epochs):
            # print("epoch:", epoch)
            for x, y_true in zip(data, all_y_trues):

                sum_h1 = self.f(x[0], x[1], self.w_hide1_1,
                                self.w_hide1_2, self.b_hide1)
                h1 = sigmoid(sum_h1)

                sum_h2 = self.f(x[0], x[1], self.w_hide2_1,
                                self.w_hide2_2, self.b_hide2)
                h2 = sigmoid(sum_h2)

                sum_o1 = self.f(h1, h2, self.w_out_1, self.w_out_2, self.b_out)
                o1 = sigmoid(sum_o1)
                y_pred = o1

                d_L_d_ypred = -2 * (y_true - y_pred)

                d_ypred_d_w5 = h1 * derive_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * derive_sigmoid(sum_o1)
                d_ypred_d_b3 = derive_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w_out_1 * derive_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w_out_2 * derive_sigmoid(sum_o1)

                d_h1_d_w1 = x[0] * derive_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * derive_sigmoid(sum_h1)
                d_h1_d_b1 = derive_sigmoid(sum_h1)

                d_h2_d_w3 = x[0] * derive_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * derive_sigmoid(sum_h2)
                d_h2_d_b2 = derive_sigmoid(sum_h2)

                # update weights and biases
                # Neuron out
                self.w_out_1 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w_out_2 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b_out -= learn_rate * d_L_d_ypred * d_ypred_d_b3

                # Neuron hide1
                self.w_hide1_1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w_hide1_2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b_hide1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                # Neuron hide2
                self.w_hide2_1 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w_hide2_2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b_hide2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

            if(epoch % 10 == 0):
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = mse_loss(all_y_trues, y_preds)
                print("y_preds:", y_preds)
                print("epoch:", epoch, "loss:", loss)


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

data_test = [-7, -3]
data_true = 1
print("start:")
network = OurNeuralNetwork()
network.train(data, all_y_trues)
print("true:", all_y_trues[0], "y_pred:", network.feedforward(x=data[0]))
print("true:", all_y_trues[1], "y_pred:", network.feedforward(x=data[1]))
print("true:", all_y_trues[2], "y_pred:", network.feedforward(x=data[2]))
print("true:", all_y_trues[3], "y_pred:", network.feedforward(x=data[3]))
print('this is test ', data_true, 'y_pred:', network.feedforward(x=data_test))
print("end")
