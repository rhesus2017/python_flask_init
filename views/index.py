from flask import render_template, Blueprint

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    return render_template('index.jinja2')