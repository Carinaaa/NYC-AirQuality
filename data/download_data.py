import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofnewyork.us", None)
aq_results = client.get("c3uy-2p5r", limit=2000)
#weather_results = client.get("qdq3-9eqn", limit=1000)

aq_results_df = pd.DataFrame.from_records(aq_results)
#weather_results_df = pd.DataFrame.from_records(weather_results)

aq_results_df.to_csv("air_data.csv")
#weather_results_df.to_csv("weather_data.csv")
