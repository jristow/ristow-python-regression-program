import numpy as np
from scipy import stats

randomData = np.random.normal(5.0, 1.0, 1000)
randomData2 = 100 - (randomData + np.random.normal(0, 1, 1000) * 3)

slope, intercept, r_value, p_value, std_err = stats.linregress(randomData, randomData2)

print(
    "The slope is: {}\n".format(slope) +
    "The intercept is: {}\n".format(intercept) +
    "The R squared value is: {}\n".format(r_value**2) +
    "The standard error is: {}".format(std_err)
)