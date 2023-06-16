# Like arrays, Linked List is a linear data structure.
# Unlike arrays, linked list elements are not stored at a contiguous location; 
# the elements are linked using pointers.

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(): 
    def __init__ (self):
        self.head = None
            
    def ptint_linked_list_data(self):
        temp =  self.head
        while temp:
            print (temp.data) 
            temp = temp.next

    def insert_elm_first(self,data):
        new_Node = Node (data)
        new_Node.next = self.head
        self.head = new_Node

    def insert_elm_last(self,data):
        new_Node = Node(data)
        #We need to add last value of Linked list )(next to )New Node
        if self.head is None:
            self.head = new_Node
            return 
        n = self.head
        while n.next is not None:
            n = n.next
        
        n.next = new_Node
        
    def insert_elm_after_elm(self,elm,data):
        n = self.head
        while n is not None:
            if n.data == elm:
                break
            n = n.next
        if n is None:
            print ("Element is not present in the List")
        else:
            new_Node = Node(data)
            new_Node.next = n.next
            n.next = new_Node
            
    def insert_elm_before_elm(self,elm,data):
        if self.head is None:
            print("No elements in the List")
            return 
        if elm == self.head:
            insert_elm_first(data)

        n = self.head
        while n is not None:
            if n.data == elm:
                break
            n = n.next
        if n is None:
            print ("Element is not present in the List")
        else:
            new_Node = Node(data)
            new_Node.next = n.next
            n.next = new_Node
            
            
linked_list = LinkedList ()
linked_list.head = Node (4)
linked_list.second = Node (6)
linked_list.fifth = Node(3)

linked_list.head.next = linked_list.second
linked_list.second.next = linked_list.fifth

linked_list.ptint_linked_list_data()

#To -Be : Implement methods to Add elements at Begining , End and In Between
"""
Approach: To insert a given data at a specified position, the below algorithm is to be followed: 
 

Traverse the Linked list upto position-1 nodes.
Once all the position-1 nodes are traversed, allocate memory and the given data to the new node.
Point the next pointer of the new node to the next of current node.
Point the next pointer of current node to the new node. 
"""
#Inserting element at the begining
















