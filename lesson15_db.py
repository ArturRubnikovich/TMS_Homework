from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

dsn = "sqlite:///lesson15.db"
engine = create_engine(dsn, echo=True)
session = sessionmaker(bind=engine, autoflush=False)


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


def drop_tables():
    Base.metadata.drop_all(engine)


drop_tables()
create_tables()


def add_users(connection):
    user1 = User(username="Artur", password="w12345", email="arturred@gmail.com")
    user2 = User(username="Alex", password="qwe123456789", email="alex1996@gmail.com")
    user3 = User(username="Max", password="qwerty000", email="maxon@gmail.com")
    user4 = User(username="Kate", password="123456789", email="kate11121991@yandex.ru")
    connection.add(user1)
    connection.add(user2)
    connection.add(user3)
    connection.add(user4)
    connection.commit()


def add_sellers(connection):
    seller1 = Seller(company="Prostore", phone="+375294561268")
    seller2 = Seller(company="Amifruit", phone="+375336541269")
    seller3 = Seller(company="Delovoy", phone="+375442587932")
    connection.add(seller1)
    connection.add(seller2)
    connection.add(seller3)
    connection.commit()


def add_products(connection):
    product1 = Product(name="wine", cost="25", count="2000", seller_id="1")
    product2 = Product(name="tomatoes", cost="10", count="5000", seller_id="2")
    product3 = Product(name="A4 paper", cost="40", count="250", seller_id="3")
    connection.add(product1)
    connection.add(product2)
    connection.add(product3)
    connection.commit()


def create_orders(connection):
    order1 = Order(user_id="3", product_id="2", count="5")
    order2 = Order(user_id="2", product_id="1", count="125")
    order3 = Order(user_id="1", product_id="3", count="48")
    connection.add(order1)
    connection.add(order2)
    connection.add(order3)
    connection.commit()


with session() as conn:
    add_users(conn)
    add_sellers(conn)
    add_products(conn)
    create_orders(conn)
