import pandas as pd
import numpy as np
from numpy import ndarray

df = pd.read_csv("courses/datacamp-courses/Introduction-to-NumPy/Understanding-NumPy-Arrays/introducing-arrays/Datasets/mental_health.csv")

def create_oned_arr(df: pd.Series) -> ndarray:
    """Create one-dimensional array using NumPy Package."""
    oned_arr = np.array(df)
    return oned_arr

def create_twod_arr(df1: pd.Series, df2: pd.Series) -> ndarray:
    """Create two-dimensional array using NumPy Package."""
    twod_arr = np.column_stack([df1, df2])
    return twod_arr

def create_threed_arr(df1: pd.Series, df2: pd.Series) -> ndarray:
    """Create three-dimensional array using NumPy Package."""
    threed_arr = np.array([
        np.column_stack([df1, df2]),
        np.column_stack([df1, df2])
    ])
    return threed_arr

oned_array = create_oned_arr(df["Person_ID"])
print(f"One-dimensional Array:")
print(oned_array)

print()

twod_array = create_twod_arr(df["Person_ID"], df["Age"])
print(f"Two-dimensional Array:")
print(twod_array)

print()

threed_array = create_threed_arr(df["Person_ID"], df["Occupation"])
print(threed_array.shape)