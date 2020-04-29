import numpy as np;
from Renderer import Renderer;
class NeuronNetwork : 
    def __init__(self, data) :
        self.mistery_flower = [4.5, 1];
        self.learning_rate = 0.2;
        self.costs = [];
        self.data = data;
        self.render = Renderer();
        self.w1 = np.random.randn();
        self.w2 = np.random.randn();
        self.b = np.random.randn();
        CC = [4.5, 1];
        T  = np.linspace(-20, 20 , 100);
        Y = self.sigmoid(T);
        Y_P = self.sigmoid_pred(T);
        #print(T);
        #print(Y);
        #self.render.scatter(self.data);

        self.trainNN();
        #self.printResults();
        z = self.mistery_flower[0] * self.w1 + self.mistery_flower[0] * self.w2 + self.b;
        pred = self.sigmoid(z);
        print(pred);
        return;
        
        self.render.renderSigmoid(T, Y, 'r');
        self.render.renderSigmoid(T, Y_P, 'b');
        self.render.renderSigmoidPlt();
        #print(self.w1);

    def sigmoid(self, x) : 
        return 1 / (1 + np.exp(-x));

    def sigmoid_pred(self, x) : 
        return self.sigmoid(x) * (1 -self.sigmoid(x));

    def printResults(self) :

        for i in range(len(self.data)) :
            point = self.data[i];
            print(point);
            z = point[0] * self.w1 + point[1] * self.w2 + self.b;
            pred = self.sigmoid(z);
            #print("pred : {}".format(pred));

    def trainNN(self) :
        #data = self.data;
        for i in range(50000) :
            ri = np.random.randint(len(self.data));
            point = self.data[ri];
            z = point[0] * self.w1 + point[1] * self.w2 + self.b;
            pred = self.sigmoid(z);
            target = point[2];
            cost = np.square(pred - target);
            dcost_pred = 2 * (pred - target);
            dpred_dz = self.sigmoid_pred(z); 
            dz_dw1 = point[0];
            dz_dw2 = point[1];
            dz_db = 1;
            dcost_dz = dcost_pred * dpred_dz;
            dcost_dw1 = dcost_dz * dz_dw1;
            dcost_dw2 = dcost_dz * dz_dw2;
            dcost_db = dcost_dz * dz_db;
            self.w1 = self.w1 - self.learning_rate * dcost_dw1;
            self.w2 = self.w2 - self.learning_rate * dcost_dw2;
            self.b = self.b - self.learning_rate * dcost_db;
            if i % 100 == 0 :
                cost_sum = 0;
                for j in range(len(self.data)) :
                    point = self.data[ri];
                    z = point[0] * self.w1 + point[1] * self.w2 + self.b;
                    pred = self.sigmoid(z);
                    target = point[2];
                    cost_sum += np.square(pred - target);

                self.costs.append(cost_sum / len(self.data));

        #self.render.renderCosts(self.costs);
        #self.render.renderSigmoidPlt();
            


