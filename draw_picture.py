import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import model_list

from matplotlib.pyplot import MultipleLocator

#落点经纬度数据
landing_data_t = model_list.output_t
#落点速度数据
landing_data_v = model_list.output_v

index = 0
Y = []
K = []

X = []
for i in range(7*1489):
    X.append(i)
for i in range(len(landing_data_t)):
    for j in range(len(landing_data_t[i])):
        Y.append(landing_data_t[i][j][0])
        K.append(landing_data_t[i][j][1])

plt.scatter(X, K)


plt.ylabel("Latitude")
plt.xlabel("Sample")
plt.show()

