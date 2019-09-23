import matplotlib.pyplot as plt


def lose_function(x1, x2, y, xita0, xita1, xita2, m):
    answer = 0
    for i in range(m):
        answer += (xita0+xita1*x1[i]+xita2*x2[i]-y[i])**2
    answer /= 2*m
    return answer


def xita0_change(x1, x2, y, xita0, xita1, xita2, m):
    answer = 0
    for i in range(m):
        answer += (xita0+xita1*x1[i]+xita2*x2[i]-y[i])
    answer /= m
    return answer


def xita1_change(x1, x2, y, xita0, xita1, xita2, m):
    answer = 0
    for i in range(m):
        answer += (xita0+xita1*x1[i]+xita2*x2[i]-y[i])*x1[i]
    answer /= m
    return answer


def xita2_change(x1, x2, y, xita0, xita1, xita2, m):
    answer = 0
    for i in range(m):
        answer += (xita0+xita1*x1[i]+xita2*x2[i]-y[i])*x2[i]
    answer /= m
    return answer


file = open("D:\\Download\\machine-learning-ex1\\ex1\\ex1data2.txt")
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
    y.append(float(c)/100000)

m = len(x1)

ave = sum(x1)/m
_max = max(x1)
_min = min(x1)
for i in range(m):
    x1[i] = (x1[i]-ave)/(_max-_min)

alpha = 0.08
xita0 = 0
xita1 = 1
xita2 = 1

lose = []
iteration = []
for time in range(10000):
    iteration.append(time)
    lose_tmp = lose_function(x1, x2, y, xita0, xita1, xita2, m)
    print("lose:", lose_tmp)
    lose.append(lose_tmp)
    xita0_C = xita0_change(x1, x2, y, xita0, xita1, xita2, m)
    xita1_C = xita1_change(x1, x2, y, xita0, xita1, xita2, m)
    xita2_C = xita2_change(x1, x2, y, xita0, xita1, xita2, m)
    xita0 -= alpha*xita0_C
    xita1 -= alpha*xita1_C
    xita2 -= alpha*xita2_C

print("y="+str(xita0)+"+"+str(xita1)+"*x1"+"+"+str(xita2)+"*x2")
plt.plot(iteration, lose)
plt.show()
