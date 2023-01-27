from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
from app.models import User, News
from datetime import datetime
from flask_login import current_user
from app.main.forms import NewsForm
from app import db
import os

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    news = News.query.order_by(News.date.desc()).limit(3).all()
    return render_template('index.html',  title='Home', news = news)

@main.route('/aboutus')
def aboutus():
    return render_template('aboutus.html',  title='About Us')

@main.route('/account')
def account():
    return render_template('account.html',  title=' Account')

@main.route('/contact')
def contact():
    return render_template('contact.html',  title='Contact')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',  title='Dashboard')

@main.route('/help')
def help():
    return render_template('help.html',  title='Help')

@main.route('/prices')
def prices():
    return render_template('prices.html',  title='Prices')

@main.route('/pricing')
def pricing():
    return render_template('pricing.html',  title='Pricing')

@main.route('/products')
def products():
    return render_template('products.html',  title='Products')


@main.route('/newsannoucement')
def newsannoucement():
    search = request.args.get('s', default='')
    if search != '':
        news = News.query.filter_by(date=search)
    else:
        news = News.query.order_by(News.date.desc()).all()
    
    return render_template('newsannoucement.html', title="Edit Cours", news = news)  

       
        
@main.route('/news/<id>', methods=['GET','POST'])
def news(id):
    if current_user.is_authenticated:

        if request.method == 'POST':
            form = NewsForm()

            if id == "-1" :

                news = News(
                    title=form.title.data,
                    caption=form.caption.data,
                    description=form.description.data,
                    date=datetime.utcnow()
                )
                db.session.add(news)
                db.session.commit()
                flash('You Have Successfully Added a News Story','Success')
                return(redirect(url_for('main.newsannoucement')))
            else:
                news = News.query.get_or_404(id)

                
                news.title = form.title.data
                news.caption = form.caption.data
                news.description = form.description.data
                news.date = datetime.utcnow()

                db.session.commit()

                return(redirect(url_for('main.newsannoucement')))
        else:
            if id == "-1":
                form = NewsForm() 
                return render_template('news.html', title="Add News", form=form)
            else :
                news = News.query.get_or_404(id)
                form = NewsForm(obj=news)
                return render_template('news.html', title="Edit News", form=form)

    else:
        return redirect(url_for('auth.login'))


@main.route('/delete/<int:id>')
def delete(id) :
    news_to_delete = News.query.get_or_404(id)
    
    try :
        db.session.delete(news_to_delete)
        db.session.commit()

        flash("Delete Successful")
        return redirect(url_for('main.newsannoucement'))
    except :
        flash("Delete Unsuccessful")
        return redirect(url_for('main.newsannoucement'))
