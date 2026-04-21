import pandas as pd
import numpy as np
from numpy import ndarray

df = pd.read_csv("courses/datacamp-courses/Introduction-to-NumPy/Understanding-NumPy-Arrays/introducing-arrays/Datasets/mental_health.csv")

def create_1D_arr(df: pd.Series) -> ndarray:
    """Create one-dimensional array using NumPy Package."""
    one_dim_arr = np.array(df)
    return one_dim_arr

def create_2D_arr(df1: pd.Series, df2: pd.Series) -> ndarray:
    """Create two-dimensional array using NumPy Package."""
    two_dim_arr = np.column_stack([df1, df2])
    return two_dim_arr

def create_3D_arr(df1: pd.Series, df2: pd.Series) -> ndarray:
    """Create three-dimensional array using NumPy Package."""
    three_dim_arr = np.array([
        np.column_stack([df1, df2]),
        np.column_stack([df1, df2])
    ])
    return three_dim_arr

def create_zero_elem_arr(data_shape: tuple) -> ndarray:
    """Create NumPy Array based on the given dataset shape."""
    zero_elem_arr = np.zeros(shape=data_shape)
    return zero_elem_arr

def create_random_elem_arr(data_shape: tuple) -> ndarray:
    """Create NumPy Array with random elements based on the given dataset shape."""
    random_elem_arr = np.random.random(data_shape)
    return random_elem_arr

def create_range_elem_arr(range: tuple) -> ndarray:
    """Create One-dimensional NumPy Array based on the given range."""
    if type(range) is int:
        range_elem_arr = np.arange(range)

    elif range is None or len(range) > 3:
        return

    elif len(range) == 2:
        range_elem_arr = np.arange(range[0], range[1])

    else:
        range_elem_arr = np.arange(range[0], range[1], range[2])

    return range_elem_arr

one_dim_array = create_1D_arr(df["Person_ID"])
print("1D Array:")
print(one_dim_array)

print()

two_dim_array = create_2D_arr(df["Person_ID"], df["Age"])
print("2D Array:")
print(two_dim_array)

print()

three_dim_array = create_3D_arr(df["Person_ID"], df["Occupation"])
print("3D Array:")
print(three_dim_array)

print()

one_dim_zero_elem_array = create_zero_elem_arr(data_shape=(2000))
print("1D Array using np.zeros(2000)")
print(one_dim_zero_elem_array)

print()

two_dim_zero_elem_array = create_zero_elem_arr(data_shape=(2000, 4))
print("2D Array using np.zeros(2000, 4)")
print(two_dim_zero_elem_array)

print()

three_dim_zero_elem_array = create_zero_elem_arr(data_shape=(3, 2000, 4))
print("3D Array using np.zeros(3, 200, 4):")
print(three_dim_zero_elem_array)

print()

one_dim_random_elem_array = create_random_elem_arr(data_shape=(1))
print(f"1D Array using np.random.random(1):")
print(one_dim_random_elem_array)

print()

two_dim_random_elem_array = create_random_elem_arr(data_shape=(4, 4))
print("2D Array using np.random.random(4, 4):")
print(two_dim_random_elem_array)

print()

three_dim_random_elem_array = create_random_elem_arr(data_shape=(2, 10, 10))
print("3D Array using np.random.random(2, 10, 10):")
print(three_dim_random_elem_array)

print()

one_dim_range_elem_array = create_range_elem_arr(range=(11))
print("1D Array using np.arange(11)")
print(one_dim_range_elem_array)

print()

one_dim_range_elem_array = create_range_elem_arr(range=(1, 101))
print("1D Array using np.arange(1, 100):")
print(one_dim_range_elem_array)

print()

one_dim_range_elem_array = create_range_elem_arr(range=(1, 101, 2))
print("1D Array using np.arange(1, 101, 2):")
print(one_dim_range_elem_array)