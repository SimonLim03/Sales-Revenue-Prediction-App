# Sales Revenue Prediction Application (Predictive and Forecasting)

## Author
Name: Simon Lim

## Description
This application involves two machine learning models that were established for business purposes.
One model is a predictive model using a Machine Learning algorithm to accurately predict the sales revenue for a given item in a specific store at a given date.
The other is a forecasting model using a time-series analysis that can forecast the total sales revenue across all stores and items for the next 7 days.
The models have been deployed using Fastapi, Docker and Heroku, which enable modle's access to users online anytime. 

The American retailer that has 10 stores across 3 different states (California (CA), Texas (TX), 
Wisconsin (WI)) sells a variety of items from 3 different categories, including hobbies, foods and 
household. The retailer has a large of amount of data for each item’s selling price, sales revenue 
and quantity of sales records across stores and dates. In this regard, machine learning and timeseries models can be potentially helpful in a variety of ways by predicting the sales revenue for a 
specific item and forecasting the total revenues for next few days

![image](https://github.com/SimonLim03/Sales-Revenue-Prediction-App/assets/150989115/02d39b0d-4080-41c4-afea-ac6e15b2998e)


## How to Run the Program
Execute the following steps to run the app:
- URL link: https://flight-fare-prediction-app-b5ff94ahafghdb9bxwllf5.streamlit.app/
- Fill in the input form and hit submit!
![image](https://github.com/SimonLim03/Flight-Fare-Prediction-App/assets/150989115/fd3c49b7-088a-4dba-846a-038d784f1ae5)


## Project Structure
<p>
/models: This folder contains model artefacts that were used to predict travel fares.
</p>

<p>
/notebooks: All the notebooks containing codes, preparation, EDA and precedures. 
</p>

<p>
/report: Experimental report
</p>

<p>
/src: Storage of functions used in experiments
</p>

## Input Parameters

| Input | Description | 
|:------------:|:------------:|
| Origin Airport | Three-character IATA airport code for the initial location | 
| Destination Airport | Three-character IATA airport code for the arrival location | 
| Cabin | String containing the cabin type of the flight (e.g. coach, premium coach, business) |
| Day | Day of Month (i.e., bewteen 1 and 31) |
| Month | Month of Year (e.g., January, December) | 
| Year | Year in yyyy format | Andrew Fuller |
| Departure Time | String containing the departure time period (e.g., Early morining, morning, afternoon, night) | 
