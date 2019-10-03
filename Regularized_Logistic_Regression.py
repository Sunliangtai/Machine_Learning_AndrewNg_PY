import numpy as np
from math import *
import matplotlib.pyplot as plt
import time

file = open("D:\\Download\\machine-learning-ex2\\ex2\\ex2data2.txt")
data = file.read()
data_1 = data.split("\n")
data_1 = list(data_1)
x1 = []
x2 = []
y = []
for i in range(len(data_1)-1):
    a, b, c = data_1[i].split(',')
    x1.append(float(a))
    x2.append(float(b))
    y.append(float(c))

xita = np.matrix([[1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0]])
m = len(x1)
X = []

alpha = 0.003
lambd = 0.001

for i in range(m):
    X.append([1, x1[i], x2[i], x1[i]**2, x1[i]*x2[i], x2[i]**2, x1[i]**3, x1[i]**2*x2[i], x1[i]*x2[i]**2, x2[i]**3, x1[i]**4, x1[i]**3*x2[i], x1[i]**2*x2[i]**2, x1[i]*x2[i]**3, x2[i]**4, x1[i]**5, x1[i]**4*x2[i], x1[i]**3*x2[i]**2, x1[i]**2*x2[i]**3, x1[i]*x2[i]**4, x2[i]**5, x1[i]**6, x1[i]**5*x2[i], x1[i]**4*x2[i]**2, x1[i]**3*x2[i]**3, x1[i]**2*x2[i]**4, x1[i]*x2[i]**5, x2[i]**6])

def sigmoid(x):
    value = np.matrix(x)@xita
    return 1/(1+exp((-1*value)))


def cost():
    costVal = 0
    for i in range(m):
        if y[i] == 0:
            costVal += -log(1-sigmoid(X[i]))
        else:
            costVal += -log(sigmoid(X[i]))
    for i in range(1, 28):
        costVal += (lambd/2)*float(xita[i][0])**2
    return costVal/m


def update():
    global xita
    global X
    gradiant = 0
    for j in range(len(X)):
        gradiant += (sigmoid(X[j])-y[j])*X[j][0]
    gradiant /= m
    xita[0][0] -= float(alpha*gradiant)

    for i in range(1, len(xita)):
        gradiant = 0
        for j in range(len(X)):
            gradiant += (sigmoid(X[j])-y[j])*X[j][i]
        gradiant /= m
        gradiant += (lambd/m)*float(xita[i][0])
        xita[i][0] -= float(alpha*gradiant)
    

print(time.asctime(time.localtime(time.time())))
cos = cost()
for t in range(10000):  
    update()
    cos = cost()
    print("cost: ", cos)

print(xita)
for i in range(len(x1)):
    if y[i] == 0:
        plt.scatter(x1[i], x2[i], marker='o', c='b', s=20)
    else:
        plt.scatter(x1[i], x2[i], marker='x', c='r', s=20)

print(time.asctime(time.localtime(time.time())))

plt.show()