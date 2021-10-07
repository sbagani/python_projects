import math

def find_smallest_subarray_givensum(arr,sum):

	windowsum = 0
	windowstart = 0
	windowlen =0

	min_size = math.inf

	for i in range(0,len(arr)):
		windowsum += arr[i]
		
		while windowsum >= sum:
			min_size = min(min_size, i - windowstart+1)
			windowsum -= arr[windowstart]

			windowstart += 1

	if min_size == math.inf:
		return 0
	return min_size



res = find_smallest_subarray_givensum([2,1,5,2,3,2], 7)
print(res)

