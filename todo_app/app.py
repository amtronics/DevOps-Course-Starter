from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, get_item, add_item, save_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    ''' landing page '''
    todos = sorted(get_items(), reverse=True, key=lambda k: k['status'])
    return render_template('index.html', todos=todos)

@app.route('/update', methods=['POST'])
def update():
    ''' for creating new to-do items via the form in index or marking them as complete'''
    completed_ids = request.form.getlist('completedCheck')
    for id in completed_ids:
        item = get_item(id)
        item['status'] = 'Completed'
        save_item(item)

    field_name = request.form.get('field_name')
    if field_name:
        # brief sanity check
        add_item(field_name)

    return redirect(url_for('index'))
