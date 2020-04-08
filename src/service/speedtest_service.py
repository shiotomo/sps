import subprocess
import json
import random

from repository import SpeedtestRepository
from config import JAPAN_SERVER_LIST

class SpeedtestService:
    def __init__(self, mode):
        self.speedtest_repository = SpeedtestRepository(mode)
        self.mode = mode 

    def get_speedtest_all(self):
        speedtests = self.speedtest_repository.select_all()
        return speedtests

    # speedtestを実行し、結果をDBに格納する
    def record_speedtest_result(self):
        speedtest_result = self.run_speedtest()
        speedtest = self.speedtest_repository.insert(speedtest_result)
        return speedtest

    # speedtestを実行した結果を取得する
    def run_speedtest(self):
        japan_server = self.get_random_speedtest_server()
        process = subprocess.run(['speedtest', '--server', japan_server['id'], '--json'], capture_output=True)
        return json.loads(process.stdout)

    # JAPAN_SERVER_LISTからランダムに1つサーバを取得する
    def get_random_speedtest_server(self):
        japan_server = random.choice(JAPAN_SERVER_LIST)
        print(japan_server['id'])
        return japan_server