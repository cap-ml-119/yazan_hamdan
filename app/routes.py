from app import app
from flask import request, jsonify
from app import storage as db_helper


@app.route('/api/v1/todo', methods=['POST'])
def create():
    """The controller which is responsible for creating a new task
    receives 1 key in the body which is:
             1) task: description of the task as a string

    Returns:
        object(dictionary): Describe the returned result
        whether it worked or not
    """
    try:
        data = request.get_json()
        db_helper.insert_new_task(data['task'])
        result = {
            'success': True,
            'response': 'Done'
        }

    except:
        result = {
            'success': False,
            'response': 'Inserting task failed'
        }

    return jsonify(result)


@app.route('/api/v1/todo/<id>', methods=['PUT'])
def update(id):
    """The controller which is responsible for updating an existing task by its ID
    receives 2 keys in the body which are:
            1) task: description of the task as a string
            2) status: status of the task as a number

    Args:
        id (int): ID of task to be updated

    Returns:
        object(dictionary): Describe the returned result
        whether it worked or not
    """
    try:
        data = request.get_json()
        db_helper.update_task_by_id(id, data["status"], data['task'])
        result = {
            'success': True,
            'response': 'Task updated successfully'
        }

    except Exception as e:
        result = {
            'success': False,
            'response': 'Something went wrong',
            "message": str(e)
            }

    return jsonify(result)


@app.route('/api/v1/todo/<id>', methods=['PATCH'])
def update_status(id):
    try:
        data = request.get_json()
        db_helper.update_task_status_by_id(id, data["status"])
        result = {
            'success': True,
            'response': 'Task updated successfully'
        }

    except Exception as e:
        result = {
            'success': False,
            'response': 'Something went wrong',
            "message": str(e)
        }

    return jsonify(result)


@app.route('/api/v1/todo/<id>', methods=['DELETE'])
def delete(id):
    """The controller which is responsible for deleting an existing task by its ID

    Args:
        id (int): ID of the task to be deleted

    Returns:
        object(dictionary): Describe the returned result
        whether it worked or not
    """
    try:
        db_helper.remove_task_by_id(id)
        result = {
            'success': True,
            'response': 'Removed task'
        }

    except Exception as e:
        result = {
            'success': False,
            'response': 'Something went wrong',
            "message": str(e)
        }

    return jsonify(result)


@app.route('/api/v1/todo/<id>', methods=['GET'])
def get(id):
    """The controller which is responsible for retrieving a task by its ID

    Args:
        id (int): ID of the task which will be retrieved

    Returns:
        object(dictionary): Describe the returned result
        whether it worked or not
    """
    try:
        result = db_helper.get_task_by_id(id)

    except Exception as e:
        result = {
                'success': False,
                'response': 'Something went wrong',
                "message": str(e)
        }

    return jsonify(result)


@app.route('/api/v1/todo/', methods=['GET'])
def getAll():
    """The controller which is responsible for retrieving all stored tasks

    Returns:
        list(array): array of all stored tasks
    """
    return jsonify(db_helper.todo_list)