from flask import Flask
from MessageController import *
app = Flask(__name__)
@app.route('/api/alert')
def api_alert():
    msgController = MessageController()
    msgController.send_warningMsg( receivers = ['191977649@qq.com','gta191977649@live.com','sxd210@qq.com','gengfa.fang@uts.edu.au','gengfa.fang@gmail.com','12755575@student.uts.edu.au','Ramya.Mopidevi@sas.com','Andrew.Gu@sas.com'])
    numbers = ["+61433161557","+61405574088","+61457289459","+61432511606"]
    msgController.send_sms(receivers=numbers)
    print("Alert Send")
    return "Alert Send"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)