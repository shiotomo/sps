from flask import Blueprint, jsonify
from flask_cors import CORS

from service import SpeedtestService

speedtest_router = Blueprint('speedtest_router', __name__, url_prefix='/api/v1/speedtests')
CORS(speedtest_router)

speedtest_service = SpeedtestService('api')

# 過去のspeedtestの実行結果を取得する
@speedtest_router.route('/')
def index():
    speedtest_list = speedtest_service.get_speedtest_all()
    return jsonify(speedtest_list)

# 指定したサーバIDの実行結果を取得する
@speedtest_router.route('/<server_id>')
def show(server_id):
    speedtest_list = speedtest_service.get_speedtest_where_server_id(server_id)
    return jsonify(speedtest_list)