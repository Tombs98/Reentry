def draw_map(data, risk):
    '''

    :param data:
    :return:
    '''
    html_f = open('./ht/landing_map.html', 'w')
    html = "<!DOCTYPE html><html><head><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /><meta name='viewport' content='initial-scale=1.0, user-scalable=no' /><style type='text/css'>body, html,#allmap {width: 100%;height: 100%;overflow: hidden;margin:0;font-family:'微软雅黑';}</style><script type='text/javascript' src='https://api.map.baidu.com/api?v=3.0&ak=yPjziotVjiAG26EqL9OvdG2kGHDQtR0j&s=1'></script><title>Landing_map</title></head><body><div id='allmap'></div></body></html>"
    html_f.write(html)
    js_va = "<script type='text/javascript'>function fun_map(){var map = new BMap.Map('allmap'); point_arr = []; circle_arr = [];var circle;var point;var marker;var opt = {width : 200,height : 100,};var infoWindow;"
    html_f.write(js_va)
    js_data = "data = [["+str(data[0][0])+","+str(data[0][1])+","+str(data[0][2])+","+str(data[0][3])+","+str(data[0][4])+"],["+str(data[1][0])+","+str(data[1][1])+","+str(data[1][2])+","+str(data[1][3])+","+str(data[1][4])+"],["+str(data[2][0])+","+str(data[2][1])+","+str(data[2][2])+","+str(data[2][3])+","+str(data[2][4])+"],["+str(data[3][0])+","+str(data[3][1])+","+str(data[3][2])+","+str(data[3][3])+","+str(data[3][4])+"],["+str(data[4][0])+","+str(data[4][1])+","+str(data[4][2])+","+str(data[4][3])+","+str(data[4][4])+"],["+str(data[5][0])+","+str(data[5][1])+","+str(data[5][2])+","+str(data[5][3])+","+str(data[5][4])+"],["+str(data[6][0])+","+str(data[6][1])+","+str(data[6][2])+","+str(data[6][3])+","+str(data[6][4])+"]];"
    html_f.write(js_data)
    js_risk = "risk = ["+str(risk[0])+","+str(risk[1])+","+str(risk[2])+","+str(risk[3])+","+str(risk[4])+","+str(risk[5])+","+str(risk[6])+"];"
    html_f.write(js_risk)
    js_color = "color=['green', 'blue', 'yellow', 'orange', 'red'];"
    html_f.write(js_color)
    js_fun = "for(let i = 0 ; i < 7; i++){point = new BMap.Point(data[i][2], data[i][3]);marker = new BMap.Marker(point);if(risk[i] ===0){circle = new BMap.Circle(point,9000,{ fillColor: color[risk[i]], strokeWeight:1, fillOpacity: 0.2, strokeOpacity:0.5});map.addOverlay(circle);}else{for(let j = 0; j < risk[i]; j++){circle = new BMap.Circle(point,9000+j*3000,{ fillColor: color[risk[i]-j], strokeWeight:1, fillOpacity: risk[i]*0.1, strokeOpacity:0.5});map.addOverlay(circle);}}map.addOverlay(marker);content = 'type_num:' + data[i][0] + '<br>mass(kg):' + data[i][1] + '<br>Lamda(deg):' + data[i][2] + '<br>B(deg):' + data[i][3] + '<br>V(m/s):' + data[i][4];addInfo(marker, content); point_arr.push(point);};"
    html_f.write(js_fun)
    js_add_fun = "function addInfo(m, c ){var infoWindow =  new BMap.InfoWindow(c,opt);m.onclick = function(){m.openInfoWindow(infoWindow);}}"
    html_f.write(js_add_fun)
    js_end = "        temp = parseInt(point_arr.length / 2); map.centerAndZoom(point_arr[temp], 1); map.enableScrollWheelZoom(true);};fun_map();</script>"
    html_f.write(js_end)
    html_f.close()