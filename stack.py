# 顺序表实现栈

class stack(object):
	"""stack"""
	def __init__(self):
		self._list = []
	def push(self,item):
		self._list.append(item)
	def pop(self):
		return self._list.pop()
	def is_empty(self):
		return self._list == []
	def size(self):
		return len(self._list)
	def peak(self):
		if self._list:
			return self._list[-1]
		else:
			return None

if __name__ == '__main__':
	s = stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.size()
	print(s.pop())
	print(s.peak())

#------------------------------------------------------------
class queue(object):
	def __init__(self):
		self._list = []
	def enqueue(self,item):
		# self._list.append(item)  #尾部添加
		self._list.insert(0,item)  #头部添加
	def dequeue(self):
		return self._list.pop(0)  #头部弹出
		return self._list.pop()
	def is_empty(self):
		return self._list == []
	def size(self):
		return len(self._list)
#--------------------------------------------------------------------
class bequeue(object):
	def __init__(self):
		self._list = []
	def add_front(self,item):
		self._list.insert(0,item)  #头部添加
	def add_rear(self,item):
		self._list.append(item)  #尾部添加
	def pop_front(self):
		return self._list.pop(0)  #头部弹出
	def pop_rear(slef):
		return self._list.pop()
	def is_empty(self):
		return self._list == []
	def size(self):
		return len(self._list)
