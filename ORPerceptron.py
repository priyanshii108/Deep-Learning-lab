import numpy as np

def Orperceptron(x1, x2):
    w1, w2 = 1,1
    b = -0.5
    z = x1*w1 + x2*w2 + b
    return 1 if z>=0 else 0

inputs = [(1,1),(1,0),(0,1),(0,0)]
for x in inputs:
    print(x, "->", Orperceptron(x[0],x[1]))