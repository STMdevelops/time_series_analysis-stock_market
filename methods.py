from statsmodels.tsa.stattools import adfuller, acf, pacf
import pandas as pd
def adf_test(series, title=""):
    print(f'Augmented Dickey-Fuller Test: {title}')
    result = adfuller(series.dropna())
    labels = ['ADF Statistic', "p-value", "Lags Used", "Observations Used"]
    out = pd.Series(result[0:4], index=labels)
    for key, value in result[4].items():
        out[f'Critical Value ({key})'] = value
    print(out.to_string())
    print('')