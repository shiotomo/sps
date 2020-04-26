import pytest
import time
from datetime import datetime, timedelta
from pytz import timezone

from src.util import TimeUtils

class TestTimeUtils:
    def setup_method(self, method):
        self.datetime_format = "%Y-%m-%d %H:%M:%S"
        self.utc_datetime_format = "%Y-%m-%d %H:%M:%S %z"

    # convert_str_datetime_zone_utc_to_jstのテスト
    # UTC(GMT) -> JSTの変換がうまくできているかチェック
    def test_convert_str_datetime_zone_utc_to_jst(self):
        str_utc_datetime = "Sat, 10 Apr 2020 00:00:00 GMT"
        str_jst_datetime = TimeUtils.convert_str_datetime_timezone_utc_to_jst(str_utc_datetime)
        assert str_jst_datetime == "2020-04-10 09:00:00"

        now = datetime.now()
        str_utc_datetime = now.astimezone(timezone("GMT")).strftime(self.utc_datetime_format)
        str_jst_datetime = TimeUtils.convert_str_datetime_timezone_utc_to_jst(str_utc_datetime)
        assert str_jst_datetime == now.astimezone(timezone("Asia/Tokyo")).strftime(self.datetime_format)

    # convert_datetime_zone_utc_to_jstのテスト
    # UTC(GMT) -> JSTの変換がうまくできているかチェック
    def test_convert_datetime_zone_utc_to_jst(self):
        now = datetime.now()
        hours = timedelta(hours = 0)
        str_jst_datetime = TimeUtils.convert_datetime_timezone_utc_to_jst(now)
        # 文字列化してassertする
        assert str_jst_datetime.strftime(self.datetime_format) == (now + hours).astimezone(timezone("Asia/Tokyo")).strftime(self.datetime_format)