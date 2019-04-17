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