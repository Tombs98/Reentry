import csv
import xlrd
import numpy as np

gpw_path = './gpw_v4_admin_unit_center_points_population_estimates_rev11_asia.csv'
china_path = './china.xlsx'
world_path = './all_country.xls'

def dataObtain():
    '''
    获取落点城市人口和经济的信息
    :return:
    density 城市人口密度
    '''

    # 获取人口
    density = [] #密度
    location_X = [] #经度
    location_Y = [] #纬度
    city = []
    country = []
    with open(gpw_path, 'r') as f:
        reader = csv.reader(f)
        print(type(reader))
        index = 0
        for i in reader:
            if index == 0:
                index = index + 1
                continue
            else:
                city.append(i[3])  #到省  i[4]市  5县
                country.append(i[2])
                location_X.append(i[9])
                location_Y.append(i[10])
                density.append(i[28])

        #获取经济
        #中国按省份
        china_gdp = []
        china_g = xlrd.open_workbook(china_path)
        sheet = china_g.sheet_by_index(0)
        cols = sheet.col_values(2)
        cols1 = sheet.col_values(0)

        for i in range(1, len(cols)):
            temp = [0, 0]
            temp[0] = cols1[i]
            temp[1] = cols[i]
            china_gdp.append(temp)

        #外国按国家
        world_gdp = []
        world_g = xlrd.open_workbook(world_path)
        shee = world_g.sheet_by_index(0)
        col = shee.col_values(3)
        col1 = shee.col_values(0)

        for i in range(4, len(col)):
            temp = [0, 0]
            temp[0] = col1[i]
            temp[1] = col[i]
            world_gdp.append(temp)

    return location_X, location_Y, density, city, country, china_gdp, world_gdp



def findSmall(arr):
    '''
    返回列表最小值索引
    :param arr:
    :return: 最小值索引
    '''
    small = arr[0]
    small_index = 0
    for i in range(len(arr)):
        if small > arr[i]:
            small = arr[i]
            small_index = i

    return small_index


def calDensity(l_b, location_x, location_y):
    '''
    :param l_x: 经度
    :param l_y: 纬度
    :return: density 落点人口密度
    '''

    index = []
    print(l_b[0][0])
    for j in range(len(l_b)):
        diff_sum = []
        for i in range(len(location_x)):
            x = float(location_x[i]) - l_b[j][0]
            y = float(location_y[i]) - l_b[j][1]
            if x < 0:
                x = 0 - x
            if y < 0:
                y = 0 - y
            sum = x + y
            diff_sum.append(sum)
        ind = findSmall(diff_sum)
        index.append(ind)
    return index

def ret_data(l_b):
    '''
    根据经纬度获取当地的经济人口情况
    :param l_b:
    :return:
    '''

    location_x, location_y, density, city, country, china_gdp, world_gdp = dataObtain()
    index = calDensity(l_b, location_x, location_y)

    population = []
    econo = []
    for i in range(len(index)):
        #获取人口密度
        population.append(np.float(density[index[i]]))

        #获取gdp
        gdp = 0
        if country[index[i]] =='China':
            if city[index[i]] == 'NA':
                gdp = 0
            else:
                for na in range(len(china_gdp)):
                    if city[index[i]] == china_gdp[na][0]:
                        gdp = china_gdp[na][1]
        else:
            for co in range(len(world_gdp)):
                if country[index[i]] == world_gdp[co][0]:
                    gdp = world_gdp[co][1]
        econo.append(gdp)

    return econo, population



