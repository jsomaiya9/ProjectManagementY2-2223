from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    if current_user.is_authenticated:
      return render_template('dashboard.html',  title='dashboard')
    else:
      return render_template('index.html',  title='Home')

@main.route('/pricing')
def pricing():
      return render_template('pricing.html',  title='pricing')
      

@main.route('/aboutus')
def aboutus():
      return render_template('aboutus.html',  title='aboutus')

@main.route('/products')
def products():
      return render_template('products.html',  title='products')
