from flask import Blueprint, jsonify
from flask_cors import CORS

from service import SpeedtestService

speedtest_batch_router = Blueprint('speedtest_batch_router', __name__, url_prefix='/api/v1/speedtests/batch')
CORS(speedtest_batch_router)

speedtest_service = SpeedtestService('api')

# 全サーバの実行結果を取得する
@speedtest_batch_router.route('/')
def index():
    speedtest_list = speedtest_service.get_speedtest_where_mode('batch')
    return jsonify(speedtest_list)

# 指定したサーバIDの実行結果を取得する
@speedtest_batch_router.route('/<server_id>')
def show(server_id):
    speedtest_list = speedtest_service.get_speedtest_where_server_id_and_batch(server_id)
    return jsonify(speedtest_list)