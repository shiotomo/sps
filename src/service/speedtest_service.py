import subprocess
import json

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
        self.speedtest_repository.insert(speedtest_result)
        print("-----------------------------------------")
        print(speedtest_result)
        print("-----------------------------------------")
        return speedtest_result

    # speedtestを実行した結果を取得する
    def run_speedtest(self):
        process = subprocess.run(['speedtest', '--server', '24333', '--json'], capture_output=True)
        return json.loads(process.stdout)

    def get_random_speedtest_server(self):
        pass