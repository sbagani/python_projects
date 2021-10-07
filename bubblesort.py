# def bubblesort(elements):
# 	size = len(elements)

# 	for j in range(size-1):
# 		swapped = False
# 		for i in range(size-1-j):
# 			if elements[i] > elements[i+1]:
# 				elements[i], elements[i+1] = elements[i+1], elements[i]
# 				swapped = True
# 		if not swapped:
# 			break;



# 	print(elements)



# # elements = int(input("Enter an array to be sorted : "))
# elements = [1,89,56,34,2,67,0,12,3]
# bubblesort(elements)




8,3,9,2,7

def bubble_sort(arr):
	size = len(arr)

	for j in range(size-1):
		swapped = False
		for i in range(size-j-1):
			if arr[i] > arr[i+1]:
				arr[i] , arr[i+1] = arr[i+1],arr[i]
				swapped = True
		if not swapped:
			break;
	
	return arr
arr = [6,34,7,2,90,3,78,45]
res = bubble_sort(arr)

print(res)




# def bubblesort(ele):
# 	elements=ele.items()
# 	size=len(elements)
# 	for j in range(size-1):
# 		for i in range(size-j-1):
# 			if elements[i]> elements[i+1]:
# 				elements[i], elements[i+1] = elements[i+1], elements[i]


# ele = [
# {
# 	"name" :"kavya",
# 	"transaction_amount" : 10000,
# 	"device":"iphone-10"
# },
# {
# 	"name" :"sravanthi",
# 	"transaction_amount" : 18500,
# 	"device":"iphone-8"
# },
# {
# 	"name" :"Rohit",
# 	"transaction_amount" : 7000,
# 	"device":"iphone-6s"
# }]
# bubblesort(ele)



