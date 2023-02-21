import os

import numpy as np
path = './ht/input/in.dat'
def in_process():
    temp = []
    res = [0, 0, 0, 0, 0, 0]
    with open(path, 'rb') as f:
        lines = f.readlines()
        for line in lines:
            line = str(line, encoding='utf-8')
            l = line.split()
            temp.append(l)

    res[0] = float(temp[3][2]) #地面坐标系原点经度
    res[1] = float(temp[5][2]) #地面坐标系原点纬度
    res[2] = float(temp[7][2]) #地面坐标系方位角
    res[3] = float(temp[9][2]) #初始时刻高度
    res[4] = float(temp[11][2]) #初始时刻速度
    res[5] = float(temp[13][2]) #初始时刻弹道倾角
    return res

def out_process(path, result):
    file = open(path, 'w')
    header = ["type_num", "mass(kg)", "Lamda(deg)", "B(deg)", "Velocity(m/s)"]

    for i in range(len(header)):
        file.write(header[i])
        for blank in range(5):
            file.write(" ")
        for j in range(len(result)):
            file.write(str(result[j][i]))
            for blank in range(5):
                file.write(" ")
        file.write("\n")
        file.write("\n")






