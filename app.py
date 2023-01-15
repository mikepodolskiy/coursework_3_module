# import required libraries, functions, blueprints
from flask import Flask, jsonify
import utils
from views import main_blueprint, post_blueprint, post_search_blueprint, user_search_blueprint
import logging

# create a custom logger
logger = logging.getLogger('api_logger')

# create custom logger handler, set logger level
logger_handler = logging.FileHandler('log/api.log', encoding='utf-8')
logger.setLevel(logging.INFO)

# create formatters according to task and add it to the handler
logger_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
logger_handler.setFormatter(logger_formatter)

# add handler to the logger
logger.addHandler(logger_handler)

# starting app
app = Flask(__name__)
# allow сyrillic symbols, setting configuration parameter for encoding
app.config['JSON_AS_ASCII'] = False

# registering blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(post_search_blueprint)
app.register_blueprint(user_search_blueprint)


# create errors generating
@app.errorhandler(404)
def page_not_found(error):
    return "404 - Page not found", 404


@app.errorhandler(500)
def page_not_found(error):
    return "500 - Internal server error", 500


# generating API endpoints

# api/posts endpoint
@app.route('/api/posts/')
def all_posts():
    logger.info('Request "/api/posts/"')
    data = utils.get_json('data/posts.json')
    return jsonify(data)


# api/posts/pk endpoint

@app.route('/api/posts/<int:pk>')
def post_by_pk(pk):
    logger.info(f'Request "/api/posts/{pk}"')
    post = utils.get_post_by_pk(pk)
    return jsonify(post)


# setting condition for app launch
if __name__ == '__main__':
    app.run()
