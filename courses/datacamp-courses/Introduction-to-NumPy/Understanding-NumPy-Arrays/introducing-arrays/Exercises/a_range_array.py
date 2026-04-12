import numpy as np
from matplotlib import pyplot as plt

# Create an array of integers from one to ten
one_to_ten = np.arange(1, 11)

doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# Create your scatterplot
plt.scatter(
    one_to_ten,
    doubling_array
)
plt.show()