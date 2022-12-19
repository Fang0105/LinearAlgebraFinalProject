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

cityName = ["基隆市","台北市","新北市","桃園市","新竹縣","新竹市","苗栗縣","台中市","彰化縣","南投縣","雲林縣","嘉義縣","嘉義市","台南市","高雄市","屏東縣","宜蘭縣","花蓮縣","台東縣","澎湖縣","金門縣","連江縣"]
cityDis = [    0    , 83.9  , 78.3  ,  57.0  ,  6.1  ,    0  ,   38.6 ,   102  ,  112  ,   0   ,    152 ,  169   ,  182  ,  240  ,   282  ,  293  ,   0    ,   238 ,    0   ,   0   ,   0   ,    0   ]
frequency = []
time = []
cost = []
dis = []
dict = {}
idx = 0
for i in cityName:
    dict[i] = [0,0,cityDis[idx]]
    idx+=1
for index,row in data.iterrows():
    frequency.append(int(row["回家頻率(?週一次，填數字即可)\r\n"]))
    time.append(float(row["回家路程時長(單位:小時)\r\n(例:1、2.5)"]))
    cost.append(int(row["回家所需交通費(抓單程，大概即可)"]))
    dict[row["居住縣市"]][0]+=1
    dict[row["居住縣市"]][1]+=row["回家頻率(?週一次，填數字即可)\r\n"]
    dis.append(dict[row["居住縣市"]][2])


#回家時間-頻率
plt.subplot(4,1,1)
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
plt.subplot(4,1,2)
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

#縣市-頻率
x = []
h = []
label = []
cnt = 1
for i in dict:
    if dict[i][0]!=0:
        x.append(cnt)
        cnt+=1
        h.append(dict[i][1]/dict[i][0])
        label.append(i)
plt.subplot(4,1,3)
plt.bar(x,h,tick_label=label)
plt.xlabel("縣市")
plt.ylabel("平均多久回家一次(week)")

#縣市距離-頻率
plt.subplot(4,1,4)
plt.xlabel("縣市火車站與新竹火車站的距離(km)")
plt.ylabel("多久回家一次(week)")
plt.scatter(dis,frequency)
A = []
b = []
for i in dis:
    A.append([1,i])
for i in frequency:
    b.append([i])
x = getX(A,b)
xdot = []
ydot = []
for i in range(0,300):
    xdot.append(i)
    ydot.append(x[0][0]+i*x[1][0])
plt.plot(xdot,ydot,c='r')

plt.tight_layout()
plt.show()