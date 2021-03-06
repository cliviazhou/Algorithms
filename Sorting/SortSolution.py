class Sortsolution:
	arr = []
	def __init__(self, arr):
		self.arr = arr
	def printArray(self):
		print self.arr
	# -! selection sort...
	def selectsort(self):
		size = len(self.arr)
		for i in range(size - 1):
			flag = i
			for j in range(i + 1, size):
				if self.arr[j] < self.arr[flag]:
					flag = j
			self.arr[flag], self.arr[i] = self.arr[i], self.arr[flag]
	# -! insertion sort ...
	def insertSort(self):
		size = len(self.arr)
		for i in range(1, size):
			tmp = self.arr[i]
			for j in range(i-1, -2, -1):
				if tmp > self.arr[j]:
					break
				else:
					self.arr[j+1] = self.arr[j]
			self.arr[j+1] = tmp
	# -! bubble sort...
	def bubbleSort(self):
		size = len(self.arr)
		for i in range(size):
			for j in range(size-1, i, -1):
				if self.arr[j-1] > self.arr[j]:
					self.arr[j-1], self.arr[j] = self.arr[j], self.arr[j-1]
	# -! quick sort...
	def partition(self, start, end):
		i = start - 1
		pivot = self.arr[end-1]
		for j in range(start, end):
			if self.arr[j] < pivot:
				i += 1
				self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
		self.arr[i+1], self.arr[end-1] = self.arr[end-1], self.arr[i+1]
		return i+1
	def qsort(self, start, end):
		if start < end:
			part = self.partition(start, end)
			self.qsort(start, part)
			self.qsort(part+1, end)
	def quickSort(self):
		self.qsort(0, len(self.arr))
	# -! mergeSort...
  
#  ~Test example 
a = [2, 1, 32, 12, 9, 34, 4, 21]
s = Sortsolution(a)
s.quickSort()
s.printArray()
