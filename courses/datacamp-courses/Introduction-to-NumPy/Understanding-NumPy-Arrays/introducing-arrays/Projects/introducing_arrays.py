import pandas as pd
import numpy as np

def create_oned_arr(df: pd.Series):
    oned_arr = np.array(df)
    return oned_arr

df = pd.read_csv("courses/datacamp-courses/Introduction-to-NumPy/Understanding-NumPy-Arrays/introducing-arrays/Datasets/mental_health.csv")

person_id = create_oned_arr(df["Person_ID"])
print(person_id)