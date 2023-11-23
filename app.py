from fastapi import FastAPI
from starlette.responses import JSONResponse
from joblib import load
import pandas as pd
from datetime import datetime, timedelta
import calendar
from prophet import Prophet

app = FastAPI()

cat_pipe = load('/models/cat_pipe.pkl')
prophet = load('/models/prophet_model.joblib')

project_description = {
    "project_name": "Sales Revenues Prediction",
    "project_objective": (
        "The objective of the project is to build two different models. "
        "One model predicts the sales revenue for specific items at specific dates, "
        "and the other forecasts the total sales revenues for the next 7 days."
    ),
    "list_of_endpoints": ["/", "/health/", "/sales/national/", "/sales/stores/items/"],
    "input_parameters (Predictive Model)": [
        "item_id",
        "store_id",
        "year",
        "month",
        "day"
    ],
    "input_parameters (Predictive Model)": [
        "specific_date",
        "days"
    ],
    "output_model": (
        "Predictive model for sales revenue for a given item"
        "Forecasting model for the total sales revenue for the next 7 days."
    ),
    "github_repo": "https://github.com/SimonLim03/Sales-Revenue-Prediction-App",
}

@app.get("/")
def read_root():
    return project_description


@app.get('/health/', status_code=200)
def healthcheck():
    return 'Hi, API endpoints are available. The application is available for predicting the sales revenue for specific item.!'

    
@app.get("/sales/stores/items/")
def predict(item_id, store_id, yr, mm, day):
    
    mm = {month: index for index, month in enumerate(calendar.month_name) if month}.get(mm, None)
    date = pd.to_datetime(f'{int(yr)}-{mm}-{int(day)}')
    today = pd.to_datetime('today')

    day_of_week = pd.Series(date).dt.dayofweek
    
    df = pd.DataFrame({'item_id' : [item_id],
                       'store_id' : [store_id],
                       'year' : [yr],
                       'month' : [mm],
                       'day' : [day],
                       'day_of_week' : [day_of_week]    
    })
    
    pred = cat_pipe.predict(df)
    return JSONResponse(pred.tolist())



@app.get("/sales/national/")
def predict(specific_date: str = None, days: int = 7):
    TODAY = pd.to_datetime('today').date()

    if specific_date:
        # If a specific date is provided, use it as the starting date
        start_date = pd.to_datetime(specific_date).date()
    else:
        # Otherwise, use today's date
        start_date = TODAY

    future = start_date + pd.to_timedelta(days, unit='D')

    dates = pd.date_range(start=start_date, end=future.strftime("%Y-%m-%d"))
    df = pd.DataFrame({"ds": dates})

    forecast = prophet.predict(df)

    # Extract the forecast for the next 7 days
    forecast_next_7_days = forecast[['ds', 'yhat']].tail(days)

    # Return the forecast for the next 7 days
    return forecast_next_7_days.to_dict(orient="records")