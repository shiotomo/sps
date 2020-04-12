from flask import Blueprint, jsonify
from flask_cors import CORS

from config import JAPAN_SERVER_LIST

speedtest_server_router = Blueprint('speedtest_server_router', __name__, url_prefix='/api/v1/speedtest_servers')
CORS(speedtest_server_router)

# 指定したサーバIDの実行結果を取得する
@speedtest_server_router.route('/')
def index():
    return jsonify(JAPAN_SERVER_LIST)

@speedtest_server_router.route('/<server_id>')
def show(server_id):
    server = [x for x in JAPAN_SERVER_LIST if x['id'] == server_id]
    print(server)
    return jsonify(server[0])