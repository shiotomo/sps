from .time_utils import TimeUtils

class ListUtils:
    @staticmethod
    def get_speedtest_list(speedtests):
        speedtest_list = []
        for speedtest in speedtests:
            timestamp = TimeUtils.convert_datetime_timezone_utc_to_jst(speedtest.timestamp)
            speedtest.timestamp = TimeUtils.to_string(timestamp)
            speedtest_list.append(speedtest.to_dict())
        return speedtest_list