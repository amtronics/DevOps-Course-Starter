from flask import Flask, render_template, request, redirect, url_for
from flask_dance.contrib.github import github
from todo_app.flask_config import Config
from todo_app.data.db_items import DatabaseAPI
from todo_app.data.view_model import ViewModel
from todo_app.oauth import blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    database = DatabaseAPI()
    app.register_blueprint(blueprint, url_prefix="/login")

    def login_required(func):
        def wrapper():
            if not github.authorized:
                redirect(url_for("github.login"))
            else:
                func()
        return wrapper

    @login_required
    @app.route('/')
    def index():
        ''' landing page '''
        items = database.items
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @login_required
    @app.route('/complete_item/<id>/<status>', methods=['POST'])
    def complete_item(id, status):
        ''' Mark item <id> as complete or to do'''
        database.save_item(id, status)
        return redirect(url_for('index'))

    @login_required
    @app.route('/add_item', methods=['POST'])
    def add_item():
        ''' for creating new to-do items via the form in index'''
        item_name = request.form.get('new_item')
        if item_name:
            # brief sanity check
            database.add_item(item_name)
        return redirect(url_for('index'))

    return app
