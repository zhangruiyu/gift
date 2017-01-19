from datetime import datetime

from app.extensions.database import db


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), index=True)
    description = db.Column(db.Text())
    reply_to = db.Column(db.Integer, index=True)
    addTime = db.Column(db.DateTime(250), default=datetime.now())

    family_id = db.Column(db.Integer, db.ForeignKey('family.id'))
    family = db.relationship('Family', backref=db.backref('comments', lazy='dynamic'))

    @staticmethod
    def getComments(index, size=10):
        list = []
        comments_query_all = Comments.query.all()
        # print(db.session.query(Banner).all()[0].to_json())
        # for index in range(len(allMenbers)):
        # list.append(allMenbers[index].to_json())
        print(len(comments_query_all))
        return comments_query_all
