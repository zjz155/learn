#! /usr/bin python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# https://mathiasbynens.be/notes/mysql-utf8mb4  运行时出现warning的解决方法
# 创建数据库表基类
Base = declarative_base()

# 定义数据库ORM关系对象
class Account(Base):
	__tablename__ = "account"

	id = Column(Integer, primary_key = True)
	name = Column(String(22))
	age = Column(Integer)
	height = Column(Float)
	number = Column(String(35))
        sex = Column(String(1))

def add_method():
    pass

# 初始化数据库连接
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/userdb")

# 连接数据库
DBSession = sessionmaker(bind = engine)

# 创建session对象
session = DBSession()
# 创建新account对象
new_account = Account(id=5, name="tom",age=29, height=170, number="20180101")

session.add(new_account)
# 提交保存到数据库
session.commit()
# 关闭session
session.close()

