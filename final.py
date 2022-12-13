import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def transpose(A):
    tra = []
    row = len(A)
    col = len(A[0])
    for i in range(0,col):
        tem = []
        for j in range(0,row):
            tem.append(A[j][i])
        tra.append(tem)
    return tra


def multiply(A,B):
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])
    mlt = []
    for i in range(0,rowA):
        tem = []
        for j in range(0,colB):
            tot = 0
            for k in range(0,colA):
                tot += A[i][k]*B[k][j]
            tem.append(tot)
        mlt.append(tem)
    return mlt

def inverseFor2x2(A):
    inverse = [[],[]]
    det = A[0][0]*A[1][1]-A[1][0]*A[0][1]
    inverse[0].append(A[1][1]/det)
    inverse[0].append(-1*A[0][1]/det)
    inverse[1].append(-1*A[1][0]/det)
    inverse[1].append(A[0][0]/det)
    return inverse

def getX(A,b):
    return multiply(multiply(inverseFor2x2(multiply(transpose(A),A)),transpose(A)),b)

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv("清交學生回家頻率與影響因素之調查 (回覆) - 表單回應 1.csv")

city = []
for i in data["居住縣市"]:
    city.append(i)

frequency = []
for i in data["回家頻率(?週一次，填數字即可)\r\n"]:
    frequency.append(int(i))

time = []
for i in data["回家路程時長(單位:小時)\r\n(例:1、2.5)"]:
    time.append(float(i))

cost = []
for i in data["回家所需交通費(抓單程，大概即可)"]:
    cost.append(int(i))

#回家時間-頻率
plt.subplot(2,1,1)
plt.scatter(time,frequency)
plt.xlabel("回家時間(hr)")
plt.ylabel("多久回家一次(week)")
A = []
b = []
for i in time:
    A.append([1,i])
for i in frequency:
    b.append([i])
x = getX(A,b)
xdot = []
ydot = []
for i in range(0,7):
    xdot.append(i)
    ydot.append(x[0][0]+i*x[1][0])
plt.plot(xdot,ydot,c='r')


#回家花費-頻率
plt.subplot(2,1,2)
plt.scatter(cost,frequency)
plt.xlabel("回家花費(TWD)")
plt.ylabel("多久回家一次(week)")
A = []
b = []
for i in cost:
    A.append([1,i])
for i in frequency:
    b.append([i])
x = getX(A,b)
xdot = []
ydot = []
for i in range(0,2000):
    xdot.append(i)
    ydot.append(x[0][0]+i*x[1][0])
plt.plot(xdot,ydot,c='r')

plt.show()
