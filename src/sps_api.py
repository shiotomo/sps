from flask import Flask
from flask_cors import CORS

from controller import sps_router
from controller import speedtest_router
from controller import speedtest_batch_router
from controller import speedtest_server_router

class SpsApi():
    @staticmethod
    def main():
        app = Flask(__name__, static_folder="../build/static", template_folder="../build")
        CORS(app)

        # ここにcontrollerを追加
        app.register_blueprint(sps_router)
        app.register_blueprint(speedtest_router)
        app.register_blueprint(speedtest_batch_router)
        app.register_blueprint(speedtest_server_router)

        app.debug = True
        app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    SpsApi.main()
    