# Readme

## Approach for machine learning
* Use machine learning to find feature importance of ~4 oil prices, ~2 exchange rates.
* A kaggle forum post on the topic: https://www.kaggle.com/questions-and-answers/27537
* Notenooks on what people did for a web traffic competition on Kaggle: https://www.kaggle.com/c/web-traffic-time-series-forecasting
* Try the "basic approach" in this notebook (in list above): https://www.kaggle.com/zoupet/predictive-analysis-with-different-approaches
* Try ARIMA Models in this notebook (in earlier list): https://www.kaggle.com/muonneutrino/wikipedia-traffic-data-exploration

## Note
* To convert unix date (this is the last entry in NYMEX_DL_AV02!, D.csv):

`from datetime import datetime`

`ts = int("1600984800")`

`print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))`
