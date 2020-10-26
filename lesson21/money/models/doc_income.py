from .database import db
from .ref_account import RefAccount
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship


class DocIncome(db.Model):
    __tablename__ = 'doc_income'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    account_id = Column(Integer, ForeignKey(RefAccount.id), nullable=False)
    account = relationship("RefAccount", back_populates="docs_income")
    sum = Column(Float, nullable=False)
    comment = Column(String, nullable=False, default="")


RefAccount.docs_income = relationship("DocIncome", order_by=DocIncome.id, back_populates="account")
