# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hKBVHzswaiVlGo-5RVqw_Wm-8AXPtpfK
"""

################################################################################
###### This neural network designed and developed by Majdi M. S.  Awad #########
################################################################################
import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork:
    def __init__(self):
        self.inputs_number = 3
        self.inputs_names = ['Dnu', 'numax', 'epsilon']

    def calculate_outputs(self, inputs):
        scaled_Dnu = (inputs[0] - 5.878520012) / 3.069350004
        scaled_numa_x = (inputs[1] - 60.00109863) / 44.48839951
        scaled_epsilon = (inputs[2] - 0.5984969735) / 0.343885988

        perceptron_layer_1_output_0 = np.tanh(-1.08472 + (scaled_Dnu * 8.83468) + (scaled_numa_x * -1.54039) + (scaled_epsilon * -3.6386))
        perceptron_layer_1_output_1 = np.tanh(0.761358 + (scaled_Dnu * 5.24602) + (scaled_numa_x * -4.54935) + (scaled_epsilon * 0.143989))
        perceptron_layer_1_output_2 = np.tanh(-0.98733 + (scaled_Dnu * 2.20786) + (scaled_numa_x * 1.89229) + (scaled_epsilon * -0.229483))
        perceptron_layer_1_output_3 = np.tanh(0.850799 + (scaled_Dnu * -7.41337) + (scaled_numa_x * 1.75661) + (scaled_epsilon * 2.89557))
        perceptron_layer_1_output_4 = np.tanh(-2.25198 + (scaled_Dnu * -2.47969) + (scaled_numa_x * 2.12309) + (scaled_epsilon * -1.58168))
        perceptron_layer_1_output_5 = np.tanh(2.09279 + (scaled_Dnu * -3.42202) + (scaled_numa_x * 1.11115) + (scaled_epsilon * -3.78158))

        probabilistic_layer_combinations_0 = 6.35881 - 6.07271 * perceptron_layer_1_output_0 - 4.87637 * perceptron_layer_1_output_1 + 1.9414 * perceptron_layer_1_output_2 + 4.08944 * perceptron_layer_1_output_3 + 4.46508 * perceptron_layer_1_output_4 + 4.4078 * perceptron_layer_1_output_5

        POP = 1.0 / (1.0 + np.exp(-probabilistic_layer_combinations_0))

        out = [POP]

        return out

    def calculate_batch_output(self, input_batch):
        output_batch = [None] * input_batch.shape[0]

        for i in range(input_batch.shape[0]):
            inputs = list(input_batch[i])
            output = self.calculate_outputs(inputs)
            output_batch[i] = output

        return output_batch

nn = NeuralNetwork()

user_inputs = []
for i in range(nn.inputs_number):
    value = float(input(f"Enter value for {nn.inputs_names[i]}: "))
    user_inputs.append(value)

result = nn.calculate_outputs(user_inputs)
rounded_result = round(result[0])

if rounded_result == 0:
    print("The result is 0, so the star is RGB (Red Giant Branch)")
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('RGB (Red Giant Branch) Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
elif rounded_result == 1:
    print("The result is 1, so the star is HeB (Helium Burning)")
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y)
    plt.title('HeB (Helium Burning) Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
else:
    print("The result is neither 0 nor 1, unable to determine star type.")
################################################################################
###### This neural network designed and developed by Majdi M. S.  Awad #########
################################################################################