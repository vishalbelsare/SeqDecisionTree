import numpy as np

def min_result(list1, n):
	temp = list1
	result = list1
	window = 1
	for iter in range(n):
		temp = np.fmin(temp[0:(np.size(temp)-window)], temp[window:])
		result = np.concatenate((result, temp))
		window = window * 2
	return result


def max_result(list1, n):
	temp = list1
	result = list1
	window = 1
	for iter in range(n):
		temp = np.fmax(temp[0:(np.size(temp)-window)], temp[window:])
		result = np.concatenate((result, temp))
		window = window * 2
	return result

# list1, list2 are the average of the first and second moments of the datapoints
# def avg_sd_result(list1, list2, n):
# 	temp1 = list1
# 	temp2 = list2
# 	result1 = temp1
# 	result2 = np.sqrt(temp2 - np.square(temp1))
# 	window = 1
# 	for iter in range(n):
# 		temp1 = np.nanmean(np.array([temp1[0:(np.size(temp1)-window)], temp1[window:]]), axis = 0)
# 		temp2 = np.nanmean(np.array([temp2[0:(np.size(temp2)-window)], temp2[window:]]), axis = 0)
# 		result1 = np.concatenate((result1, temp1))
# 		result2 = np.concatenate((result2, temp2))
# 		window = window * 2
# 	result2 = np.sqrt(result2 - np.square(result1))
# 	return np.concatenate((result1, result2))

# list1, list2 are the average of the first and second moments of the datapoints
# list3 are the counts 
def avg_sd_result(list1, list2, list3, n):
	temp1 = list1
	temp2 = list2
	temp3 = list3
	result1 = temp1
	result2 = temp2
	window = 1
	for iter in range(n):
		temp1 = temp1 * temp3
		temp2 = temp2 * temp3
		temp1 = np.nansum(np.array([temp1[0:(np.size(temp1)-window)], temp1[window:]]), axis = 0)
		temp2 = np.nansum(np.array([temp2[0:(np.size(temp2)-window)], temp2[window:]]), axis = 0)
		temp3 = np.nansum(np.array([temp3[0:(np.size(temp3)-window)], temp3[window:]]), axis = 0)
		temp4 = np.fmax(temp3, 1)
		temp1 = temp1/temp4
		temp2 = temp2/temp4
		result1 = np.concatenate((result1, temp1))
		result2 = np.concatenate((result2, temp2))
		window = window * 2
	result2 = np.sqrt(result2 - np.square(result1))
	return np.concatenate((result1, result2))


def min_max_avg_sd(stats, n):
	result_min = min_result(stats[:, 0], n)
	result_max = max_result(stats[:, 1], n)
	# result_avg_sd = avg_sd_result(stats[:, 2], np.square(stats[:, 2]) + np.square(stats[:, 3]), n)
	result_avg_sd = avg_sd_result(stats[:, 2], np.square(stats[:, 2]) + np.square(stats[:, 3]) * (1-1/np.fmax(1, stats[:, 4])), stats[:, 4], n)
	return np.concatenate((result_min, result_max, result_avg_sd))


import math 
def col_ref_matrix(n):
	window = 1
	result1 = range(n)
	result2 = range(n)
	size = n
	for iter in range(math.floor(math.log(n, 2))):
		size = size - window
		result1 = np.concatenate((result1, range(0, size)))
		result2 = np.concatenate((result2, range(n-size, n)))
		window = window * 2
	return np.vstack((result1, result2))


# Example
# m = 168
# n = 7
# xx = np.concatenate((np.random.normal(0, 1, (m, 3)), np.zeros((m, 1))), axis = 1)
# result = min_max_avg_sd(xx, 7)

# Example
stats = np.zeros((5, 5))
stats[:, 2] = range(5)
stats[:, 4] = 1
stats[1, 4] = 0
stats[1, 2] = stats[1, 3] = np.nan
stats[3, 4] = 3
result_temp = min_max_avg_sd(stats, 4)


