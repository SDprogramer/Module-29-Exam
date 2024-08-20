from flask import Blueprint

my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/hello')
def hello():
    return "Hello from the blueprint!"
