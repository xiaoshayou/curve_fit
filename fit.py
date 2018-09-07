import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy import log


def f_1(x, A, B):
    # 对数模型
    return A*log(x)+B

data_raw = np.array([]) 

# 取出待拟合数据
f = open("C:\\Users\\admin\\Desktop\\test.txt",encoding='utf-8')
line = f.readline()
while line:
    data_raw = np.append(data_raw,line.split())
    line = f.readline()
f.close()
data_all = np.reshape(data_raw,(-1,2))

sample_start = 1
sample_end = 100

x = data_all[sample_start:sample_end,0].astype(int)
y = data_all[sample_start:sample_end,1].astype(float)
A2, B2 = optimize.curve_fit(f_1, x, y)[0]

print(A2)
print(B2)

# 拟合后的数据
x_test = x
y_test = A2*log(x_test) + B2

# 画图
plt.scatter(x, y)
plt.plot(x_test, y_test, "red")
