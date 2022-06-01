import ctypes

"""This is supposed to be an implementation of a Dynamic-Array/ArrayList in Python."""

class ArrayList(object):
    """An arraylist is almost the same as an array, but its size can be modified at runtime. It does not need a fixed size at initialization.
    To keep a method private, we can use the '_' sign before the name."""

    def __init__(self):
        self.elems = 0 # The number of elements in the array, set to 0 by default
        self.cap = 1 # This is the maximum capacity of elements in the arraylist. However, it will be resized as needed.
        self.arr = self.make_array(self.cap) # This creates an array with the 'cap' elements

    def __len__(self):
        # This will return the number of elements in the arraylist
        return self.elems

    def full_l(self):
        return self.cap

    def __getitem__(self, ind):
        """Return the element at the specific index"""
        # This checks for the validity of the index. If it is invalid, it returns an error statement.
        if not 0 <= ind <= self.cap:
            return IndexError(f"Bad index. It is out of bounds. Try something between 0 and {self.cap-1}.")
        # Returns the right element if the index is in bound
        return self.arr[ind]

    def add(self, element):
        """Add an element to the end of the arraylist"""
        if self.elems == self.cap:
        # If there is not enough room in the arraylist, we increase its size by half of the current size.
            self._resize((self.cap * 3)//2 + 1)
        # Here, we added an element to the end of the arraylsit and increased its elements by 1
        self.arr[self.elems] = element
        self.elems += 1

    def add_at(self, ind, element):
        """This method is supposed to add an element at any given index in the arraylist"""
        # This checks if the index is valid
        if not 0 <= ind < self.cap:
            return IndexError(f"Bad index. It is out of bounds. Try something between 0 and {self.cap-1}.")
        # This is to resize array if the arraylist is full
        if self.elems == self.cap:
        # This resizes the array if it is full, by increasing the arraylist's capacity by half of the existing size
            self._resize((self.cap * 3)//2 + 1)
        # Now, the elements must be added
        for inde in range(self.elems-1, ind-1, -1):
            self.arr[inde+1] = self.arr[inde]
        self.arr[ind] = element
        self.elems += 1

    def remove(self):
        """This method is supposed to remove the last element in the arraylist"""
        if self.elems == 0:
            return "You cannot delete anything from an empty array"
        self.arr[-1] = 0
        self.elems -= 1
    
    def remove_at(self, ind):
        """This is to remove element from a specific index"""
        if self.elems == 0:
            return "You cannot delete anything from an empty array"
        if ind < 0 or ind > self.elems-1:
            return "Index is invalid, you cannot delete that specific index"
        if ind == self.elems-1:
            self.arr[ind] = 0
            self.elems -= 1
            return
        for each in range(ind, self.elems-1):
            self.arr[each] = self.arr[each+1]
        self.arr[self.elems-1] = 0
        self.elems -= 1

    def _resize(self, capacity):
        """Resize the array to new capacity"""
        new_arr = self.make_array(capacity)
        for each in range(self.elems):
            new_arr[each] = self.arr[each]
        self.arr = new_arr
        self.cap = capacity

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

if __name__ == '__main__':
    array = ArrayList()
    array.add(0)
    array.add(10)
    array.add_at(1, 12)
    array.add_at(2, 123)
    array.add_at(3, 1234)
    array.remove()
    array.remove_at(2)
    print(array.full_l())
    for each in range(len(array)):
        if array[each] == None:
            print(0)
        else:
            print(array[each])
