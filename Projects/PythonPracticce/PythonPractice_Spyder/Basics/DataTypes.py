
#-----------------------------------------------------------------------------
"""
Number data:
1.Integer :We have a value upto 15 digits
2.Float :decimal point can accurate upto 15 places
3.Complex :imag and real are the attributes to represent complex

Difference between List ,Tuple, Set ,Dictionaries,String
List :
    1.list is ordered list
    2.list have different data types
    3.We can use slicing to fetch the data from list
    4.list is mutable , We can change the values of the list
    5.Denoted by squre brackets []

Tuple:
    1.Tuple is same as of the list , difference is it is immtable
    2.denoted by open brackets ()

Set :
    1.Set is unordered list
    2.Set has unique values
    3.Set is mutable
    4.No slicing concept here, since there is No indexing
    5.So we are using the methods like Add , update etc.. to change the values in Set
    6.denoted by the curly brackets {}

Dictionaries :
    1.Normally used for large data
    2.Key -Value pair
    3.denoted inside the curly braces {}

String:
    1.strings represented inside the " ...." or '.....'
    2.Multiline strings can be expressed using triple quotes
"""
#-----------------------------------------------------------------------------

#Numeric data

number_int =5
number_float=5.6666666666666677598758857488
print(number_float) #it will print only 15 digits
number_complex =5+6j
com =complex(4,6)
print(com)
#number_complex2 =5+4i --------We can not use the i for complex numbers in python, We use only j
print(number_complex.real ,number_complex.imag)

#List

list_example =[1,2,5,6,3,8,8,4,3,4,'vinod',"vijay",2+8j]
print(list_example) # It will print the data in the ordered list

print(list_example[6:])
"""print(list_example[55]) #Throw an Error - IndexError: list index out of range """
print(list_example[:4])
print(list_example[3:5])
print(list_example[11])
list_example[11]="Ajay" #--------->List is mutable getting value is changes
print(list_example[11])

#Tuple

tuple_example =(3,6,43,2,8,10,5,3,6+8j,"vijay")
print("Print the Tuple " ,tuple_example) # It will print the data in the ordered list
print(tuple_example[:7])
""" tuple_example[4]=5 ----->THrow an Error  : TypeError: 'tuple' object does not support item assignment """

#Set
set_example = {4,6, 2,4,6,8+7j,"Ajay","vnod","Ajay"}
print("Set Explme --",set_example)
""" print(set_example[5]) ---->Throw an Error :TypeError: 'set' object does not support indexing """

#Dictionaries



dict_example = {2:5,"vinod":5,"vijay":6 ,6:"Ajay"}
print(dict_example)
""" print(dict_example['VIJAY']) #KeyError: 'VIJAY' """
#The keys are case senstive , we need to use the existing keys only

dict2 = {1:'vinod',2:'vijay',2:'ajay'}
print(dict2.keys())
print(dict2.values())
# Here we will get only vinod and ajay as values , since we are overriding the value of vijay with ajay
#String

str_example = "This is the string representation in the python"
print("String Example ---", str_example)

print(int(True))
print(int(False))
