from flask import render_template, session, redirect, url_for, jsonify

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


@main.route('/message_board1', methods=['GET', 'POST'])
def message_board1():
    members = Family.getAllMembers()
    return render_template('single-page.html', members=members)
