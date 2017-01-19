from pytz import lazy
from sqlalchemy.orm import backref

from app.extensions.database import db


class Family(db.Model):
    __tablename__ = 'family'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    nickname = db.Column(db.String(50), index=True)
    description = db.Column(db.String(250))
    relation = db.Column(db.String(250))

    @staticmethod
    def getAllMembers():
        list = []
        # print(db.session.query(Banner).all()[0].to_json())
        allMenbers = Family.query.all()
        # for index in range(len(allMenbers)):
        # list.append(allMenbers[index].to_json())
        print(len(allMenbers))
        return allMenbers
