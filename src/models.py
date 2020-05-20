import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    password = "somehashedcode"
    followers = relationship("followers")
    posts = relationship("post")
    comments = relationship("comments")

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    comments_id = Column(String(100), ForeignKey("comments.id"))

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
   

class Followers(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    
class Following(Base):
    __tablename__ = "following"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id")) 


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')