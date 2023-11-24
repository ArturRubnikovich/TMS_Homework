from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase

dsn = "sqlite:///lesson15.db"
engine = create_engine(dsn)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(50), unique=True, nullable=False)


class Seller(Base):
    __tablename__ = "seller"
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64), nullable=False)
    phone = Column(String(20), nullable=False)


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    cost = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    seller_id = Column(Integer, ForeignKey("seller.id"), nullable=False)


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    count = Column(Integer, nullable=False)


def create_tables():
    Base.metadata.create_all(engine)


create_tables()
