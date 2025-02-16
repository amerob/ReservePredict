import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

def load_pipeline():
    with open('./predict_pipeline.pickle', 'rb') as f:
        pipeline = pickle.load(f)
    return pipeline


def predict_cancellation(input_data):
    pipeline = load_pipeline()

    selected_features = ['type_of_meal_plan',
                         'room_type_reserved',
                         'market_segment_type',
                         'lead_time',
                         'avg_price_per_room',
                         'no_of_special_requests']
    input_df = pd.DataFrame([input_data], columns=selected_features)

    prediction = pipeline.predict(input_df)
    probability = pipeline.predict_proba(input_df)[:, 1]

    if probability < 0.5:
        prediction = 1 - prediction
        probability = 1 - probability

    return prediction[0], probability


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    prob = None

    if request.method == 'POST':
        sample_input = {
            'type_of_meal_plan': request.form.get('type_of_meal_plan'),
            'room_type_reserved': request.form.get('room_type_reserved'),
            'market_segment_type': request.form.get('market_segment_type'),
            'lead_time': float(request.form.get('lead_time')),
            'avg_price_per_room': float(request.form.get('avg_price_per_room')),
            'no_of_special_requests': int(request.form.get('no_of_special_requests'))
        }

        result, prob = predict_cancellation(sample_input)

    return render_template('index.html', result=result, prob=prob)


if __name__ == '__main__':
    app.run(debug=True)
