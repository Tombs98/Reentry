import os

# 1.读取数据路径

def file_op(path):
    filelist = os.listdir(path)
    p1 = []  # in文件
    p2 = []  # out文件
    for f in filelist:
        if f == '.DS_Store':  # 解压可能会出现这个文件夹
            continue
        old = os.path.join(path, f)
        path1 = old + '/in.dat'
        path2 = old + '/landing_aera.dat'
        p1.append(path1)
        p2.append(path2)
    return p1, p2

path = './temp'  # 对应自己的文件路径
in_file, out_file = file_op(path)

path2 = './2021-01-19'
in_file2, out_file2 = file_op(path2)