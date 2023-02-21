import requests


import json
def city(lb):
    '''
    根据预测所得得经纬度，得到对应的城市，采用了百度地图API，需要在联网状态使用
    :return:
    '''
    district = []
    C = []
    province = []
    total_add = []
    for i in range(7):
        t = str(lb[i][1])
        t = t + ','
        t = t + str(lb[i][0])
        r = requests.get(url='http://api.map.baidu.com/reverse_geocoding/v3/', params={'location':t, 'ak':'pRhpisRaqLkjjG1HtZNkqEyPx50c8WGa','output':'json'})
        result = r.json()

        #落点县
        dis = result['result']['addressComponent']['district']
        district.append(dis)

        #落点城市
        city = result['result']['addressComponent']['city']
        C.append(city)

        #落点省份
        pro = result['result']['addressComponent']['province']
        province.append(pro)

        #落点详细地址
        total = result['result']['formatted_address']
        total_add.append(total)
    print(total_add)
    return province

# def test():
#     r = requests.get(url='http://api.map.baidu.com/reverse_geocoding/v3/',params={'location': '40.91928525,120.6382093', 'ak': 'pRhpisRaqLkjjG1HtZNkqEyPx50c8WGa', 'output': 'json'})
#     result = r.json()
#     print(result)
# test()