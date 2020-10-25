from .database import db
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime

class RefAccount(db.Model):
    __tablename__ = 'ref_accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
