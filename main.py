import datetime
start = datetime.datetime.now()
import in_and_out
import predict
import write_html
import risk_def
if __name__ == "__main__":
    out_path = './ht/output/out.dat'
    #获取文件输入数据
    input_data = in_and_out.in_process()
    print("input ", input_data)
    #将输入数据进行预测
    result = predict.predict(input_data)
    # re = testCity.city(result)
    print("result", result)

    #导出到out文件
    in_and_out.out_process(out_path, result)
    #风险度定义
    risk_rank = risk_def.get_info(result)
    print("risk_rank", risk_rank)
    write_html.draw_map(result, risk_rank)

end = datetime.datetime.now()
print("time:   ", end-start)