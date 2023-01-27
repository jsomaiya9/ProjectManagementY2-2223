from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User, Profile
from app.main.forms import ProfileForm, UserForm, EditForm, ExpForm
from flask_login import current_user
from app import db
from datetime import datetime


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    return render_template('index.html',  title='Home')


@main.route('/aboutus')
def aboutus():
    return render_template('aboutus.html',  title='About Us')


@main.route('/pricing')
def pricing():
    return render_template('pricing.html',  title='Pricing')

@main.route('/help')
def help():
    return render_template('help.html',  title='Help')

@main.route('/account/<username>', methods=['GET', 'POST'])
def account(username):
    if current_user.is_authenticated:
        
        user = User.query.filter_by(username = username).first()

        profile = Profile.query.filter_by(user_id=user.id).first()

        return render_template('account.html', title="Account", profile=profile)
    else:
        return(redirect(url_for('auth.login')))

@main.route('/contact')
def contact():
    return render_template('contact.html',  title='Contact')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',  title='Dashboard')

@main.route('/products')
def products():
    return render_template('products.html',  title='Products')


@main.route('/certify', methods=["GET", "POST"])
def certify():
    if current_user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm()
            profile = Profile.query.filter_by(user_id=current_user.id).first()

            profile.member_type = form.membertype.data
            db.session.commit()
            
            return(redirect(url_for('main.account', username=current_user.username)))
           
        else:
            form = ProfileForm()
            profile = Profile.query.filter_by(user_id=current_user.id).first()
            
            return render_template('certify.html', title="Certification", form=form)
    else:
        return(redirect(url_for('auth.login')))

@main.route('/admin/users')
def admin_users():
    if current_user.is_authenticated:
            
        users = User.query.all()

        return render_template('users.html', users = users)

    return redirect(url_for('main.index'))

@main.route('/admin/users/<id>', methods=['GET', 'POST'])
def user_edit(id):
    form = EditForm()
    
    user = User.query.filter_by(id=id).first()
    profile = Profile.query.filter_by(user_id=id).first()

    if request.method == 'POST':
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.rating = form.rating.data


        if profile: 
            profile.member_type = form.member_type.data
            profile.is_verified = True
        else :
            profile = Profile(
                member_type=form.membertype.data,
                is_verified = True,
                user_id = id
            )
            db.session.add(profile)
        db.session.commit()
        return redirect(url_for('main.admin_users'))
    else :
        form.first_name.data = user.first_name
        form.last_name.data = user.last_name
        user.rating = form.rating.data

        if profile: 
            form.member_type.data = profile.member_type
        
        return render_template('edit.html', form=form)

@main.route('/users/<id>', methods=['GET', 'POST'])
def exp_edit(id):
    form = ExpForm()
    user = User.query.filter_by(id=id).first()
    if request.method == 'POST':
        user.exp_qual = form.exp_qual.data
        db.session.commit()
        return redirect(url_for('main.account', username=current_user.username))
    else:
        form.exp_qual.data = user.exp_qual
        return render_template('expqual.html', form=form)