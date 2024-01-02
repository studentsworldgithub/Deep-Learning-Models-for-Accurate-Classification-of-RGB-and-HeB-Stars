import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class NeuralNetwork {
    private int inputsNumber = 3;
    private List<String> inputsNames = List.of("Dnu", "numax", "epsilon");

    public List<String> getInputsNames() {
        return inputsNames;
    }

    public List<Double> calculateOutputs(List<Double> inputs) {
        double scaledDnu = (inputs.get(0) - 5.878520012) / 3.069350004;
        double scaledNumax = (inputs.get(1) - 60.00109863) / 44.48839951;
        double scaledEpsilon = (inputs.get(2) - 0.5984969735) / 0.343885988;

        double perceptronLayer1Output0 = Math.tanh(-1.08472 + (scaledDnu * 8.83468) + (scaledNumax * -1.54039) + (scaledEpsilon * -3.6386));
        double perceptronLayer1Output1 = Math.tanh(0.761358 + (scaledDnu * 5.24602) + (scaledNumax * -4.54935) + (scaledEpsilon * 0.143989));
        double perceptronLayer1Output2 = Math.tanh(-0.98733 + (scaledDnu * 2.20786) + (scaledNumax * 1.89229) + (scaledEpsilon * -0.229483));
        double perceptronLayer1Output3 = Math.tanh(0.850799 + (scaledDnu * -7.41337) + (scaledNumax * 1.75661) + (scaledEpsilon * 2.89557));
        double perceptronLayer1Output4 = Math.tanh(-2.25198 + (scaledDnu * -2.47969) + (scaledNumax * 2.12309) + (scaledEpsilon * -1.58168));
        double perceptronLayer1Output5 = Math.tanh(2.09279 + (scaledDnu * -3.42202) + (scaledNumax * 1.11115) + (scaledEpsilon * -3.78158));

        double probabilisticLayerCombinations0 = 6.35881 - 6.07271 * perceptronLayer1Output0 - 4.87637 * perceptronLayer1Output1 + 1.9414 * perceptronLayer1Output2 + 4.08944 * perceptronLayer1Output3 + 4.46508 * perceptronLayer1Output4 + 4.4078 * perceptronLayer1Output5;

        double pop = 1.0 / (1.0 + Math.exp(-probabilisticLayerCombinations0));

        List<Double> out = new ArrayList<>();
        out.add(pop);
        return out;
    }

    public List<List<Double>> calculateBatchOutput(List<List<Double>> inputBatch) {
        List<List<Double>> outputBatch = new ArrayList<>();

        for (List<Double> inputs : inputBatch) {
            List<Double> output = calculateOutputs(inputs);
            outputBatch.add(output);
        }

        return outputBatch;
    }

    public static void main(String[] args) {
        NeuralNetwork nn = new NeuralNetwork();
        Scanner scanner = new Scanner(System.in);

        List<Double> userInputs = new ArrayList<>();
        for (String inputName : nn.getInputsNames()) {
            System.out.print("Enter value for " + inputName + ": ");
            double value = scanner.nextDouble();
            userInputs.add(value);
        }

        List<Double> result = nn.calculateOutputs(userInputs);
        int roundedResult = (int) Math.round(result.get(0));

        if (roundedResult == 0) {
            System.out.println("The result is 0, so the star is RGB (Red Giant Branch)");
        } else if (roundedResult == 1) {
            System.out.println("The result is 1, so the star is HeB (Helium Burning)");
        } else {
            System.out.println("The result is neither 0 nor 1, unable to determine star type.");
        }
    }
}
