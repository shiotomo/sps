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

Base.metadata.create_all(bind=ENGINE)