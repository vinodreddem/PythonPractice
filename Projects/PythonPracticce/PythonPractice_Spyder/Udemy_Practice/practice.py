# import time
# import threading

# # def funct_for_thread(x,y):
# #     z = x+y
# #     print (z)
# #     time.sleep(3)
# #     print (z +5 )

# # create_thread = threading.Thread(target= funct_for_thread, args=(7,8))
# # create_thread.start()
# # print ("In Main Thread")

# def add(z :int, y :int) -> int:
#     return z+y+0.5

# print(add(3,5))

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next=None
        
# class LinkedList(Node):
#     def __init__(self):
#         self.head = None

# lsc = LinkedList()
# lsc.head = Node(4)
# lsc.sec = Node(3)
# lsc.third = Node(2)

# lsc.head.next = lsc.sec
# lsc.sec.next = lsc.third

class Person():
    def __init__(self,age,name):
        self.age = age
        self.name = name
        
    
    
per = Person(26,'John')
per.sex ='male'
print(hasattr(per,'sex'))

