from flask import Flask, Blueprint, render_template

from views import main_blueprint, post_blueprint, post_search_blueprint, user_search_blueprint

# starting app
app = Flask(__name__)

# registering blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(post_search_blueprint)
app.register_blueprint(user_search_blueprint)

app.run()
