from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    ''' landing page '''
    todos = get_items()
    return render_template('index.html', todos=todos)

@app.route('/create', methods=['POST'])
def create():
    ''' for creating new to-do items via the form in index '''
    field_name = request.form.get('field_name')
    print(request.form)
    add_item(field_name)
    return redirect(url_for('index'))
