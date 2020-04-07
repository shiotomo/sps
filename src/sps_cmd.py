from service import SpeedtestService

class SpsCmd:
    @staticmethod
    def main():
        speedtestService = SpeedtestService('cmd')
        result = speedtestService.record_speedtest_result()
        print(result)
        speedtests = speedtestService.get_speedtest_all()
        for speedtest in speedtests:
            print(vars(speedtest))

if __name__ == "__main__":
    SpsCmd.main()