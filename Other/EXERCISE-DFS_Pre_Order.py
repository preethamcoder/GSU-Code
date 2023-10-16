class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        res = []
        def helpa(root):
            if root is None:
                return None
            res.append(root.value)
            helpa(root.left)
            helpa(root.right)
        helpa(self.root)
        return res

    def dfs_post_order(self):
        res = []
        def helpa(root):
            if root is None:
                return None
            helpa(root.left)
            helpa(root.right)
            res.append(root.value)
        helpa(self.root)
        return res
    
    def dfs_in_order(self):
        res = []
        def helpa(root):
            if root is None:
                return None
            helpa(root.left)
            res.append(root.value)
            helpa(root.right)
        helpa(self.root)
        return res






my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_in_order())
print(my_tree.dfs_pre_order())



"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 18, 27, 76, 52, 82]

 """

                

