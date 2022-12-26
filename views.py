from flask import Flask, Blueprint, render_template, request
import utils

# creating blueprint for main with all posts, setting template folder
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

# creating blueprint for post view, setting template folder
post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')

# creating blueprint for search post by keywrod view, setting template folder
post_search_blueprint = Blueprint('post_search_blueprint', __name__, template_folder='templates')

# creating blueprint for post view, setting template folder
user_search_blueprint = Blueprint('user_search_blueprint', __name__, template_folder='templates')

# calling blueprint for main page in required template
@main_blueprint.route('/')
def main_page():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


# calling blueprint for post view in required template
@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    post = utils.get_post_by_pk(postid)
    comments = utils.get_comments_by_post_id(postid)
    comments_quantity = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_quantity=comments_quantity)


# calling blueprint for search by keyword results in required template
@post_search_blueprint.route('/search')
def search_post_by_content():
    string = request.args.get('s')
    posts_with_string = utils.search_for_posts(string)
    posts_with_string_to_show = posts_with_string[0:10]
    posts_quantity = len(posts_with_string)
    return render_template('search.html', posts_quantity=posts_quantity, posts_with_string_to_show=posts_with_string_to_show)


# calling blueprint for search by username results in required template
@user_search_blueprint.route('/users/<username>')
def search_user_posts_by_username(username):
    user_posts = utils.get_posts_by_user(username)
    posts_quantity = len(user_posts)
    return render_template('user-feed.html', user_posts=user_posts, posts_quantity=posts_quantity)


