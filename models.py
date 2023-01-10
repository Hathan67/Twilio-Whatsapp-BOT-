from sqlalchemy import Column,Integer, String, ForeignKey, Float, MetaData, func, Table
from sqlalchemy.types import Date
from database import Base, engine, session
from sqlalchemy.orm import relationship, column_property
from sqlalchemy_utils import aggregated
import math



metadata = MetaData
#creating a model

class Odetails(Base):
    __tablename__ = "orderDetails"

    id = Column(Integer,primary_key=True)
    order_id = Column("order_id", String(55))
    product_id = Column("product_id",Integer, ForeignKey("Products.product_id"))
    quantity = Column("quantity",Integer)
    amount = Column("amount",Integer)
    orderStatus = Column("orderStatus", String(55))

    products = relationship('Product', back_populates='orders', lazy="joined")

    def __repr__(self):
        return "<Odetails(order_id='%s', quantity='%s', amount='%s', orderStatus='%s')>"%(
            self.order_id,
            self.quantity,
            self.amount,
            self.orderStatus,
        )


class Product(Base):
    __tablename__ = "Products"

    # id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column("product_id",Integer, primary_key=True)
    product_name = Column("product_name",String(255))
    rate = Column("rate", Float)

    orders = relationship('Odetails', back_populates='products', lazy="joined")


    def __repr__(self):
        return "<Product(product_id='%s', product_name='%s', rate='%s')>"%(
            self.product_id,
            self.product_name,
            self.rate,
        )
Base.metadata.create_all(engine)
