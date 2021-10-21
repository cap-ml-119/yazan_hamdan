from flask import Flask
from src import prediction_controller

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(prediction_controller.prediction_app)
    app.run(debug=True, port=5000, host="0.0.0.0")
