import random
from sklearn.neighbors import NearestNeighbors
import numpy as np
from numpy import loadtxt


xx = loadtxt('trainF.csv', delimiter=",")

class Smote:
    def __init__(self, samples, N=10, k=5):
        self.n_samples, self.n_attrs = samples.shape
        self.N = N
        self.k = k
        self.samples = samples
        self.newindex = 0
        # self.synthetic=np.zeros((self.n_samples*N,self.n_attrs))

    def over_sampling(self):
        N = int(self.N / 100)
        self.synthetic = np.zeros((self.n_samples * N, self.n_attrs))
        neighbors = NearestNeighbors(n_neighbors=self.k).fit(self.samples)
        #print('neighbors', neighbors)
        for i in range(len(self.samples)):
            nnarray = neighbors.kneighbors(self.samples[i].reshape(1, -1), return_distance=False)[0]
            # print nnarray
            self._populate(N, i, nnarray)
        return self.synthetic

    # for each minority class samples,choose N of the k nearest neighbors and generate N synthetic samples.
    def _populate(self, N, i, nnarray):
        for j in range(N):
            nn = random.randint(0, self.k - 1)
            dif = self.samples[nnarray[nn]] - self.samples[i]
            gap = random.random()
            self.synthetic[self.newindex] = self.samples[i] + gap * dif
            self.newindex += 1


def main():
    a = np.array([[1, 2, 3], [4, 5, 6], [2, 3, 1], [2, 1, 2], [2, 3, 4], [2, 3, 4]])
    a = np.array(xx)

    #print a
    s = Smote(a, N=200)
    #print type(s.over_sampling())
    x=s.over_sampling()
    x_list=x.tolist()
    #str_list=str(x_list[0])
    for j in range(0,len(x_list)):
    	 m=''
   	 for i in range(0,len(x_list[j])):
    		m=m+str(x_list[j][i])+','
   	 print m[:-1]
    #for i in range(0,len(x_list)):
    	#print ','.join(x_list[i])


if __name__ == '__main__':
    main()
