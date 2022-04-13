import imp
import random
from enum import Enum
import numpy as np

class Format(Enum):
    CNN = 'conv network'
    RNN = 'Rec NN'
    DNN = 'Deep NN'
    RESNET = 'resnet'

class State(Enum):
    Start = 'start'
    Finish = 'finish'

class NeuralNetwork():
    def __init__(self, format:Format, state:State, input_vector, hidden_neurones, output_shape=2) -> None:
        #Layer_number is hidden layers number
        self.format = format
        self.number_layers = len(hidden_neurones)+1
        self.state = State
        self.input = input_vector
        self.W = Weights_handling(hidden_neurones, neurone_per_layer=[input_vector.shape[0],output_shape])
    def __str__(self) -> str:
        return f'[  {str(self.format.value)+ " of "} {str(self.number_layers)+" hidden layers" } ]'

    def is_trained(self):
        if( self.state == 'start'):
            return 1
        else:
            return 0

    def train(self):
        if(self.state == 'finish'):
            raise ValueError("already trained")
        #FF & BP
    
    def FF(self):
        def Forward_Propagation(X):
            L_Z = []
            L_A = []
            L_Z.append(NeuralNetwork.W.weights[0].dot(X) + NeuralNetwork.W.bias[0])
            L_A.append(np.abs(1))
            #correct and continue


 

class Weights_handling():
    def __init__(self, hidden_neurones, neurone_per_layer ):
        [ neurone_per_layer.insert((i+1),hidden_neurones[i]) for i in range(len(hidden_neurones))]    

        self.weights = [
            np.random.randn(neurone_per_layer[i+1],neurone_per_layer[i])
            for i in range( len(neurone_per_layer)-1 ) 
        ]
        self.bias = [
            np.random.randn(neurone_per_layer[i+1],1)
            for i in range( len(neurone_per_layer)-1 ) 
        ]

    def __str__(self) -> str:
        return f'[{len(self.weights)} ]'

# to continue
#https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/
