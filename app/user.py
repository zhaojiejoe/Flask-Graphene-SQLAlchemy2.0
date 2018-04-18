# coding=utf-8

from flask import Blueprint
bp = Blueprint('user', __name__, url_prefix='/')


@bp.route('/')
def hello_world():
    return {"Hello": "World!"}


@bp.route('common/<list:page_names>')
def commonsplit(page_names):
    return {'ret': page_names}
