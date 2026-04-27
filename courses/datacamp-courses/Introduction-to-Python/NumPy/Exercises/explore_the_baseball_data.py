import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
np_baseball = np.array(baseball)

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))