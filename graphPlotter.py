import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np

class graphPlotter():

    def __init__(self, name, data, metadata):
        self.fig, self.ax = plt.subplots()
        self.ax.grid(which='major', color='k')
        self.name = name
        self.data = data
        self.metadata = metadata

    def plotFile(self, s0=0, s=0, mn=np.array([0, 1])):

        if 'Oscilloscope' in self.name:
            numb = self.metadata['Number Of Channels']
            if s==0:
                s = int(numb)
            for i in range(s0, s):
                self.ax.scatter(self.data[0], self.data[i], s=3)
                self.ax.legend(['Channel_'+str(i+1) for i in range(s)])
            plt.show()

        elif 'Shimadzu' in self.name:
            numb = int(len(self.metadata['exp']))
            subnumb = int(len(self.metadata['attrib']))
            if s==0:
                s = numb
            for i in range(s0, s):
                m = mn[0] + subnumb*i
                n = mn[1] + subnumb*i
                self.ax.scatter(self.data[m], self.data[n], s=3)
                self.ax.legend(self.metadata['exp'])
            plt.show()

        elif 'MI-40KU' in self.name:
            s = self.data.columns[-1]
            for i in range(s):
                self.ax.scatter(self.data[0], self.data[i], s=3)
                self.ax.legend([str(i+1) for i in range(s)])
            plt.show()

        elif 'sensor' in self.name:
            x = [i for i in range(len(self.data[0]))]
            for i in range(4):
                self.ax.scatter(x, self.data[i], s=3)
            plt.show()
