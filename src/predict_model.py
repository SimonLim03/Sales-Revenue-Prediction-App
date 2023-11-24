from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def calculate_regression_metrics(y_test, pred):
    rmse = mean_squared_error(y_test, pred, squared=False)
    mse = mean_squared_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    mae = mean_absolute_error(y_test, pred)
    metrics = {
        "RMSE": rmse,
        "MSE": mse,
        "R2": r2,
        "MAE": mae
    }
    return metrics