from pytz import timezone
from dateutil import parser
from datetime import timedelta

class TimeUtils:
    @staticmethod
    def convert_str_datetime_timezone_utc_to_jst(str_utc_datetime):
        jst_datetime = parser.parse(str_utc_datetime).astimezone(timezone('Asia/Tokyo'))
        str_jst_datetime = jst_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return str_jst_datetime

    def convert_datetime_timezone_utc_to_jst(utc_datetime):
        # delta = timedelta(hours=9)
        delta = timedelta(hours=0)
        jst_datetime = utc_datetime + delta
        return jst_datetime.astimezone(timezone('Asia/Tokyo'))

    @staticmethod
    def to_datetime(str_datetime):
        pass

    @staticmethod
    def to_string(datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S %z")
