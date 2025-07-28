import numpy as np
import pandas as pd

results_df = pd.read_csv("../data/air_data.csv")

# Get the first 2 rows of latest array you created, size=(3,7)
my_np = np.array([results_df["unique_id"][:7].tolist(),results_df["geo_type_name"][:7].tolist(),results_df["name"][:7].tolist()])
print(my_np[:2])

# Get the first 2 values of the first 2 rows of the latest array
print(my_np[:2,:2])

# Create a random array and an array of ones
# both of size (3, 5), save them both to variables
first_array = np.random.choice(results_df["unique_id"][:7].tolist(),size = (3,5))
ones_array = np.ones((3,5))

# Add the two arrays together
print(first_array + ones_array)

# Create another array of ones of shape (5, 3)
one_reverted_array = np.ones((5,3))

# Add the array of ones and the other most recent array together
print(first_array + one_reverted_array.T)

# Subtract the new array of ones from the other most recent array
print(first_array - one_reverted_array.T)

# Multiply the ones array with the latest array
print(first_array * one_reverted_array.T)

# Take the array to the power of 2 using '**'
print(first_array ** 2)

# Do the same thing with np.square()
print(np.square(np.array(results_df["geo_join_id"][:7])))

# Find the mean of the array using np.mean()
print(np.mean(np.array(results_df["data_value"][:7])))

# Find the maximum of the latest array using np.max()
print(np.max(np.array(results_df["data_value"][:7])))

# Find the minimum of the latest array using np.min()
print(np.min(np.array(results_df["data_value"][:7])))

# Find the standard deviation of the latest array
print(np.std(np.array(results_df["data_value"][:7])))

# Find the variance of the latest array
print(np.var(np.array(results_df["data_value"][:7])))
