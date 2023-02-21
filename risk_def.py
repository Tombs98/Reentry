import which_city
import data_ach
import numpy as np

def get_info(landing_data):
    '''
    获取落点城市信息
    :param landing_data:
    :return:
    '''
    m_v = []
    l_b = []
    for i in range(len(landing_data)):

        #获取质量速度
        m_v_res = [0, 0]
        m_v_res[0] = landing_data[i][1]
        m_v_res[1] = landing_data[i][4]
        m_v.append(m_v_res)

        #获取经纬度
        l_b_res = [0, 0]
        l_b_res[0] = landing_data[i][2]
        l_b_res[1] = landing_data[i][3]
        l_b.append(l_b_res)
    #获取动能
    kinetic = get_kinetic(m_v)
    gdp, population = get_ep(l_b)
    risk = get_risk(gdp, population, kinetic)

    #获取经济人口情况
    return risk

def get_ep(landing_t):
    '''
    根据经纬度获取落点城市,以及当地的经济人口情况
    :param landing_t:
    :return:
    '''
    #根据经纬度获取城市
    #两个方案，1）通过百度地图API，获取到经纬度的城市，然后通过城市获取当地的经济人口情况
    # pr = which_city.city(landing_t)

    #2）直接通过经纬度，比较gpw文件中所有城市经纬度与落点经纬度的差值，差值最小的确定为落点

    #返回经济（中国为省份GDP，国外为国家GDP）、人口（密度）
    gdp, population = data_ach.ret_data(landing_t)
    print(gdp, population)
    return gdp, population



def get_kinetic(m_v):
    '''
    根据质量和速度计算动能
    :param m_v:
    :return:
    '''
    kinetic = []
    for i in range(len(m_v)):
        k = 1/2 * m_v[i][0] * m_v[i][1] * m_v[i][1]
        kinetic.append(k)
    return kinetic

def get_risk(gdp, population, kinetic):
    '''
    根据经济人口以及动能计算风险度
    :param ep:
    :param kinetic:
    :return:
    '''

    #归一化
    gdp = np.array(gdp)
    population = np.array(population)
    kinetic = np.array(kinetic)
    # gdp = normal(gdp)
    # population = normal(population)
    # kinetic = normal(kinetic)
    # print(population)
    # print(gdp)
    # print(kinetic)
    risk = []
    for i in range(len(gdp)):
        g = gdp[i]
        k = kinetic[i]
        p = population[i]
        r = (g * k * p) * 0.2
        risk.append(r)
    risk = normal(risk)

    #危险等级
    #采用布氏定律以 0.2为公差分别将其分为 5 个等份，区域泥石流风险的计算公式在 0～1
    # 取值范围相应构成 0 ~0.04， 0.04 ~0.16， 0.16 ~0.36， 0.36~ 0.64， 0.64 ~1.0 五个区段
    # 即由低到高分出 5 级，相应定名为：可忽略风险区，低风险区，中等风险区，高风险区和极高风险区
    print(risk)
    risk_rank = []
    for i in range(len(risk)):
        if risk[i]<=0.04:
            risk_rank.append(0)
        elif risk[i]<=0.16 and risk[i]>0.04:
            risk_rank.append(1)
        elif risk[i]<=0.36 and risk[i]>0.16:
            risk_rank.append(2)
        elif risk[i]<=0.64 and risk[i]>0.36:
            risk_rank.append(3)
        elif risk[i]<=1 and risk[i]>0.64:
            risk_rank.append(4)
    return risk_rank

def normal(data):
    '''
    归一化
    :param arr:
    :return:
    '''
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range