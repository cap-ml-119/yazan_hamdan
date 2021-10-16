from io import StringIO
from flask import request, Blueprint
from flask_expects_json import expects_json
import pickle
import pandas as pd
from werkzeug.wrappers import Response
from src import services

prediction_app = Blueprint('prediction_app', __name__, url_prefix='/api/v1')

# To Open Model
with open("./model/vFjXi.sav", 'rb') as handle:
    pipeline = pickle.load(handle)


@prediction_app.route('/predict', methods=['POST'])
@expects_json(services.PREDICTION_SCHEMA)
def single_prediction():
    try:
        data = request.get_json()
        response = {
            "status": 200,
            "predicted_value": pipeline.predict([services.get_json_data(data)])[0][0]
        }
    except Exception as e:
        response = {
            'status': 400,
            "response": str(e)
        }

    return response


@prediction_app.route('/batch-predict', methods=['POST'])
def batch_predict():
    try:
        file = services.uploading_file_helper(request)
        dataframe = pd.read_csv(StringIO(file.stream.read().decode('utf-8')))
        predictions = pipeline.predict(dataframe)

        # stream the response as the data is generated
        response = Response(services.generate(predictions), mimetype='text/csv')
        # add a filename
        response.headers.set("Content-Disposition", "attachment", filename="predictions.csv")
    except Exception as e:
        response = {
            'status': 400,
            "response": str(e)
        }

    return response
