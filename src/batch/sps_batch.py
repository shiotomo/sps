import time
import sys

from service import SpeedtestService

class SpsBatch:
    INTERVAL_TIME = 300

    def __init__(self):
        self.speedtest_service = SpeedtestService('batch')

    # CRON_MINUTES_INTERVALの間隔でspeedtestを実行し結果を保存する
    def sps_service_schedule(self):
        print("run sps_service_schedule !!")
        try:
            while True:
                print("run speedtest")
                self.speedtest_service.record_speedtest_all_server()
                time.sleep(self.INTERVAL_TIME)
        except KeyboardInterrupt:
            print("stop speedtest!!")
            sys.exit()
