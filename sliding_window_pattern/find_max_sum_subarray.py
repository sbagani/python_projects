def find_max_sum_subarray(arr, k):
	max = 0

	windowstart = 0
	windowsum = 0

	for i in range(len(arr)):
		windowsum += arr[i]

		if i >= k-1:
			if windowsum > max:
				max = windowsum
				
			windowsum -= arr[windowstart]
			windowstart +=1

	return max

res = find_max_sum_subarray([1,2,3,4,5,6], 3)
print(res)
