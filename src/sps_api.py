from flask import Flask

from api import speedtest_router
from api import speedtest_batch_router

class SpsApi():
    @staticmethod
    def main():
        app = Flask(__name__)

        # ここにcontrollerを追加
        app.register_blueprint(speedtest_router)
        app.register_blueprint(speedtest_batch_router)

        app.debug = True
        app.run(host='127.0.0.1', port=5000)

if __name__ == "__main__":
    SpsApi.main()
    