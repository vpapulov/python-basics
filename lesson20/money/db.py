from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class RefAccount(Base):
    __tablename__ = 'ref_accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class DocIncome(Base):
    __tablename__ = 'doc_income'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    account_id = Column(Integer, ForeignKey(RefAccount.id), nullable=False)
    account = relationship("RefAccount", back_populates = "docs_income")
    sum = Column(Float, nullable=False)
    comment = Column(String, nullable=False)

RefAccount.docs_income = relationship("DocIncome", order_by = DocIncome.id, back_populates = "account")


engine = create_engine('sqlite:///money.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.create_all(engine)
