import array as arr

"""
Array:

1.Array is used to store the same type of data , We can not store the elements of different data types.
2.To create an array we need to import the array module.
3. While creating an arrray we need to mention the data type by using type code.
    Every data type has unique type code.
    
Type Code :
    Type Code     C -Type      Python Type         Min Size in bytes 
    ---------   ----------   --------------     ---------------------
    b           -Signed Char    -int                  1
    B            Unsigned Char   int                  1
    u            py-UNICODE      unicode character    2
    h            signed short    int                  2
    H            Unsigned short  int                  2
    i            signed int      int                  2
    I            Unsigned int    int                  2
    l            signed long     int                  4
    L            Unsigned Long   int                  4
    f            float           float                4
    d            double          float                8
"""

vals = arr.array('I',[1,5,6,88])
print (vals)

"""
1. vals = arr.array('i',[1,5,6.5,8]) 
---------------------------------
Traceback (most recent call last):
array('I', [1, 5, 6, 88])
  File "C:/Users/Sanvi/PycharmProjects/PracticePython/Basics/Python_ApplicationPrograamming_Package/ArrayDemo.py", line 16, in <module>
    vals = arr.array('i',[1,5,6.5,8])
TypeError: integer argument expected, got float

2. vals = arr.array('I',[1,5,6,8,-8])
---------------------------------
Traceback (most recent call last):
  File "C:/Users/Sanvi/PycharmProjects/PracticePython/Basics/Python_ApplicationPrograamming_Package/ArrayDemo.py", line 13, in <module>
    vals = arr.array('I',[1,5,6,8,-8])
OverflowError: can't convert negative value to unsigned int
"""

uniarra = arr.array('u',['vinod' ,'vijay'])
print("uniarra",uniarra)  
"""
functions of Array:

1, buffer_info : this will give you the address and size (64658224, 4) in the tuple
"""

print(vals.buffer_info()) #(64658224, 4)

val2 = arr.array(vals.typecode , (a*2 for a in vals))
print(val2)

"""
Accessing elements from Array :
1.Usinf for loop with index 
2.Using for loop with val directle
3.Even it is possible with while loop , but we need to intialaise and check condition and increment the value
"""

for a in range(len(val2)):
    print (val2[a])

val2.
for e in vals:
    print (e)

i =0
while i< len(vals) :

    print (i)
    print (vals[i])
    i+=1

"""
Traceback (most recent call last):
  File "C:/Users/Sanvi/PycharmProjects/PracticePython/Basics/Python_ApplicationPrograamming_Package/ArrayDemo.py", line 58, in <module>
(60070720, 4)
    val2(0) ----If we use open brackets insteead of squre brackets
array('I', [2, 10, 12, 176])
TypeError: 'array.array' object is not callable
    
    """