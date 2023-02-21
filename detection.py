#导入模块
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#构造一组随机数据
x=[1,2,3,4,5,6,7]
y=[0.00819397,0.00909381,0.00790912,0.00824792,0.00662589,0.00738348,0.0091104]

#画散点图和直方图
fig = plt.figure()
plt.bar(x, y, 0.3, facecolor = 'red', edgecolor = 'white')
plt.xlabel("debris number")
plt.ylabel("error(m/s)")
plt.title("Velocity error")



plt.show()