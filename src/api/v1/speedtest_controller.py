from flask import Blueprint, jsonify

from service import SpeedtestService

speedtest_router = Blueprint('speedtest_router', __name__, url_prefix='/api/v1/speedtests')

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

# speedtestを実行する
@speedtest_router.route('/create')
def create():
    speedtest_result = speedtest_service.record_speedtest_result()
    return jsonify({
        'status': 'OK',
        'data': speedtest_result.to_dict()
    })