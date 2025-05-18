import os
from sqlalchemy import create_engine, Column, String, Integer, BigInteger, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

POSTGRES_URL = os.getenv('POSTGRES_URL')
engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    hash = Column(String, primary_key=True, index=True)
    chain = Column(String, index=True)
    sender = Column(String)
    receiver = Column(String)
    fee = Column(BigInteger)
    token_transfers = Column(JSON)


def insert_transaction(session, tx):
    db_tx = Transaction(**tx)
    session.add(db_tx)
    session.commit() 