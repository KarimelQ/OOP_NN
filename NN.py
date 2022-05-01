from modules import *
from utilities import *

# test branch 

# test commit 1

if __name__ == "__main__":
    X_train, y_train, X_test, y_test = load_data()
    X_train=X_train.reshape(X_train.shape[0],X_train.shape[1]*X_train.shape[2])/255
    X_test=X_test.reshape(X_test.shape[0],X_test.shape[1]*X_test.shape[2])/255
    
    num_filters = 8
    filter_size = 3
    pool_size = 24

    NN = NeuralNetwork(format = Format.CNN ,input_vector= np.random.randn(4,1) ,hidden_neurones=[3], state='start' )
    
    print(NN.W.weights[2].shape)