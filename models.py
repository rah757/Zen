from database import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    UnicodeText,
    String,
    Time,
    DateTime,
    Float,
    Interval,
    Boolean,
)

class User(Base, UserMixin):
    __tablename__ = 'user'
    _id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    active = Column(Boolean, nullable=False)
    password = Column(String(100), nullable=False)
    fs_uniquifier = Column(String(64), nullable=False)
    entries = relationship('Entry', backref='user', lazy=True)
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))

class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    description = Column(String)

class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    username = Column('username', Integer(), ForeignKey('user.username'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))

class Entry(Base):
    __tablename__ = 'entry'
    entry_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user._id'), nullable=False)
    health = Column(Integer)
    sleep = Column(Integer)

    def __init__(self, user_id, health):
        self.user_id = user_id
        self.health = health
