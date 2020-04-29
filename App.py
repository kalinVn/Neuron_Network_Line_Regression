from NeuronNetwork import NeuronNetwork

class App : 
    def __init__(self) :
        self.data = [
            [3, 1.5, 1],
            [2, 1, 0],
            [4, 1.5, 1],
            [3, 1, 0],
            [3.5, .5, 1],
            [2, .5, 0],
            [5.5, 1, 1],
            [1, 1, 0]

        ];
        
        #print(self.data[0]);
        NN = NeuronNetwork(self.data);

app = App();
    
