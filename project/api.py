# api.py

import os
from flask import Blueprint, render_template, request, json
from flask_login import login_required, current_user
from pyproj import Transformer

#api = Blueprint('main', __name__)
print("hi")

# api.py

import os
from flask import Blueprint, render_template, request, json
from flask_login import login_required, current_user
from pyproj import Transformer
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
##api.add_resource(TodoList, '/todos')
##api.add_resource(#)


if __name__ == '__main__':
    app.run(debug=True)
#@api.route('/profile', methods=['POST'])
#def api_post():
#	x = request.form.get('lng')
	#y = form.getvalue('lat')
	#trFrom = form.getvalue('trFrom')
	#trTo = form.getvalue('trTo')
	#xx, yy = pyproj.transform(trFrom, trTo, x, y)
	#return redirect(url_for('main.profile'))
	#print xx, yy
