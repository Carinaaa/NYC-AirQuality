# NYC-AirQuality

1. Create a new venv environment and activate

```aiignore
python -m venv .venv

.venv\Scripts\activate
```

2. Install the requirements

```aiignore
 py -m pip install -r .\requirements.txt
```

Data source for Air Quality: https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r/about_data
limited to 2000 due to missing token

Data source for Temperature: https://data.cityofnewyork.us/dataset/Hyperlocal-Temperature-Monitoring/qdq3-9eqn/about_data

Downloaded directly from the website, with filtered data due too detailed data for this scope. 
Also, we will consider 2018-2019 as 2022-2023 for learning purposes. So do not take the results as correct.
