
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None

	def print_list(self):
		curnode = self.head
		while curnode:
			print(curnode.data)
			curnode = curnode.next

	def append(self,ele):
		newnode = Node(ele)

		if self.head is None:
			self.head = newnode
			return
			
		lastnode = self.head
		while lastnode.next:
			lastnode = lastnode.next
		lastnode.next = newnode

	def prepend(self,ele):
		newnode = Node(ele)
		curnode = self.head

		self.head = newnode
		newnode.next = curnode

	def insert_after_node(self,prenode,data):
		if not prenode:
			print("Previous node is not in the list")
			return

		newnode = Node(data)

		newnode.next = prenode.next
		prenode.next = newnode

	def delete_node(self,key):
		curnode= self.head

		if curnode and curnode.data == key:
			self.head = curnode.next
			curnode = None
			return
		prev = None
		while curnode and curnode.data != key :
			prev = curnode
			curnode=  curnode.next

		if curnode is None:
			return
		prev.next = curnode.next
		curnode =None
	def del_node_at_pos(self,pos):
		curnode = self.head
		
		if pos == 0:
			self.head= curnode.next
			curnode= None
			return
		prev = None
		count = 1
		while curnode and count != pos:
			prev = curnode
			curnode = curnode.next
			count +=1

		if curnode is None:
			return

		prev.next = curnode.next
		curnode = None


	def reverse(self):
		curnode = self.head
		prev = None

		while curnode:
			nxt = curnode.next
			curnode.next = prev
			prev = curnode # c
			curnode = nxt # D




l = Linkedlist()

l.append("A")
l.append("B")
l.append("C")
l.append("D")

l.prepend("K")
l.append("X")
l.append("Y")
l.append("Z")

l.insert_after_node(l.head.next.next,"S")

l.del_node_at_pos(6)

l.print_list()








