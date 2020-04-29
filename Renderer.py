from  matplotlib import pyplot as plt;
import numpy as np;
class Renderer : 
    def __init__(self) :
      pass;

    def renderSigmoid(self, T, Y, color) :
        plt.plot(T, Y, c = color);
    
    def renderSigmoidPlt(self) :
        plt.show();

    def scatter(self, data) : 
        plt.axis([0, 6, 0, 6]);
        plt.grid();
        for i in range(len(data)) :
            point = data[i];
            color = 'r'
            if point[2] == 0 :
                color = 'b'
            plt.scatter( point[0], point[1], c = color);
        self.renderSigmoidPlt();

    def renderCosts(self, costs) :
        plt.plot(costs);

