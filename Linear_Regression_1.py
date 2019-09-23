import matplotlib.pyplot as plt


def lose_function(X, y, xita0, xita1, m):
    answer = 0
    for i in range(m):
        answer += (xita1*X[i]+xita0-y[i])**2
    answer /= 2*m
    return answer


def xita0_change(X, y, xita0, xita1, m):
    answer = 0
    for i in range(m):
        answer += (xita1*X[i]+xita0-y[i])
    answer /= m
    return answer


def xita1_change(X, y, xita0, xita1, m):
    answer = 0
    for i in range(m):
        answer += (xita1*X[i]+xita0-y[i])*X[i]
    answer /= m
    return answer


alpha = 0.015
xita0 = 0
xita1 = 1
lose = []
iteration = []

file = open("D:\\Download\\machine-learning-ex1\\ex1\\ex1data1.txt")
data = file.read()
data_1 = data.split("\n")
data_1 = list(data_1)
X = []
y = []
for i in range(len(data_1)-1):
    a, b = data_1[i].split(',')
    X.append(float(a))
    y.append(float(b))

m = len(X)

for time in range(10000):
    iteration.append(time)
    lose_tmp = lose_function(X, y, xita0, xita1, m)
    lose.append(lose_tmp)
    print("lose:", lose_tmp)
    xita0_C = xita0_change(X, y, xita0, xita1, m)
    xita1_C = xita1_change(X, y, xita0, xita1, m)
    xita0 -= alpha*xita0_C
    xita1 -= alpha*xita1_C


print("y="+str(xita0)+"+"+str(xita1)+"*x")
plt.plot(iteration, lose)
plt.show()
