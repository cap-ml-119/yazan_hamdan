PREDICTION_SCHEMA = {
    'type': "object",
    'properties': {
        'season': {
            'type': 'number',
        },
        'weather': {
            'type': 'number',
        },
        'temp': {
            'type': 'number',
        },
        'humidity': {
            'type': 'number',
        },
        'windspeed': {
            'type': 'number',
        },
        'month': {
            'type': 'number',
        },
        'hour': {
            'type': 'number',
        },
    },
    'required': ['season', 'weather', 'temp', 'humidity', 'windspeed', 'month', 'hour']
}


def allowed_file(filename):
    """Check if the uploaded file is a csv file

    Args:
        filename (string): uploaded file name

    Returns:
        bool: returns true if the file exctention is csv, false otherwise
    """
    return '.' in filename and filename.split('.', 1)[1].lower() == 'csv'


def uploading_file_helper(request):
    """check if the post request has the file part

    Args:
        request (Request): Request body, to check if it contains a file

    Raises:
        Exception: If there is no file attached

    Returns:
        FileStorage: File attached
    """
    if 'file' not in request.files:
        raise Exception("No File attached")

    return request.files.get("file")


def generate(data):
    """Convert a list into a string

    Args:
        data (list of number): To be converted into a string

    Returns:
        [string]: Converted list
    """
    temp = ""
    for row in data:
        temp += str(row[0]) + "\n"

    return temp


def get_json_data(obj):
    """Gets all values of a Dict

    Args:
        obj (Dict): To extract values of json

    Returns:
        [list of string]: Values of a given dict without keys
    """
    temp_list = []
    obj_keys = obj.keys()

    for key in obj_keys:
        temp_list.append(obj[key])

    return temp_list
