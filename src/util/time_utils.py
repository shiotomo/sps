from pytz import timezone
from dateutil import parser

class TimeUtils:
    @staticmethod
    def convert_timezone_utc_to_jst(str_utc_datetime):
        jst_datetime = parser.parse(str_utc_datetime).astimezone(timezone('Asia/Tokyo'))
        str_jst_datetime = jst_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return str_jst_datetime
    
    @staticmethod
    def to_datetime(str_datetime):
        pass