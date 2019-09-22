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

xita_1 = []
xita_0 = []
lose = []
xita_0.append(xita0)
xita_1.append(xita1)


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
    lose_tmp = lose_function(X, y, xita0, xita1, m)
    lose.append(lose_tmp)
    print("lose:", lose_tmp)
    xita0_C = xita0_change(X, y, xita0, xita1, m)
    xita1_C = xita1_change(X, y, xita0, xita1, m)
    xita0 -= alpha*xita0_C
    xita1 -= alpha*xita1_C
    xita_0.append(xita0)
    xita_1.append(xita1)

all = len(xita_0)
xita_0_final = xita_0[all-1]
xita_1_final = xita_1[all-1]

print("y="+str(xita_0_final)+"+"+str(xita_1_final)+"*x")

plt.scatter(X, y, color="red")
Y = []
for i in X:
    Y.append(xita_0_final+i*xita_1_final)

plt.plot(X, Y, color="blue")
plt.show()
