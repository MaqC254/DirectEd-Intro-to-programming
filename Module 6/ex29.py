#imports mean function from statistics library
from statistics import mean
#imports mode function from statistics library
from statistics import mode
#imports medain function from statistics library
from statistics import median
#imports variance function from statistics library
from statistics import variance
#initializes a list of ages
ages = [5, 10, 15, 20, 25]
#calls mean function from statistic library that calculates the mean
mean_age = mean(ages)
#prints the mean of the ages
print(mean_age)
#calls median function from statistic library that finds the median
median_age = median(ages)
#prints the median of the ages
print(median_age)
#calls mode function from statistic library that calculates the mode
mode_age = mode(ages)
#prints the mode of the ages
print(mode_age)
#calls variance function from statistic library that calculates the variance
variance_age = variance(ages)
#prints the variance of the ages
print(variance_age)