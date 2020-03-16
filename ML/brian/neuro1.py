from numpy import exp, array, random, dot

class neural_network:
    def __init__(self):
        random.seed(1)
        # We model a single neuron, with 3 inputs and 1 output and assign random weight.
        self.weights = 2 * random.random((2, 1)) - 1

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01*dot(inputs.T, error)
            self.weights += adjustment

    def think(self, inputs):
        return (dot(inputs, self.weights))

