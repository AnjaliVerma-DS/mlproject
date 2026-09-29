from Flask import Flask,requests,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predic_datapoint():
    if requests.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=requests.form.get('gender'),
            race_ethnicity=requests.form.get('race_ethnicity'),
            parental_level_of_education=requests.form.get('parental_level_of_education'),
            lunch=requests.form .get('lunch'),
            test_preparation_course=requests.get('test_preparation_course'),
            reading_score=requests.form.get('reading_score'),
            writing_score=float(requests.form.get('writing_score'))
        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=predict_pipeline()
        print("Mid prediction")
        results=predict_pipeline.predict(pred_df)
        print("after prediction")
        return render_template('home.html','results=results[0]')


if __name__=="main":
    app.run(host="0.0.0.0")
