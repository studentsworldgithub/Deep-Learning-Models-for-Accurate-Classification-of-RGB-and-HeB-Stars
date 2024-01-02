#include <iostream>
#include <cmath>
#include <vector>

class NeuralNetwork {
private:
    int inputs_number = 3;
    std::vector<std::string> inputs_names = {"Dnu", "numax", "epsilon"};

public:
    int getInputsNumber() const {
        return inputs_number;
    }

    std::string getInputName(int index) const {
        return inputs_names[index];
    }

    std::vector<double> calculate_outputs(const std::vector<double>& inputs) {
        double scaled_Dnu = (inputs[0] - 5.878520012) / 3.069350004;
        double scaled_numa_x = (inputs[1] - 60.00109863) / 44.48839951;
        double scaled_epsilon = (inputs[2] - 0.5984969735) / 0.343885988;

        double perceptron_layer_1_output_0 = tanh(-1.08472 + (scaled_Dnu * 8.83468) + (scaled_numa_x * -1.54039) + (scaled_epsilon * -3.6386));
        double perceptron_layer_1_output_1 = tanh(0.761358 + (scaled_Dnu * 5.24602) + (scaled_numa_x * -4.54935) + (scaled_epsilon * 0.143989));
        double perceptron_layer_1_output_2 = tanh(-0.98733 + (scaled_Dnu * 2.20786) + (scaled_numa_x * 1.89229) + (scaled_epsilon * -0.229483));
        double perceptron_layer_1_output_3 = tanh(0.850799 + (scaled_Dnu * -7.41337) + (scaled_numa_x * 1.75661) + (scaled_epsilon * 2.89557));
        double perceptron_layer_1_output_4 = tanh(-2.25198 + (scaled_Dnu * -2.47969) + (scaled_numa_x * 2.12309) + (scaled_epsilon * -1.58168));
        double perceptron_layer_1_output_5 = tanh(2.09279 + (scaled_Dnu * -3.42202) + (scaled_numa_x * 1.11115) + (scaled_epsilon * -3.78158));

        double probabilistic_layer_combinations_0 = 6.35881 - 6.07271 * perceptron_layer_1_output_0 - 4.87637 * perceptron_layer_1_output_1 + 1.9414 * perceptron_layer_1_output_2 + 4.08944 * perceptron_layer_1_output_3 + 4.46508 * perceptron_layer_1_output_4 + 4.4078 * perceptron_layer_1_output_5;

        double POP = 1.0 / (1.0 + exp(-probabilistic_layer_combinations_0));

        std::vector<double> out = {POP};
        return out;
    }

    std::vector<std::vector<double>> calculate_batch_output(const std::vector<std::vector<double>>& input_batch) {
        std::vector<std::vector<double>> output_batch(input_batch.size(), std::vector<double>(1));

        for (size_t i = 0; i < input_batch.size(); ++i) {
            std::vector<double> inputs = input_batch[i];
            std::vector<double> output = calculate_outputs(inputs);
            output_batch[i] = output;
        }

        return output_batch;
    }
};

int main() {
    NeuralNetwork nn;

    std::vector<double> user_inputs;
    for (int i = 0; i < nn.getInputsNumber(); ++i) {
        double value;
        std::cout << "Enter value for " << nn.getInputName(i) << ": ";
        std::cin >> value;
        user_inputs.push_back(value);
    }

    std::vector<double> result = nn.calculate_outputs(user_inputs);
    int rounded_result = round(result[0]);

    if (rounded_result == 0) {
        std::cout << "The result is 0, so the star is RGB (Red Giant Branch)" << std::endl;
    } else if (rounded_result == 1) {
        std::cout << "The result is 1, so the star is HeB (Helium Burning)" << std::endl;
    } else {
        std::cout << "The result is neither 0 nor 1, unable to determine star type." << std::endl;
    }

    return 0;
}
