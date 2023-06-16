"""
is Operator : Checks the identity of Two Objects
== Operator : Checks the attributes of Two Objects 
"""

a = [1,2,3]
b =a 

print ('Ids of A {} and of B {}'.format (id(a),id(b))) #2003638973760

print ('Result of a==b is',a==b)
print ('Result of a is b is',a is b)

c = list (a)

print ("Id of C is ",id (c)) #1946617718784
print ('Result of a==c is',a==c)
print ('Result of a is c is',a is c)
