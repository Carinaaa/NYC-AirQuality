import pandas as pd
import numpy as np

results_df = pd.read_csv("../data/air_data.csv")

# Create a 1-dimensional NumPy array using np.array()

array_1 = np.array(results_df["geo_place_name"][:3])
print(array_1)
print(array_1.shape)
print(array_1.dtype)
print(array_1.ndim)
print(type(array_1))

# Create a 2-dimensional NumPy array using np.array()
array_2 = np.array([results_df["geo_place_name"][:3].tolist(), results_df["time_period"][:3].tolist()])
print(array_2)
print(array_2.shape)
print(array_2.dtype)
print(array_2.ndim)
print(type(array_2))

# Create a 3-dimensional Numpy array using np.array()
array_3 = np.array([
                    [results_df["geo_place_name"][:3].tolist(), results_df["time_period"][:3].tolist()],
                    [results_df["geo_place_name"][:3].tolist(), results_df["time_period"][:3].tolist()]
                    ])
print(array_3)
print(array_3.shape)
print(array_3.dtype)
print(array_3.ndim)
print(type(array_3))

# Import pandas and create a DataFrame out of one
# of the arrays you've created
df_array_3 = pd.DataFrame(array_3[0])
print(df_array_3)

# Create an array of shape (10, 2) with only ones
ones = np.ones(shape = (10,2))
print(ones)
print(ones.shape)

# Create an array of shape (7, 2, 3) of only zeros
zeros = np.zeros(shape=(7,2,3))
print(zeros.shape)

# Create an array within a range of 0 and 100 with step 3
step_array = np.arange(0,100,3)

# Create a random array with numbers between 0 and 10 of size (7, 2)
random_array = np.random.randint(10, size=(7,2))

# Create a random array of floats between 0 & 1 of shape (3, 5)
random_floats_array = np.random.random(size=(3,5))

# Set the random seed to 42
np.random.seed(42)
# Create a random array of numbers between 0 & 10 of size (4, 6)
random_seed_array = np.random.randint(10, size=(4,6))

# Create an array of random numbers between 1 & 10 of size (3, 7)
# and save it to a variable
random_int_array = np.random.randint(1,10, size=(3,7))

# Find the unique numbers in the array you just created
print(np.unique(random_int_array))

# Find the 0'th index of the latest array you created
print(random_int_array[0])

# Get the first 2 rows of latest array you created

# Get the first 2 values of the first 2 rows of the latest array

# Create a random array of numbers between 0 & 10 and an array of ones
# both of size (3, 5), save them both to variables

# Add the two arrays together

# Create another array of ones of shape (5, 3)

# Try add the array of ones and the other most recent array together


