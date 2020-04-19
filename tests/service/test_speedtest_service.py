import pytest

from src.service import SpeedtestService
from src.config import JAPAN_SERVER_LIST

class TestSpeedtestService:
    def setup_method(self, method):
        self.speedtest_service = SpeedtestService("test")
        self.server = JAPAN_SERVER_LIST[0]
        self.error_server_id = 00000

    # run_speedtestの返り値の型を判定する
    def test_run_speedtest_check_type(self):
        result = self.speedtest_service.run_speedtest(self.server['id'])
        assert type(result) is dict

    # run_speedtestの返り値の型を判定する
    # 存在しないidを入力するため{}が帰ってくる
    def test_run_speedtest_exception_check_type(self):
        result = self.speedtest_service.run_speedtest(self.error_server_id)
        assert type(result) is dict

    # run_speedtestの返り値の型を判定する
    # 存在しないidを入力するため{}が帰ってくる
    def test_run_speedtest_check_value(self):
        result = self.speedtest_service.run_speedtest(self.error_server_id)
        assert result == {}