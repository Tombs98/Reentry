#训练机器学习模型

import numpy as np
import sklearn
import folium
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import linear_model
#from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
import op_in
from sklearn.neural_network import MLPRegressor

import model_list
import in_and_out
import joblib
# import webbrowser
import datetime


#获取所有31个case的碎片落点
# case_all = landing.result + landing.result1
# case_all = np.array(case_all, dtype=float)


in_all = np.array(op_in.in_all, dtype=float)

# #14个模型
# final = model_list.final

#落点经纬度数据
landing_data_t = model_list.output_t
#落点速度数据
landing_data_v = model_list.output_v

print(len(landing_data_t[0]))



# print("输入您想预测的值（经度、纬度、方位角、高度、速度、弹道倾角）：")
# a, b, c, d, e, f = map(float, input().split())
# p_in = test.in_process() #输入
# p_in.append(a)
# p_in.append(b)
# p_in.append(c)
# p_in.append(d)
# p_in.append(e)
# p_in.append(f)

#2.划分数据与标签
in_data = in_all #输入数据

'''
#14个模型
for i in range(14):
    train_data, test_data, train_label, test_label = sklearn.model_selection.train_test_split(x, final[i], random_state=1, train_size=0.6, test_size=0.4)
    #classifier = linear_model.LinearRegression()
    #classifier = tree.DecisionTreeClassifier()
    #classifier = DecisionTreeRegressor(max_depth=2)
    classifier = DecisionTreeRegressor(max_depth=5)
    #classifier = DecisionTreeRegressor(max_depth=8)
    classifier.fit(train_data, train_label) #训练svm分类器

    #3.输出七个碎片的经纬度预测值、模型准确率
    pre = classifier.predict([p_in])
    num = i//2
    if i%2==0:
        re[num][2] = pre
        print("碎片", re[num][0], "的经度", pre)
        print("训练集：", classifier.score(train_data, train_label))
        print("测试集：", classifier.score(test_data, test_label))
    else:
        re[num][3] = pre
        print("碎片", re[num][0], "的纬度", pre)
        print("训练集：", classifier.score(train_data, train_label))
        print("测试集：", classifier.score(test_data, test_label))
'''
p_in = in_and_out.in_process()
def predict(p_in):
    # 建立输出矩阵
    re = np.zeros((7, 5), dtype=float)

    '''
    碎片的质量和序号
    '''
    re[0][0] = 6
    re[1][0] = 16
    re[2][0] = 7
    re[3][0] = 13
    re[4][0] = 8
    re[5][0] = 15
    re[6][0] = 14
    re[0][1] = 0.160000E+02
    re[1][1] = 0.727000E+02
    re[2][1] = 0.650000E+02
    re[3][1] = 0.225500E+03
    re[4][1] = 0.800000E+01
    re[5][1] = 0.207000E+02
    re[6][1] = 0.108500E+03

    lb_time = []
    v_time = []
    #经纬度预测
    for i in range(7):
        time = datetime.datetime.now()
        train_data, test_data, train_label, test_label = sklearn.model_selection.train_test_split(in_data, landing_data_t[i], random_state=1, train_size=0.6, test_size=0.4)
        #classifier = linear_model.LinearRegression()
        #classifier = tree.DecisionTreeClassifier()
        #classifier = DecisionTreeRegressor(max_depth=2)
        # from yellowbrick.features import FeatureImportances
        de_tree =DecisionTreeRegressor(max_depth=5)

        svr_w = svm.SVR(kernel='rbf', C=100, gamma='auto', epsilon=6)
        svr_j = svm.SVR(kernel='rbf', C=100, gamma='auto', epsilon=6)
        # mlp_w = MLPRegressor(max_iter=500)
        # mlp_j = MLPRegressor(max_iter=500)
        #classifier = DecisionTreeRegressor(max_depth=8)
        de_tree.fit(train_data, train_label) #决策树回归
        # train_j = []
        # train_w = []
        # for j in range(len(train_label)):
        #     train_j.append(train_label[j][0])
        #     train_w.append(train_label[j][1])
        # test_j = []
        # test_w = []
        # for j in range(len(test_label)):
        #     test_j.append(test_label[j][0])
        #     test_w.append(test_label[j][1])
        # # mlp_w.fit(train_data, train_w)
        # # mlp_j.fit(train_data, train_label)
        # svr_j.fit(train_data, train_j)
        # svr_w.fit(train_data, train_w)
        #训练svm回归器
        # print("train_data", test_data[0:10])
        # print("train_label", train_label[0:10])
        #3.输出七个碎片的经纬度预测值、模型准确率
        pre = de_tree.predict([p_in])

        re[i][2] = pre[0][0] #经度
        re[i][3] = pre[0][1] #纬度
        # print("决策树回归误差：  经度    纬度")
        # sum = 0
        # for i in range(len(train_data)):
        #     y_ = de_tree.predict(train_data[[i]])
        #     y = train_label[i]
        #     sum += abs(y - y_)
        # mean = sum / len(train_data)
        # print(mean)
        # print("svm回归误差：  经度    纬度")
        # sum = 0
        # for i in range(len(test_data)):
        #     y_ = svr_w.predict(test_data[[i]])
        #     y = svr_test_w[i]
        #     sum += abs(y - y_)
        # mean = sum / len(train_data)
        # print(mean)
        # print("mlp回归误差：  经度    纬度")
        # sum = 0
        # for i in range(len(train_data)):
        #     y_ = mlp_j.predict(train_data[[i]])
        #     y = train_label[i]
        #     sum += abs(y - y_)
        # mean = sum / len(train_data)
        # print(mean)

        # re[i][4] = pre[0][2]
        # print("pre:", pre)
        # # print(pre)

        # print("训练集：", (svr_w.score(train_data, svr_train_w)+svr_j.score(train_data, svr_train_j))/2)
        # print("测试集：", (svr_w.score(test_data, svr_test_w)+svr_j.score(test_data, svr_test_j))/2)
        # print("训练集：", mlp_j.score(train_data, train_label))
        # print("测试集：", mlp_j.score(test_data, test_label))
        # print("训练集：", de_tree.score(train_data, train_label))
        # print("测试集：", de_tree.score(test_data, test_label))
        # joblib.dump(de_tree, 'model/lb.pkl')
        end = datetime.datetime.now()
        temp = (end - time)
        lb_time.append(temp)

    #速度预测
    for i in range(7):
        time = datetime.datetime.now()
        train_data, test_data, train_label, test_label = sklearn.model_selection.train_test_split(in_data,
                                                                                                  landing_data_v[i],
                                                                                                  random_state=1,
                                                                                                  train_size=0.6,
                                                                                                  test_size=0.4)
        de_tree = DecisionTreeRegressor()
        de_tree.fit(train_data, train_label)  # 训练svm分类器
        pre = de_tree.predict([p_in])
        re[i][4] = pre
        # print("pre:", pre)
        # # print(pre)
        # print("训练集：", de_tree.score(train_data, train_label))
        # print("测试集：", de_tree.score(test_data, test_label))
        # sum = 0
        # for oo in range(len(train_data)):
        #     y_ = de_tree.predict(train_data[[oo]])
        #     y = train_label[oo]
        #     sum += abs(y - y_)
        # mean = sum / len(train_data)
        # print("e")
        # print(mean)
        joblib.dump(de_tree, 'model/v.pkl')
        end = datetime.datetime.now()
        temp = (end -time)
        v_time.append(temp)

    print("time --------------")
    print(lb_time)
    print(np.array(lb_time).sum())
    print(np.array(v_time).sum())
    return re
predict(p_in)
