import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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


plt.subplot(2,1,1)
plt.scatter(time,frequency)
plt.xlabel("回家時間(hr)")
plt.ylabel("多久回家一次(week)")

plt.subplot(2,1,2)
plt.scatter(cost,frequency)
plt.xlabel("回家花費(TWD)")
plt.ylabel("多久回家一次(week)")
plt.show()

