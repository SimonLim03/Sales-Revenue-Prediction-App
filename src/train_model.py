from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
import xgboost as xgb

def create_transformer(categories):
    return Pipeline(steps=[('ordinal_encoder', OrdinalEncoder(categories=[categories]))])


def create_xgb_pipeline(preprocessor, X_train, y_train):
    xgb_pipe = Pipeline(
        steps=[
            ('preprocessor', preprocessor),
            ('xgb', xgb.XGBRegressor())
        ]
    )
    xgb_pipe.fit(X_train, y_train)
    return xgb_pipe

def create_xgb_pipe_tuned(preprocessor, X_train, y_train):
    xgb_pipe_tuned = Pipeline(
        steps=[
            ('preprocessor', preprocessor),
            ('xgb', xgb.XGBRegressor(
                n_estimators=400,  # Number of boosting rounds 
                learning_rate=0.1,  # Step size shrinkage
                max_depth=5,  # Maximum tree depth
                subsample=0.8,  # Fraction of samples used for each boosting round
                colsample_bytree=0.8,  # Fraction of features used for each boosting round
                min_child_weight=1,  # Minimum sum of instance weight in a child
                gamma=0  # Regularization parameter  
            ))
        ]
    )
    xgb_pipe_tuned.fit(X_train, y_train)
    return xgb_pipe_tuned