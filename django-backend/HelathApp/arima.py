from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
from .models import DiseaseCaseReport

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def predict_cases(df):

    # Convert date column
    df["report_date"] = pd.to_datetime(df["report_date"])

    # Sort by date
    df = df.sort_values("report_date")

    # Set index
    df.set_index("report_date", inplace=True)

    # Time series
    series = df["case_count"]

    # Train ARIMA
    model = ARIMA(series, order=(2,1,2))

    model_fit = model.fit()

    # Forecast next 30 days
    forecast = model_fit.get_forecast(steps=30)

    predicted = forecast.predicted_mean

    confidence = forecast.conf_int()

    return {

        "actual": series,

        "predicted": predicted,

        "confidence": confidence

    }