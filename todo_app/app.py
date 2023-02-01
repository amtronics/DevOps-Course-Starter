from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.trello_items import TrelloItems

app = Flask(__name__)
app.config.from_object(Config())
trello = TrelloItems()

@app.route('/')
def index():
    ''' landing page '''
    todos = sorted(trello.get_items(), reverse=True, key=lambda k: k['status'])
    return render_template('index.html', todos=todos)

@app.route('/update', methods=['POST'])
def update():
    ''' for creating new to-do items via the form in index or marking them as complete'''
    completed_ids = request.form.getlist('completedCheck')
    for id in completed_ids:
        item = trello.get_item(id)
        item['status'] = 'Done'
        trello.save_item(item)

    field_name = request.form.get('field_name')
    if field_name:
        # brief sanity check
        trello.add_item(field_name)

    return redirect(url_for('index'))
