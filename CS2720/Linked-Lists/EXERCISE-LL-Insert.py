class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        elem = Node(value)
        if index == 0:
            self.prepend(value)
        elif index > 0 and index < self.length:
            curr = 0
            tmp = self.head
            while curr < index-1:
                tmp = tmp.next
                curr += 1
            elem.next = tmp.next
            tmp.next = elem
            self.length += 1
        elif index == self.length:
            self.append(value)
        else:
            return "Foul"

my_linked_list = LinkedList(1)
my_linked_list.append(3)


print('LL before insert():')
my_linked_list.print_list()


my_linked_list.insert(1,2)

print('\nLL after insert(2) in middle:')
my_linked_list.print_list()


my_linked_list.insert(0,0)

print('\nLL after insert(0) at beginning:')
my_linked_list.print_list()


my_linked_list.insert(4,4)

print('\nLL after insert(4) at end:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before insert():
    1
    3

    LL after insert(2) in middle:
    1
    2
    3

    LL after insert(0) at beginning:
    0
    1
    2
    3

    LL after insert(4) at end:
    0
    1
    2
    3
    4

"""