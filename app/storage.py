import uuid

# Task in memory
todo_list = []


# Note: I used term "Task" to represent a to do object in comments below
def update_task_by_id(task_id: str, status: int, description: str) -> Exception:
    """A function that is responsible for updating a task by its ID
    throw an exception if ID wasn't found

    Args:
        task_id (str): Unique identifier for the task used for searching
        status (int): The new task status as int
        description (str): The new description of the task
    """
    if status > 3:
        raise Exception("status value should be smaller than 4")
    if status < 1:
        raise Exception("status value should be greater than 0")

    for obj in todo_list:
        if obj['id'] == task_id:
            obj['status'] = status
            obj['task'] = description
            return

    raise Exception(f"Task with ID : {task_id} is not found")


def update_task_status_by_id(task_id: str, status: int):
    """A function that is responsible for updating a task status by its ID
    throw an exception if ID wasn't found

    Args:
        task_id (str): Unique identifier for the task used for searching
        status (int): The new task status as int
    """
    if status > 3:
        raise Exception("status value should be smaller than 4")
    if status < 1:
        raise Exception("status value should be greater than 0")

    for obj in todo_list:
        if obj['id'] == task_id:
            obj['status'] = status
            return

    raise Exception(f"Task with ID : {task_id} is not found")


def insert_new_task(description: str) -> None:
    """A function that is responsible for creating a new task
    generate a unique ID, status is 0 by default

    Args:
        text (str): [description of the new task created
    """
    todo_list.append(
        {
            'id': str(uuid.uuid1()),
            'task': description,
            'status': 1
        }
    )


def remove_task_by_id(task_id: str) -> None:
    """A function that is responsible for deleting a task by its ID
    Throw an exception if ID wasn't found

    Args:
        task_id (str): The ID of a task that will be removed
    """
    for index, value in enumerate(todo_list):
        if value['id'] == task_id:
            del todo_list[index]
            return

    raise Exception(f"Task with ID : {task_id} is not found")


def get_task_by_id(task_id) -> dict:
    """A function that finds and returns task by its ID
    throw an exception if ID wasn't found

    Args:
        task_id (str): ID of the task which will be returned
    """
    for task in todo_list:
        if task['id'] == task_id:
            return task

    raise Exception(f"Task with ID : {task_id} is not found")


def get_all_data() -> [dict]:
    if len(todo_list) == 0:
        raise Exception("There is no data stored")

    return todo_list
