import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder

def preprocess_data(df):
    df["revenues"] = df["sales"] * df["sell_price"]
    df["is_event"] = df["event_type"].apply(lambda x: 0 if x == 0 else 1)
    df["day_of_week"] = pd.to_datetime(df['date']).dt.day_name()
    df["year"] = pd.to_datetime(df['date']).dt.year
    df["month"] = pd.to_datetime(df['date']).dt.month
    df['day'] = pd.to_datetime(df['date']).dt.day
    return df

def drop_columns(df, columns_to_drop):
    df.drop(columns=columns_to_drop, inplace=True)
    
def create_transformer(categories):
    return Pipeline(steps=[('ordinal_encoder', OrdinalEncoder(categories=[categories]))])