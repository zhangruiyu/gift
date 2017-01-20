from flask import render_template, session, redirect, url_for, jsonify
from flask import request

from app import Comments
from app import Family
from app.extensions.database import db
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', name='123')


@main.route('/plan', methods=['GET', 'POST'])
def plan():
    # family = Family(name='张瑞宇', description='爱爱的到底是啥', relation='铲屎少年')
    # db.session.add(family)
    # db.session.commit()
    # Family.getAllMembers()
    return render_template('plan.html', name='123')


@main.route('/about', methods=['GET', 'POST'])
def about():
    members = Family.getAllMembers()
    return render_template('about.html', members=members)


@main.route('/message_board', methods=['GET', 'POST'])
def message_board():
    comments = Comments.getComments(0)
    return render_template('comments.html', comments=comments)


@main.route('/addFamily', methods=['GET', 'POST'])
def addFamily():
    try:
        name = request.form['name']
        nick_name = request.form['nick_name']
        description = request.form['description']
        relation = request.form['relation']
        family = Family(name=name, nickname=nick_name, description=description, relation=relation)
        db.session.add(family)
        db.session.commit()
    except:
        return jsonify({'code': 100})
    return jsonify({'code': 200})


@main.route('/comment', methods=['GET', 'POST'])
def addcomment():
    try:
        name = request.form['name']
        description = request.form['description']
        family = Comments(name=name, description=description)
        db.session.add(family)
        db.session.commit()
    except:
        return jsonify({'code': 100})
    return jsonify({'code': 200})
