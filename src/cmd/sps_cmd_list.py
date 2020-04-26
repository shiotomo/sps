import json

from service import SpeedtestService
from config import JAPAN_SERVER_LIST
from db import Migration

class SpsCmdList():
    def __init__(self, cmd):
        self.cmd = cmd
        self.speedtest_service = SpeedtestService('cmd')

    def run(self):
        if self.cmd == 'speedtest':
            self.run_speed_test()
        elif self.cmd == 'result':
            self.get_result()
        elif self.cmd == 'all':
            self.run_speed_test_all_server()
        elif self.cmd == 'migrate':
            Migration()
        else:
            print(self.cmd)

    def run_speed_test(self):
        result = self.speedtest_service.record_speedtest_result()
        print(result)

    def get_result(self):
        speedtest_list = self.speedtest_service.get_speedtest_all()
        print(speedtest_list)

    def run_speed_test_all_server(self):
        for server in JAPAN_SERVER_LIST:
            try:
                result = self.speedtest_service.run_speedtest(server)
                print('ok: ' + str(server))
            except json.decoder.JSONDecodeError:
                print('error: ' + str(server['id']))