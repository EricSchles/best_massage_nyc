import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_imageattach.entity import Image, image_attachment

engine = sql.create_engine("sqlite:///:memory", echo=True)
Base = declarative_base()

class Photos(Base):

    __tablename__ = 'photos'

    id = sql.Column(sql.Integer, primary_key=True)
    post = sql.Column(sql.String(
    photo = sql.Column(
