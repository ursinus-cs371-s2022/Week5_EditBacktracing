class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # Python's version of "null" is "None"
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.N = 0
     
    def add_first(self, value):
        """
        Parameters
        ----------
        value: any
            Add a new node to the beginning with this value
        """
        new_node = Node(value)
        head_before = self.head
        self.head = new_node
        new_node.next = head_before
        self.N += 1
     
    def remove_first(self):
        """
        Remove and return the first value from the linked list
        or do nothing and return None if it's already empty
        """
        ret = None
        if self.head: # If the head is not None
            ret = self.head.value
            self.head = self.head.next
            self.N -= 1
        return ret
    
    def peek_first(self):
        ret = None
        if self.head:
            ret = self.head.value
        return ret
         
    def __str__(self):
        # This is like the to-string method
        s = "LinkedList: "
        node = self.head
        while node: #As long as the node is not None
            s += "{} ==> ".format(node.value)
            node = node.next
        return s
     
    def __len__(self):
        # This allows us to use len() on our object to get its length!
        return self.N

class Stack:
    def __init__(self):
        self.L = LinkedList()
    
    def push(self, val):
        self.L.add_first(val)
    
    def pop(self):
        return self.L.remove_first()
    
    def peek(self):
        return self.L.peek_first()
    
    def get_entire_stack(self):
        node = self.L.head
        ret = []
        while node: #As long as the node is not None
            ret = [node.value] + ret
            node = node.next
        return ret