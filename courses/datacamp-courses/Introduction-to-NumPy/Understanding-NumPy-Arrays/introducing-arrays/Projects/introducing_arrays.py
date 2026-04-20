import pandas as pd
import numpy as np

def create_oned_arr(df: pd.Series) -> np.array:
    """Create one-dimensional array using NumPy Package."""
    oned_arr = np.array(df)
    return oned_arr

def create_twod_arr(df1: pd.Series, df2: pd.Series) -> np.array:
    """Create two-dimensional array using NumPy Package."""
    twod_arr = np.column_stack([df1, df2])
    return twod_arr

df = pd.read_csv("courses/datacamp-courses/Introduction-to-NumPy/Understanding-NumPy-Arrays/introducing-arrays/Datasets/mental_health.csv")

person_id = create_oned_arr(df["Person_ID"])
print(f"One-dimensional Array:")
print(person_id)

print()

person_id_and_age = create_twod_arr(df["Person_ID"], df["Age"])
print(f"Two-dimensional Array:")
print(person_id_and_age)