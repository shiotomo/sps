import json
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, Boolean, Float, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from .setting import Base
from .setting import ENGINE

class Speedtest(Base):
    __tablename__ = 'speedtest'
    id = Column('id', Integer, primary_key = True)
    download = Column('download', Float)
    upload = Column('upload', Float)
    ping = Column('ping', Float)
    server_url = Column('server_url', String)
    server_lat = Column('server_lat', String)
    server_lon = Column('server_lon', String)
    server_name = Column('server_name', String)
    server_country = Column('server_country', String)
    server_cc = Column('server_cc', String)
    server_sponsor = Column('server_sponsor', String)
    server_id = Column('server_id', String)
    server_host = Column('server_host', String)
    server_d = Column('server_d', Float)
    server_latency = Column('server_latency', Float)
    timestamp = Column('timestamp', DateTime)
    bytes_sent = Column('bytes_sent', Integer)
    bytes_received = Column('bytes_recived', Integer)
    share = Column('share', String)
    client_ip = Column('client_ip', String)
    client_lat = Column('client_lat', String)
    client_lon = Column('client_lon', String)
    client_isp = Column('client_isp', String)
    client_isprating = Column('client_isprating', String)
    client_rating = Column('client_rating', String)
    client_ispdlavg = Column('client_ispdlavg', String)
    client_loggedin = Column('client_loggedin', String)
    client_country = Column('client_country', String)
    mode = Column('mode', String)

    # speedtestモデルを辞書型に変換する
    def to_dict(self):
        speedtest_dict = {
            'id': self.id,
            'download': self.download,
            'upload': self.upload,
            'ping': self.ping,
            'server_url': self.server_url,
            'server_lat': self.server_lat,
            'server_lon': self.server_lon,
            'server_name': self.server_name,
            'server_country': self.server_country,
            'server_cc': self.server_cc,
            'server_sponsor': self.server_sponsor,
            'server_id': self.server_id,
            'server_host': self.server_host,
            'server_d': self.server_d,
            'server_latency': self.server_latency,
            'timestamp': self.timestamp,
            'bytes_sent': self.bytes_sent,
            'bytes_received': self.bytes_received,
            'share': self.share,
            'client_ip': self.client_ip,
            'client_lat': self.client_lat,
            'client_lon': self.client_lon,
            'client_isp': self.client_isp,
            'client_isprating': self.client_isprating,
            'client_rating': self.client_rating,
            'client_ispdlavg': self.client_ispdlavg,
            'client_loggedin': self.client_loggedin,
            'client_country': self.client_country,
            'mode': self.mode
        }
        return speedtest_dict
    
    def to_json(self):
        speedtest_dict = self.to_dict()
        return json.dumps(speedtest_dict, default=self.json_serial)

    # date, datetimeの変換関数
    def json_serial(self, obj):
        # 日付型の場合には、文字列に変換します
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        # 上記以外はサポート対象外.
        raise TypeError ("Type %s not serializable" % type(obj))


Base.metadata.create_all(bind=ENGINE)