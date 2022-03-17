class RENode:
  def __init__(self):
    self._operator = ''     # '*', '.', '+', 'leaf'
    self._symbol = ''       # only for leaf nodes
    self._position = 0      # only for non-^ leaf nodes
    self._lchild = None
    self._rchild = None     # only for . and +
    self._nullable = False
    self._firstpos = set()
    self._lastpos = set()

  def to_string(self,n):
    result = ' '*n
    if self._operator == 'leaf':
      result += 'SYMBOL: '+self._symbol
      result += ' NULLABLE='+str(self._nullable)
      result += ' FIRSTPOS='+str(self._firstpos)
      result += ' LASTPOS='+str(self._lastpos)+'\n'
    elif self._operator == '*':
      result += 'OPERATOR: STAR'
      result += ' NULLABLE='+str(self._nullable)
      result += ' FIRSTPOS='+str(self._firstpos)
      result += ' LASTPOS='+str(self._lastpos)+'\n'
      result += self._lchild.to_string(n+2)
    elif self._operator == '.':
      result += 'OPERATOR: DOT'
      result += ' NULLABLE='+str(self._nullable)
      result += ' FIRSTPOS='+str(self._firstpos)
      result += ' LASTPOS='+str(self._lastpos)+'\n'
      result += self._lchild.to_string(n+2)
      result += self._rchild.to_string(n+2)
    elif self._operator == '+':
      result += 'OPERATOR: PLUS'
      result += ' NULLABLE='+str(self._nullable)
      result += ' FIRSTPOS='+str(self._firstpos)
      result += ' LASTPOS='+str(self._lastpos)+'\n'
      result += self._lchild.to_string(n+2)
      result += self._rchild.to_string(n+2)
    else:
      result += 'SOMETHING WENT WRONG'
    print(result)
    return result

  def __str__(self):
    return self.to_string(0)
