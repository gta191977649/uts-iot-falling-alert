from flask import Flask
from MessageController import *
app = Flask(__name__)
@app.route('/api/alert')
def api_alert():
    msgController = MessageController()
    msgController.send_warningMsg( receivers = ['191977649@qq.com','gta191977649@live.com'])

    print("Alert Send")
    return "Alert Send"

if __name__ == '__main__':
    app.run()