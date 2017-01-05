from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Boolean, Text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER
from sqlalchemy.orm import relationship

from oslo_db.sqlalchemy import models


Base = declarative_base(cls=models.ModelBase)


class Order(Base, models.SoftDeleteMixin, models.TimestampMixin):
    __tablename__ = 'orders'

    id = Column(String(64), primary_key=True)
    order_details = relationship('OrderDetail', backref='order')


class OrderDetail(Base, models.SoftDeleteMixin, models.TimestampMixin):
    __tablename__ = 'order_detail'

    id = Column(String(64), primary_key=True)
    order_id = Column(String(64), ForeignKey('orders.id'))
