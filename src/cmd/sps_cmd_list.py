from service import SpeedtestService

class SpsCmdList():
    def __init__(self, cmd):
        self.cmd = cmd
        self.speedtest_service = SpeedtestService('cmd')

    def run(self):
        if self.cmd == 'speedtest':
            self.run_speed_test()
        elif self.cmd == 'result':
            self.get_result()
        else:
            print(self.cmd)

    def run_speed_test(self):
        result = self.speedtest_service.record_speedtest_result()
        print(result)

    def get_result(self):
        speedtest_list = self.speedtest_service.get_speedtest_all()
        print(speedtest_list)