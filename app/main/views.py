from flask import render_template, request, current_app
from ..models import User
from . import main
from ..models import Article, Category


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(
        Article.create_timestramp.desc()).paginate(
            page,
            per_page=current_app.config['FLASK_POST_PER_PAGE'],
            error_out=False)
    one_page_articles = pagination.items
    articles = Article.query.order_by(Article.create_timestramp.desc())
    categories = Category.query
    return render_template('index.html', articles=articles,
                           categories=categories,
                           one_page_articles=one_page_articles,
                           pagination=pagination)


@main.route('/about_me')
def about_me():
    user = User.query.filter_by(id=1).first()
    return render_template('about_me.html', user=user)


@main.route('/aritcle/<int:id>')
def article(id):
    article = Article.query.get_or_404(id)
    return render_template('article.html', article=article)


@main.route('/archive')
def archive():
    articles = Article.query.order_by(Article.create_timestramp.desc())
    categories = Category.query
    return render_template('archive.html', articles=articles,
                           categories=categories)


@main.route('/category/<string:name>')
def category(name):
    articles = Article.query.order_by(Article.create_timestramp.desc())
    categories = Category.query
    category = Category.query.filter_by(name=name).first_or_404()
    return render_template('category.html', category=category,
                           articles=articles, categories=categories)
