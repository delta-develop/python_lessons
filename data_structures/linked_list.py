
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next_node = None


class SingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_node
    
    def insert(self,data,location=0):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next_node = self.head
                self.head = new_node
            elif location == -1:
                self.tail.next_node = new_node
                self.tail = new_node
            else:
                current = self.head
                index = 0
                while index < location - 1:
                    current = current.next_node
                    index += 1
                    if current is None:
                        self.tail.next_node = new_node
                        self.tail = new_node
                
                next_node = current.next_node
                current.next_node = new_node
                new_node.next_node = next_node
                if current == self.tail:
                    self.tail = current
    
    def insert_beginning(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
    
    def insert_end(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
    
    def insert_position(self,node,position):
        current = self.head
        for index in range(position):
            current = current.next_node
            
            if current == None:
                raise Exception("Out of bounds")

            
        node.next_node = current
        
        
            
            
    def print_ll(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next_node
            
        print("end")
    
    
        

lst = SingleLinkedList()
node1 = Node(1)
node2 = Node(2)

lst.insert_beginning(node1)
lst.print_ll()
lst.insert_end(node2)
lst.print_ll()
