lst = [(12,34,54),(23,56,78)]
print (lst)

lst[0] = 15
#lst [1][2]= 14  #TypeError: 'tuple' object does not support item assignment
# list is used to assign multiple variables in a single list
#list is a type of an array , declared by [] brackets

nums = [34,65,78,98,44,67]

print(nums)
#we can get the elements from list by using the index
print(nums[1])
print(nums[4])
print(nums[-3])
print(nums[2:4])
print(nums[3:])
print(nums[:3])

#we can assign a Strings as well in the list

names =['vijay','ashok','vinod','vishnu']
print(names)

#assign multiple lists into a single list
mul = [nums,names]
print(mul)

#we can assign strings and num into a single list as well
mixed =[58.89,'Vijay',56]
print (mixed)

#operations performed on list

#1.Append the values to a list at last
nums.append(5)
print(nums)
#insert at specific place
nums.insert(2,56)
print(nums)

#remove the specified element from teh list
#nums.remove(55)
#If value is not there and we are trying to remove the element then
#we will get the Error names ValueError

nums.remove(65)
print(nums)

#we can perfotm Max,Min ,Count ,Sum operations on list
print(min(nums))
print(sum(nums))
print(max(nums))

#we can delete number based on the index , we can use the pop method
nums.pop(2)
print(nums)

#Tuple
#is same as list but we can't change the values
#So we can iterate the values fastly
#tuple uses () to indicate

tup =(45,'ajay',66.7)
print(tup)

pair_tuple = ((1,4),(4,6),(6,7))

y = (7)
print (type (y)) # <class 'int'>

#here we are defined Y as tuple with single element but the Python interpreter will automatically removes () and make it as Integer
#So inorder to define tuple with single element we need to ass comma in the last 
z = (5,)
print (type(z))
for tuple_q in pair_tuple:
    print('tuple in pair is ',tuple_q)

for (tup1,tup2) in pair_tuple:
    print ('tup 1 is ',tup1)
    print ('tup 2 is',tup2)

    """
    pair_tuple = ((1,4),(4,6),(6,7,1))
    Traceback (most recent call last):
      File "c:/PythonPracticce/PythonPractice_Spyder/List_demo.py", line 68, in <module>
    for (tup1,tup2) in pair_tuple:
    ValueError: too many values to unpack (expected 2) # 6,7,1)
    """

#if we try to assign a value then we will type Error for tuples

#Set
#Set is used to indicate te unique elements , we don't have multiple values
#it is using has concept , so we can't get teh elements in sequence
#SO we don't have a concept of the index
#for representation of sets we are using the {} braces

set1= {45,67,99,66,67,45}
print(set1)

#set1[2]---->TypeError: 'set' object does not support indexing
#we can perform all operations for sets as well


#Dictionary :[Mapping]
#dictionary has the key ,value pair
d ={"Vinod":"TCS", 'vijay':'Hexaware','Ashok':"HP","Vishnu":"Accenture"}
# :--->used to group the key value pair and ,--->used to differentiate different key value pair

print(d)
#get key and values from the dictionary
print(d.keys())
print(d.values())

print(d.get('Vinod'))#if we don't find the key in the dictionary , then we didn't raise any error , we simply return null value.

e ={"Vinod":"TCS", 'vijay':'Hexaware','Ashok':"HP","Vishnu":"Accenture","Vinod":"CapGemini"}
print(e)
#here we are ovverriding the value of the Key called "vinod" by the value CapGemini

