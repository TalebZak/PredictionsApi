from flask import Flask
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)


class TemperaturePrediction(Resource):
    def get(self):
        df = pd.read_csv('predictions/temperature predictions.csv', index_col=False)
        data = df.to_dict('records')
        answer = {}
        for element in data:
            answer[element['Year']] = element

        return answer, 200


class CarbonEmissions(Resource):
    def get(self):
        df = pd.read_csv('predictions/carbon emissions.csv', index_col=False)
        data = df.to_dict('records')
        answer = {}
        for element in data:
            answer[element['Year']] = element
        return answer, 200


api.add_resource(TemperaturePrediction, '/temperature-prediction')
api.add_resource(CarbonEmissions, '/carbon-emissions')
if __name__ == '__main__':
    app.run()
