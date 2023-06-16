import math
"""
Dictionary :
1.unordered collection of items
2.key -value pair
3.Dictionaries are optimized to retrieve values when the key is known.
4.Creating a dictionary is as simple as placing items inside curly braces {} separated by comma.
    An item has a key and the corresponding value expressed as a pair, key: value.
5.{} or dict() used to create dictionary
6.values of any type and repeatable
7.keys -immutable type like String ,number and tuple -unique values

Link :https://www.datacamp.com/community/tutorials/python-dictionary-comprehension?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=278443377095&utm_targetid=aud-392016246653:dsa-473406574715&utm_loc_interest_ms=&utm_loc_physical_ms=9062136&gclid=CjwKCAjw7_rlBRBaEiwAc23rhiR1TiKJuXj0iUC2ABFGN875JFKkj_MOp89kUxvlt4ni0FH4WQyp7RoCFyEQAvD_BwE


"""

empty_dict ={}
print(type(empty_dict))

number_dict ={1:"vinod",2:[3,6,7]}
print(number_dict)

dict_dict =dict({"vinod":55,"vijay":56})
print(dict_dict)

dict_dict2 = dict([(1,"arju"),(2,"priya")])
print(dict_dict2)

"""
Access of Elements :
using key to access the elements
"""
print(number_dict[2])

#Looping Dictionaries
dict_1 = {'Key1':'Vinod',"vinod":55,"vijay":56,"List":[2,3,5,6],'dict':{'one':1,'two':2}}

for k in dict_1:
    print('Values in dict',k)
    #Automatically takes the Keys while looping dictionary

#To fetch both Keys and Values in dictionary we need to use items 
# Check is there any list or tuple or dict inside a dictonary values
bool_1 = False
for k,v in dict_1.items():
    print('Keys ',k)
    print ('Values',v)
    if isinstance(v,(list,dict,tuple)):
        bool_1=True
        break
print('bool_1 is ',bool_1)

"""
The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
The syntax of isinstance() is:
    isinstance(object, classinfo)
classinfo - class, type, or tuple of classes and types
"""

dict_1[('first_name','last_name')] = 789
print (dict_1)
print(dict_1['last_name'])


# Sorted the dict

# Switch - case Example

# Real time Example for Dict and use 

# Nested dict 

# Recursion Function and check the isinstance() operator.