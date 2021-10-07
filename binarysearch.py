# def binary_search(arr,x):
# 	low =0

# 	high = len(arr) -1

# 	mid = 0

# 	while low <= high :
# 		mid = (high + low) // 2

# 		if arr[mid] < x: 
# 			low = mid +1
# 		elif arr[mid] > x:
# 			high = mid -1
# 		else:
# 			return mid
# 	return -1

# arr = [2,3,4,10,40,80,109,111]

# x = 109

# result = binary_search(arr,x)

# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")





def binary_search(arr, x):
	low =0

	high = len(arr)-1

	mid = 0

	while low <= high:
		mid = (high + low) //2
		if arr[mid] < x:
			low = mid+1
		elif arr[mid] > x:
			high = mid -1
		else:
			return mid
	return -1


result = binary_search([1,2,3,4,5,6,7,8,9,10],9)
if result != -1:
	print(f"elemnet is at the index {result}")
else:
	print("Element is not in the list")




































