from flask import Blueprint

pages = Blueprint('test', __name__)


@pages.route('/')
def home():
    return '<h1>Hi! This is my first deployment test</h1>'