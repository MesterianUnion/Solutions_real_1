from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BotAnswer(Base):
    __tablename__ = 'bot_answers'

    id = Column(Integer, primary_key=True)
    answer = Column(String)
    command_used = Column(String)
    user = Column(String)
    timestamp = Column(DateTime)

class BotSession(Base):
    __tablename__ = 'bot_sessions'

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
