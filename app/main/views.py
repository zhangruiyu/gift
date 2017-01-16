from flask import render_template, session, redirect, url_for, jsonify

from app import Family
from app.extensions.database import db
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', name='123')


@main.route('/generic', methods=['GET', 'POST'])
def generic():
    # family = Family(name='张瑞宇', description='爱爱的到底是啥', relation='铲屎少年')
    # db.session.add(family)
    # db.session.commit()
    # Family.getAllMembers()
    return render_template('generic.html', name='123')


@main.route('/elements', methods=['GET', 'POST'])
def elements():
    members = Family.getAllMembers()
    return render_template('elements.html', members=members)
