def find_avg_subarray(arr, k):
	results = []

	windowstart = 0
	windowsum = 0

	for i in range(len(arr)):
		windowsum += arr[i]

		if i >= k-1:
			average = windowsum / k
			results.append(average)

			windowsum -= arr[windowstart]

			windowstart =+ 1

	return results


res = find_avg_subarray([1,3,2,6,-1,4,1,8,2] , 5)

print(res)