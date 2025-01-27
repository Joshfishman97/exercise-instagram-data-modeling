import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20),nullable=False,index=True)
    firstname = Column(String(20),nullable=False)
    lastname = Column(String(20),nullable=False)
    email = Column(String(250), nullable=False,unique=True)
   

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, ForeignKey('user.id') ,primary_key=True)
    user_from = relationship(User)
    user_to_id  = Column(Integer, ForeignKey('user.id') ,primary_key=True)
    user_to = relationship(User)
    
    
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Likes(Base):
    __tablename__ = 'likes'
    user_id  = Column(Integer, ForeignKey('user.id'),primary_key=True)
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'),primary_key=True)
    post = relationship(Post)



class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    author = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'),nullable=False)
    post = relationship(Post)
    

class MyEnum(enum.Enum):
    video = 1
    photo = 2
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MyEnum))
    url  = Column(String(250),nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e