from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User
from flask_login import current_user
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    if current_user.is_authenticated:
        return render_template('dashboard.html', title='Dashboard')
    else:
        return render_template('index.html',  title='Home')

@main.route('/pricing')
def pricing():
    return render_template('pricing.html', title="Pricing")
@main.route('/help')
def help():
    return render_template('help.html', title="Help")
@main.route('/account')
def account():
    return render_template('account.html', title="Account")
@main.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us")