import pytest
import time
from datetime import datetime
from pytz import timezone

from src.util import TimeUtils

class TestTimeUtils:
    def setup_method(self, method):
        self.datetime_format = "%Y-%m-%d %H:%M:%S"
        self.utc_datetime_format = "%Y-%m-%d %H:%M:%S %z"

    # convert_time_zone_utc_to_jstのテスト
    # UTC(GMT) -> JSTの変換がうまくできているかチェック
    def test_convert_time_zone_utc_to_jst(self):
        str_utc_datetime = "Sat, 10 Apr 2020 00:00:00 GMT"
        str_jst_datetime = TimeUtils.convert_timezone_utc_to_jst(str_utc_datetime)
        assert str_jst_datetime == "2020-04-10 09:00:00"

        now = datetime.now()
        str_utc_datetime = now.astimezone(timezone("GMT")).strftime(self.utc_datetime_format)
        str_jst_datetime = TimeUtils.convert_timezone_utc_to_jst(str_utc_datetime)
        assert str_jst_datetime == now.astimezone(timezone("Asia/Tokyo")).strftime(self.datetime_format)