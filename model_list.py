#输入数据处理（14个模型的数据样式、7个模型的数据样式）

import landing
import numpy as np

out_all = landing.out_all
out_v = landing.out_v

# def mlist():
#     final = []
#     for j in range(7):
#         resp = []
#         resp1 = []
#         for i in range(len(out_all)):
#             resp.append(out_all[i][j][0])
#             resp1.append(out_all[i][j][1])
#         final.append(resp)
#         final.append(resp1)
#     return final
# #单输出，14个模型 碎片的经度、纬度放进数组里
# #j代表case里的第几个碎片，i代表第几个case
# #final[0]是 所有输出条数的 第1个碎片的经度，final[1]是第1个碎片的纬度，final[2]是第2个碎片的经度...
# final = np.array(mlist(), dtype=float)

def suipian():
    output_t = []
    output_v = []
    for i in range(7):
        out_t = [] #经纬度
        out_ve = [] #速度
        for j in range(len(out_all)):
            out_t.append(out_all[j][i])
            out_ve.append(out_v[j][i])
        output_t.append(out_t)
        output_v.append(out_ve)
        # for k in range(len())
    return output_t, output_v
#给决策树多输出 准备的，7个模型 每个碎片的经纬度序列
#最终格式为二维数组
#a[i]代表第几个碎片，a[i][j]为第几个碎片的case几里的经纬度
output_t, output_v = suipian()
output_t = np.array(output_t, dtype=float)
output_v = np.array(output_v, dtype=float)