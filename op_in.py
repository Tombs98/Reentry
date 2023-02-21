'''
处理in.dat
'''
import file_op

in_file = file_op.in_file

in_file2 = file_op.in_file2

def op_in(x):
    res_t = []
    for i in range(len(x)):
        temp = []
        res = [0, 0, 0, 0, 0, 0]
        for line in open(x[i], 'r', encoding='utf-8'):
            s = line.strip().split('\t')
            temp.append(s)
        res[0] = temp[3][2]
        res[1] = temp[5][2]
        res[2] = temp[7][2]
        res[3] = temp[9][4]
        res[4] = temp[11][4]
        res[5] = temp[13][4]
        res_t.append(res)
    return res_t  # 所有的in.dat文件夹的数据
# print(op_in())
# 最终格式为一个二维数组
# a[0] 为一个case里面的6个参数 可以通过a[0][i]获取对应参数

def op_in2(x):
    res_t = []
    for i in range(len(x)):
        data = []
        with open(x[i]) as f:
            for j, line in enumerate(f):
                if j < 1:
                    continue
                s = line.strip().split()
                data.append(s)
        res_t.extend(data)
    return res_t

in_all = op_in(in_file) + op_in2(in_file2)

# 获取2021-01-19每个文件的in.dat的行数
def file_line(x):
    count = []
    for i in range(len(x)):
        with open(x[i]) as f:
            text = f.read()
            length = len(text.splitlines())
        count.append(length)
    return count
count = file_line(in_file2)#每个文件的数据行数