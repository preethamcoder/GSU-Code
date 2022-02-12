class module_one:
  def __init__(self, elem):
    self.lst = list(range(1, elem+1))
  
  def slice(self, size):
    if(size > len(self.lst) or size <= 0):
      return("The sub-list size cannot be larger than the list's size or less than 0! Please check values.")
    else:
      new_lst = self.lst[:size]
      return(new_lst)
