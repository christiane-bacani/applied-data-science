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
    if data_shape == (1):
        return np.random.random()

    else:
        return np.random.random(size=data_shape)

one_dim_array = create_1D_arr(df["Person_ID"])
print("One-dimensional array:")
print(one_dim_array)

print()

two_dim_array = create_2D_arr(df["Person_ID"], df["Age"])
print("Two-dimensional array:")
print(two_dim_array)

print()

three_dim_array = create_3D_arr(df["Person_ID"], df["Occupation"])
print("Three-dimensional array:")
print(three_dim_array)

print()

one_dim_zero_elem_array = create_zero_elem_arr(data_shape=(2000))
print("One-dimensional zero elements array:")
print(one_dim_zero_elem_array)

print()

two_dim_zero_elem_array = create_zero_elem_arr(data_shape=(2000, 4))
print("Two-dimensional zero elements array:")
print(two_dim_zero_elem_array)

print()

three_dim_zero_elem_array = create_zero_elem_arr(data_shape=(3, 2000, 4))
print("Three-dimensional zero elements array:")
print(three_dim_zero_elem_array)

print()

one_dim_random_elem_array = create_random_elem_arr(data_shape=(1))
print("One-dimensional random elements array:")
print(one_dim_random_elem_array)

print()

two_dim_random_elem_array = create_random_elem_arr(data_shape=(4, 4))
print("Two-dimensional random elements array:")
print(two_dim_random_elem_array)

print()

three_dim_random_elem_array = create_random_elem_arr(data_shape=(2, 10, 10))
print("Three-dimensional random elements array:")
print(three_dim_random_elem_array)