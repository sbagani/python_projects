def swap_list(list1):
	size = len(list1)

	temp = list1[0]
	list1[0] = list1[size-1]
	list1[size-1]=temp

	return list1

list1 = [12,34,56,78,90]
#swap_list(list1)
#print(list1)


def swap_by_pos(list2, pos1,pos2):
	temp = list2[pos1]
	list2[pos1]=list2[pos2]
	list2[pos2]=temp
	return list1

list2 = [1,2,3,4,5,6,7,8,9]
# swap_by_pos(list2,0,5)
# print(list2)

def palindrome(s):
	mid = len(s)-1//2
	start = 0
	end = len(s)-1
	flag =0

	while(start < mid):
		if(s[start] == s[end]):
			start +=1
			end -= 1
		else:
			flag =1
			break;
	if flag == 0:
		print(f"the string {s} is a palindrome")
	else:
		print(f"the string {s} is not a palindrome")

# s = input("enter a string : ")
# palindrome(s)

def symmetrical(s):
	n = len(s)
	flag = 0

	if n % 2 :
		mid = n//2 +1
	else :
		mid = n//2

	start1 =0
	start2 = mid

	while(start1 < mid and start2 < n):
		if(s[start1] == s[start2]):
			start1 =start1 +1
			start2 = start2+1

			flag = 1;
			break;

	if flag == 0:
		print(f"The string {s} is symmetrical")
	
	else:
		print(f"The string {s} is not symmetrical")
# s = input("enter a string")
# symmetrical(s)

def reverse_words_in_string(s):
	list1 = s.split(" ")
	
	reversed_words = " ". join(reversed(list1))
	print(reversed_words)

# reverse_words_in_string("geeks quiz practice code")

class Stack():
	def __init__(self):
		self.items =[]

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def get_stack(self):
		return self.items
# s = Stack()

# s.push("A")
# s.push("B")
# s.push("C")
# s.push("D")

# print(s.get_stack())

# s.pop()

# print(s.is_empty())

# print(s.get_stack())


class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def addItems(self,data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
			return

		lastNode = self.head
		while lastNode.next:
			lastNode = lastNode.next

		lastNode.next = newNode

	def prepend(self,data):
		newNode = Node(data)

		newNode.next = self.head
		self.head = newNode

	def insert_after_node(self,prev,data):
		newNode = Node(data)

		newNode.next = prev.next
		prev.next = newNode



	def removeItems(self):
		pass

	def printItems(self):
		curNode = self.head
		while curNode:
			print(curNode.data)
			curNode = curNode.next



# l = LinkedList()
# l.addItems("A")
# l.addItems("B")
# l.addItems("C")

# l.prepend("D")

# l.insert_after_node(l.head.next,"K")
	

# l.printItems()
















































































