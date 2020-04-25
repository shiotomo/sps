from flask import Blueprint, render_template

sps_router = Blueprint('sps_router', __name__, url_prefix='/')

@sps_router.route('/', defaults={'path': ''})
@sps_router.route('/<path:path>')
def index(path):
    return render_template('index.html')