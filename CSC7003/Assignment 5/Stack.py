class Stack:
    def __init__(self):
        self.data = []
    def __str__(self):
        ret = ""
        for i in self.data:
            ret += i
        return(ret)
    def __len__(self):
	    return(len(self.data))
    def is_empty(self):
        return(len(self.data) == 0)
    def push(self, e):
        self.data.append(e)
    def top(self):
        if(self.is_empty()):
            return("Stack is empty!")
        return(self.data[-1])
    def pop(self):
        if(self.is_empty()):
            return("Stack is empty!")
        return(self.data.pop())