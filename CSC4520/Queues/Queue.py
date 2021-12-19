class Queue:
  
	def __init__(self):
		self.queue = []
	
  def enqueue(self, elem):
		self.queue.append(elem)
	
  def dequeue(self):
		if(len(self.queue == 0)):
      return "Queue is empty!"
    return(self.queue.pop(0))

  def peek(self):
		return(self.queue[0])
	
  def elems(self):
		return(self.queue)
	
  def length(self):
		return(len(self.queue))
