<?php

class NeuralNetwork
{
    private $inputsNumber = 3;
    private $inputsNames = ['Dnu', 'numax', 'epsilon'];

    public function getInputsNames()
    {
        return $this->inputsNames;
    }

    public function calculateOutputs($inputs)
    {
        $scaledDnu = ($inputs[0] - 5.878520012) / 3.069350004;
        $scaledNumax = ($inputs[1] - 60.00109863) / 44.48839951;
        $scaledEpsilon = ($inputs[2] - 0.5984969735) / 0.343885988;

        $perceptronLayer1Output0 = tanh(-1.08472 + ($scaledDnu * 8.83468) + ($scaledNumax * -1.54039) + ($scaledEpsilon * -3.6386));
        $perceptronLayer1Output1 = tanh(0.761358 + ($scaledDnu * 5.24602) + ($scaledNumax * -4.54935) + ($scaledEpsilon * 0.143989));
        $perceptronLayer1Output2 = tanh(-0.98733 + ($scaledDnu * 2.20786) + ($scaledNumax * 1.89229) + ($scaledEpsilon * -0.229483));
        $perceptronLayer1Output3 = tanh(0.850799 + ($scaledDnu * -7.41337) + ($scaledNumax * 1.75661) + ($scaledEpsilon * 2.89557));
        $perceptronLayer1Output4 = tanh(-2.25198 + ($scaledDnu * -2.47969) + ($scaledNumax * 2.12309) + ($scaledEpsilon * -1.58168));
        $perceptronLayer1Output5 = tanh(2.09279 + ($scaledDnu * -3.42202) + ($scaledNumax * 1.11115) + ($scaledEpsilon * -3.78158));

        $probabilisticLayerCombinations0 = 6.35881 - 6.07271 * $perceptronLayer1Output0
            - 4.87637 * $perceptronLayer1Output1 + 1.9414 * $perceptronLayer1Output2
            + 4.08944 * $perceptronLayer1Output3 + 4.46508 * $perceptronLayer1Output4
            + 4.4078 * $perceptronLayer1Output5;

        $pop = 1.0 / (1.0 + exp(-$probabilisticLayerCombinations0));

        return [$pop];
    }

    public function calculateBatchOutput($inputBatch)
    {
        $outputBatch = [];

        foreach ($inputBatch as $inputs) {
            $output = $this->calculateOutputs($inputs);
            $outputBatch[] = $output;
        }

        return $outputBatch;
    }
}

$nn = new NeuralNetwork();

$userInputs = [];
foreach ($nn->getInputsNames() as $inputName) {
    echo "Enter value for $inputName: ";
    $value = floatval(trim(fgets(STDIN)));
    $userInputs[] = $value;
}

$result = $nn->calculateOutputs($userInputs);
$roundedResult = round($result[0]);

if ($roundedResult == 0) {
    echo "The result is 0, so the star is RGB (Red Giant Branch)\n";
} elseif ($roundedResult == 1) {
    echo "The result is 1, so the star is HeB (Helium Burning)\n";
} else {
    echo "The result is neither 0 nor 1, unable to determine star type.\n";
}
