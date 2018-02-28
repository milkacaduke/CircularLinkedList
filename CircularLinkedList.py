
class LLNode(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None


class CircularSinglyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, data):
		self.insert_front(data)

	def insert_front(self, data):
		if data is None:
			return

		new_node = LLNode(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			new_node.next = self.head
		else:
			new_node.next = self.head
			self.tail.next = new_node
			self.head = new_node

	def print_all(self):
		if self.head is None:
			return

		cur_node = self.head
		i = 0

		print("")
		print("[head]")
		print("   v")
		print("   ", end="")
		while cur_node and cur_node != self.tail:
			print(cur_node.data + " -> ", end="")
			cur_node = cur_node.next
			i += 1
		# left with self.tail
		if cur_node:
			print(cur_node.data)
			i += 1

		if i <= 1:
			return

		FRONT_BUFFER = "   ^"
		FRONT_BUFFER2 = "   |"
		ONE_ELM_BUFFER = "     "
		ONE_ELM_BUFFER2 = "    |"
		ONE_ELM_BUFFER3 = "_____"
		ONE_ELM_BUFFER4 = "____|"
		
		builtString = FRONT_BUFFER
		builtString2 = FRONT_BUFFER2
		for k in range(i-2):
			builtString += ONE_ELM_BUFFER
			builtString2 += ONE_ELM_BUFFER3
		builtString += ONE_ELM_BUFFER2
		builtString2 += ONE_ELM_BUFFER4
		print(builtString)
		print(builtString2)




# main stuff
cll = CircularSinglyLinkedList()
cll.insert("A")
cll.insert("B")
cll.insert("C")
# cll.insert("D")
# cll.insert("E")
cll.print_all()




