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
The application was available online via Heroku, but currently it has been shut down due to monthly costs.
However, there is the other way to run the application. Docker and Fastapi were used to run the application.

Execute the following steps to run the app:
- Clone the master branch from the github repo or download a zip folder:  https://github.com/SimonLim03/Sales-Revenue-Prediction-App.git
- Navigate to the root directory of the project in your terminal
- Run the following commands:
    - `docker build -t my_fast_api .`
    - `docker run -p 8000:80 my_fast_api`
    
- There are two API endpoints for descriptions of the app and running the app.
- http://localhost:8000/ : Description of the application, including what to expect for input parameters.
- http://localhost:8000/docs/ : Runnining the application
- /sales/stores/items/ : Predictive Model (predict the sales revenue for a given item in a specific store at a given date)
- /sales/national/ : Forecasting Model (forecast the total sales revenue across all stores and items for the next 7 days)


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
