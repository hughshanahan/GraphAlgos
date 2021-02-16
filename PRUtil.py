import numpy as np

# myA is an adjacency matrix with integer entries

def findDegree(myA):
# return a vector with the number of non-zero entries per row
        n = myA.shape[0]
        deg = np.sum(myA, axis=1)

        return deg

def computePT(myA):
        P = myA.copy()
        n = myA.shape[0]
        deg = findDegree(myA)
        for i in range(0,n):
                for j in range(0,n):
                        if ( deg[i] > 0.0 ):
                                P[i,j] /= deg[i]

        return np.transpose(P)
