# Sales Revenue Prediction Application (Predictive and Forecasting)

## Author
Name: Simon Lim

## Description
This application is a machine learning product, which can predict the expected flight fare for different airport trips. 
In particular, this project split the travel airfare into 4 different fares, including minimum, median, modal and mean of airfare
Together, these metrics aim to provide a comprehensive overview of potential fares to users.
To enable model’s access to users, Docker and Streamlit were used for model deployment, enabling users to use the models as a application.


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
/raw: Initial datasets.
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
