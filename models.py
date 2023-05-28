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

# Models for database
# Role model (doesn't do anything for now)
class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    description = Column(String)

class User(Base, UserMixin):
    __tablename__ = 'user'
    username = Column(String(20), primary_key=True)
    email = Column(String(20), unique=True)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, nullable=False)
    fs_uniquifier = Column(String(64), nullable=False)
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))

class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    username = Column('username', Integer(), ForeignKey('user.username'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))

# Model for all the questions over at /questions
class Questions(Base):
    __tablename__ = 'questions'
    uname = Column(Integer, primary_key=True)
    q0 = Column(Integer)
    q1 = Column(Integer)
    q2 = Column(Integer)
    q3 = Column(Integer)
    q4 = Column(Integer)
    q5 = Column(Integer)
    q6 = Column(Integer)
    q7 = Column(Integer)
    q8 = Column(Integer)
    q9 = Column(Integer)
