from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.trello_items import TrelloAPI

app = Flask(__name__)
app.config.from_object(Config())
trello = TrelloAPI()

@app.route('/')
def index():
    ''' landing page '''
    todos = sorted(trello.get_items(), reverse=True, key=lambda k: (k.status, k.name))
    return render_template('index.html', todos=todos)

@app.route('/complete_item/<id>/<status>', methods=['POST'])
def complete_item(id, status):
    ''' Mark item <id> as complete or to do'''
    trello.save_item(id, status)
    return redirect(url_for('index'))

@app.route('/add_item', methods=['POST'])
def add_item():
    ''' for creating new to-do items via the form in index'''
    item_name = request.form.get('new_todo')
    if item_name:
        # brief sanity check
        trello.add_item(item_name)
    return redirect(url_for('index'))
