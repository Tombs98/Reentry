'''
处理landing.dat
'''
import op_in
import file_op

out_file = file_op.out_file

out_file2 = file_op.out_file2

def sss(a):
    '''
    去重复空格
    :param a:
    '''
    if len(a) > 0:
        return a

def op_out(file):
    res_t = []
    res_v = []
    for i in range(len(file)):
        temp = []
        re = []
        v = []
        for line in open(file[i], 'r', encoding='utf-8'):
            s = line.strip().split('\t')
            temp.append(s)
        for i in range(2, len(temp)):
            res = [0, 0] #经纬度
            te_s = str(temp[i][0])
            te_l = te_s.split(" ")
            te_s = list(filter(sss, te_l))

            # 经纬度
            res[0] = te_s[4]  # Lamda
            res[1] = te_s[5]  # Bv
            v.append(te_s[7])  # V
            re.append(res)
        res_v.append(v)
        res_t.append(re)
    return res_t, res_v  # 所有的landing.dat文件夹的数据
# 最终格式为三维
# a[i]为一个case里面的7对经纬度 a[i][j]为一个case的第j对  a[0][0][0]为某对的经度或纬度
result_t, result_v = op_out(out_file)
result1_t, result1_v = op_out(out_file2)

def last():
    last_t = []
    last_v = []
    for j in range(7):
        for i in range(op_in.count[j] - 1):
            last_t.append(result1_t[j])
            last_v.append(result1_v[j])
    return last_t, last_v
#把2021-01-19文件的每个case的landing_aera里的数据条数跟input.dat的数据条数对应
result2_t, result2_v = last()

#1489条经纬度
out_all = result_t + result2_t
out_v = result_v + result2_v
