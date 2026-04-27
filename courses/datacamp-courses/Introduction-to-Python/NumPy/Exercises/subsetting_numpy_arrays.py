import numpy as np

weight_lb = [
    [74, 74, 72, 75, 75, 73]
    [1.8796, 1.8796, 1.8288, 1.905, 1.905, 1.8542]
]

height_in = [
    [74, 74, 72, 75, 75, 73]
    [1.8796, 1.8796, 1.8288, 1.905, 1.905, 1.8542]
]

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])