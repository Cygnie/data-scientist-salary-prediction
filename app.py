# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import jsonify
import requests
import numpy as np
import pandas as pd
import sklearn
import pickle
import datetime


app = Flask(__name__)
model = pickle.load(open('DS_salaries_Pipe.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route("/predict", methods=['POST'])
def predict():
    
    employee_residence_country_list= ['Other', 'DE', 'US', 'GB', 'FR', 'IN', 'PK', 'GR', 'CA', 'ES','BR', 'NL', 'PT', 'JP']
    company_location_country_list = ['NZ', 'DE', 'US', 'GB', 'PL', 'FR', 'IN', 'PK', 'UA', 'AU', 'GR',
                                       'CA', 'NG', 'EE', 'CZ', 'BE', 'ES', 'AT', 'BR', 'DZ', 'IR', 'NL',
                                       'HU', 'PT', 'TR', 'JP', 'HN', 'MT', 'AE', 'LU', 'RO', 'SG', 'CH',
                                       'MY', 'MX', 'IT', 'HR', 'IL', 'DK', 'RU', 'CO', 'IQ', 'CN']
    if request.method == 'POST':
        
        Year = int(request.form['Year'])
        year = int(datetime.datetime.now().year) - Year
        
        experience_level=request.form['experience_level']
        employment_type=request.form['employment_type']
        job_title=request.form['job_title']
        
        employee_residence = request.form['employee_residence']
        
        if employee_residence.strip().upper() not in employee_residence_country_list:
           employee_residence ="Other"
        
        company_location = request.form['company_location']
        
        if company_location.strip().upper() not in company_location_country_list:
           company_location ="Other"
        
        remote_ratio=request.form['remote_ratio']
        company_size=request.form['company_size']
        
        prediction_table = {"experience_level":experience_level, 
                            "employment_type":employment_type, 
                            "job_title":job_title,
                            "employee_residence":employee_residence, 
                            "remote_ratio":remote_ratio, 
                            "company_location":company_location,
                            "company_size":company_size, 
                            "year":year}
        prediction_DF = pd.DataFrame(data=[prediction_table])

        output = model.predict(prediction_DF)

        if output<0:
            return render_template('home.html',prediction_text="Sorry you cannot predict your salary")
        else:
            return render_template('home.html',prediction_text="your estimated salary is {}".format(output[0]))
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)
