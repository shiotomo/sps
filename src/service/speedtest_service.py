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
        speedtest_list = []
        for speedtest in speedtests:
            speedtest_list.append(speedtest.to_dict())
        return speedtest_list

    # speedtestを実行し、結果をDBに格納する
    def record_speedtest_result(self):
        print("run speedtest!!")
        server = self.get_random_speedtest_server()
        speedtest_result = self.run_speedtest(server)
        speedtest = self.speedtest_repository.insert(speedtest_result)
        print(speedtest.to_dict())
        return speedtest

    # 全てのserverでspeedtestを実行し、結果をDBに格納する
    def record_speedtest_all_server(self):
        result_list = []
        for server in JAPAN_SERVER_LIST:
            speedtest_result = self.run_speedtest(server)
            speedtest = self.speedtest_repository.insert(speedtest_result)
            print(speedtest.to_dict())
            result_list.append(speedtest.to_dict())
        return result_list

    # speedtestを実行した結果を取得する
    def run_speedtest(self, server):
        process = subprocess.run(['speedtest', '--server', server['id'], '--json'], capture_output=True)
        return json.loads(process.stdout)

    # JAPAN_SERVER_LISTからランダムに1つサーバを取得する
    def get_random_speedtest_server(self):
        japan_server = random.choice(JAPAN_SERVER_LIST)
        print(japan_server['id'])
        return japan_server