from flask import Flask, jsonify, Blueprint, render_template
import flask
import utils
from views import main_blueprint, post_blueprint, post_search_blueprint, user_search_blueprint

# starting app
app = Flask(__name__)
# allow сyrillic symbols, defining configuration parameter for encoding
app.config['JSON_AS_ASCII'] = False

# registering blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(post_search_blueprint)
app.register_blueprint(user_search_blueprint)


# generating errors
@app.errorhandler(404)
def page_not_found(error):
    return "Page not found", 404


@app.errorhandler(500)
def page_not_found(error):
    return "Internal server error", 500


# generating API endpoints

# api/posts endpoint
@app.route('/api/posts/')
def all_posts():
    data = utils.get_json('data/posts.json')
    return jsonify(data)


# api/posts/post-id endpoint

@app.route('/api/posts/<int:pk>')
def post_by_pk(pk):
    post = utils.get_post_by_pk(pk)
    return jsonify(post)


# define condition for app launch
if __name__ == '__main__':
    app.run()
