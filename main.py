from flask import Flask
from MessageController import *
app = Flask(__name__)
@app.route('/api/alert')
def api_alert():
    msgController = MessageController()

    msgController.send_warningMsg( receivers = ['191977649@qq.com'])

    # numbers = ["+61433161557","+61405574088","+61457289459","+61432511606"]
    # msgController.send_sms(receivers=numbers)
    print("Alert Send")
    return "Alert Send"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)