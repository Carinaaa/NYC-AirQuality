import pandas as pd
from math import inf

# Goal: Analyze how air quality has changed over the years in NYC.

# Parse and clean data
all_data = pd.read_csv("../data/air_data.csv")
all_data.dropna(inplace=True)

# Group by year and compute averages for pollutants.
all_data["years"] = all_data["start_date"].str[:4]

pollutants = all_data.groupby(["name", "years"])["data_value"].agg(['mean','max','min','var'])
print(pollutants)

# Perform rolling averages or smoothing for trendlines.
# Compute anomalies or z-scores for spikes in pollution levels.

# Goal: Compare pollution levels across NYC boroughs.
# Group by borough and calculate average/max pollutant levels.
regions = all_data.groupby(["geo_place_name"])["data_value"].agg(['max',"min","mean"])
print(regions)

# Rank boroughs by overall air quality.
sorted_regions = regions.sort_values("mean") # inplace = False, ascending = True
print(sorted_regions)

# Create masks/filters for borough-level comparisons.
# Normalize pollutant data for fair comparison.

# Goal: Classify days as "Good", "Moderate", "Unhealthy", etc., based on AQI thresholds.
# Create a new column for AQI based on pollutant levels. Map AQI values.
labels = ["good", "moderate", "unhealthy"]
bins = [-inf, 13, 16, inf]
all_data["levels"] = pd.cut(all_data['data_value'], bins=bins, labels=labels)
print(all_data[["data_value","levels"]])

# Vectorize AQI calculations using conditional arrays.
# Simulate random variations or missing data to test robustness.

# Goal: Explore how weather (temperature, wind, humidity) impacts air quality.
regions_periods = all_data.groupby(["geo_place_name","time_period"])
for name, group_df in regions_periods:
    print(f"Group: {name}")

# Merge datasets (air quality + weather).
manhattan_only = all_data[(all_data["geo_place_name"].str.contains("Manhattan")) & (all_data['time_period'].str.contains("2022")) | (all_data['time_period'].str.contains("2023"))]
print(manhattan_only[["geo_place_name","time_period","data_value"]])

manhattan_temperature = pd.read_csv("../data/Filtered_Manhatten_20250731.csv")
manhattan_temperature_summer = manhattan_temperature[manhattan_temperature["Day"].str[:2].isin(["03","04","05","06","07","08"])]
manhattan_temperature_winter = manhattan_temperature[manhattan_temperature["Day"].str[:2].isin(["01","02","09","10","11","12"])]
print(manhattan_temperature_summer)

avg_manhattan = manhattan_only.groupby(["geo_place_name","time_period"])["data_value"].agg('mean')
#print(avg_manhattan)

# Compute correlations.

# Perform linear regression or correlation matrices.
# Create synthetic data for hypothesis testing.

# Goal: Create time-series heatmaps or borough-based spatial maps.
# Pivot tables with time vs pollutant levels.
# Group and reshape data for heatmap input.

# Fill missing values (e.g., interpolation).
# Normalize heatmap values.

# Goal: Build a simple anomaly detection system.
# Track historical pollutant distributions.
# Detect outliers using IQR or z-score methods.

# Compute statistical thresholds.
# Efficiently identify and flag anomalies.

# Goal: Create a simple rule-based system that flags dangerous days based on multiple pollutant thresholds.
# Evaluate multiple thresholds for pollutants.
# Create alert flags.

# Vectorize alert logic (e.g., np.where, boolean masks).