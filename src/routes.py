from flask import Blueprint, render_template, jsonify
from src.helpers.imgLinks import colorLinks

rotas_bp = Blueprint('rotas', __name__, template_folder='../static/templates')


@rotas_bp.route('/')
def index():
    return render_template('start.html')

@rotas_bp.route('/signin')
def signin():
    return render_template('sign-in.html')

@rotas_bp.route('/signup')
def signup():
    return render_template('sign-up.html')

@rotas_bp.route('/char')
def char():
    return render_template('char.html')

@rotas_bp.route('/img', methods=['GET'])
def img():
    return jsonify(colorLinks)