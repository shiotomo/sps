from datetime import datetime, timezone

from db import DBSession, Speedtest

class SpeedtestRepository:
    def __init__(self, mode):
        self.session = DBSession
        self.mode = mode

    def select_all(self):
        speedtests = self.session.query(Speedtest).all()
        return speedtests

    def select_where_server_id(self, server_id):
        speedtests = self.session.query(Speedtest).filter(Speedtest.server_id == server_id).all()
        return speedtests

    def select_where_mode(self, mode):
        speedtests = self.session.query(Speedtest).filter(Speedtest.mode == mode).all()
        return speedtests

    def select_where_server_id_and_batch(self, server_id):
        speedtests = self.session.query(Speedtest).filter(Speedtest.server_id == server_id, Speedtest.mode == 'batch').all()
        return speedtests

    def insert(self, record):
        timestamp = datetime.now()
        speedtest = Speedtest(
            download = record['download'],
            upload = record['upload'],
            ping = record['ping'],
            server_url = record['server']['url'],
            server_lat = record['server']['lat'],
            server_lon = record['server']['lon'],
            server_name = record['server']['name'],
            server_country = record['server']['country'],
            server_cc = record['server']['cc'],
            server_sponsor = record['server']['sponsor'],
            server_id = record['server']['id'],
            server_host = record['server']['host'],
            server_d = record['server']['d'],
            server_latency = record['server']['latency'],
            timestamp = timestamp,
            bytes_sent = record['bytes_sent'],
            bytes_received = record['bytes_received'],
            share = record['share'],
            client_ip = record['client']['ip'],
            client_lat = record['client']['lat'],
            client_lon = record['client']['lon'],
            client_isp = record['client']['isp'],
            client_isprating = record['client']['isprating'],
            client_rating = record['client']['rating'],
            client_ispdlavg = record['client']['ispdlavg'],
            client_loggedin = record['client']['loggedin'],
            client_country = record['client']['country'],
            mode = self.mode
        )
        self.session.add(speedtest)
        self.session.commit()
        return speedtest
