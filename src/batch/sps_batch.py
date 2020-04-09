import schedule
import time

from service import SpeedtestService

class SpsBatch:
    CRON_MINUTES_INTERVAL = 5

    def __init__(self):
        self.speedtest_service = SpeedtestService('batch')

    # CRON_MINUTES_INTERVALの間隔でspeedtestを実行し結果を保存する
    def sps_service_schedule(self):
        print("run sps_service_schedule !!")
        schedule.every(self.CRON_MINUTES_INTERVAL).minutes.do(self.speedtest_service.record_speedtest_all_server)
        while True:
            schedule.run_pending()
            time.sleep(1)