a = (12,24,32)
b = (12,24,32)
c = a
print ('id of a {} and id of b {} and id of c {}'.format(id(a),id(b),id(c)))
print ('a is b ?',a is b)
print ('a is c ?',a is c)
print ('c is b ?',c is b)
# id of a 2175244150720 and id of b 2175244150720 and id of c 2175244150720
# a is b ? True
# a is c ? True
# c is b ? True

lst1 = [12,24,32]
lst2 = [12,24,32]
lst3 = lst2
print ('id of lst1 {} and id of b {} and id of c {}'.format(id(lst1),id(lst2),id(lst3)))
print ('lst1 is lst2 ?',lst1 is lst2)
print ('lst1 is lst3 ?',lst1 is lst3)
print ('lst3 is lst2 ?',lst3 is lst2) #This alone True
# id of lst1 2547477739136 and id of b 2547478147712 and id of c 2547478147712
# lst1 is lst2 ? False
# lst1 is lst3 ? False
# lst3 is lst2 ? True


a_var = 12
b_var = a_var 
print ('id of a_var', id (a_var))
print ('id of b_var', id (b_var))

b_var = 23
print ('a_var',a_var) #If value of b_var changes , it will not have an impact on a_var
# id of a_var 1302379850384
# id of b_var 1302379850384
# a_var 12

a_var1 = 12
b_var1 = a_var1 

a_var1 = 14
print ('b_var1 is ', b_var1)
print ('id of a_var1', id (a_var1))
print ('id of b_var1', id (b_var1))
# b_var1 is  12
# id of a_var1 1302379850448
# id of b_var1 1302379850384



list_inp1 = [24,36,58]
list_inp3 = list_inp1

list_inp1[1] = 74
print ('list_inp3 is after list_inp elelment is changed from 36 to 74',list_inp3)
#list_inp3 is after list_inp elelment is changed from 36 to 74 [24, 74, 58]
list_inp3.append(56)
print('list_inp1 After appending element to lst3',list_inp1)
# list_inp1 After appending element to lst3 [24, 74, 58, 56]



list_inp1 = [24,36,58]
list_inp3 = list_inp1

list_inp1[1] = 74
print ('list_inp3 is after list_inp elelment is changed from 36 to 74',list_inp3)
#list_inp3 is after list_inp elelment is changed from 36 to 74 [24, 74, 58]
list_inp3.append(56)
print('list_inp1 After appending element to lst3',list_inp1)
# list_inp1 After appending element to lst3 [24, 74, 58, 56]

elm = dict (zip(('a','b','c','d'),(1,2,3,4)))
print (elm)

#While looping dict we will get keys by default
sd = [x for x in elm]
print (sd)

print ('a' in sd)
#/......................................................................................................

import copy
lst = [ [1,2,3,4],5,6,8]
lst_2 = lst
print ('id of the lst', id (lst)) #1241550963136
print ('id of the lst_2',id (lst_2))

lst_3 = copy.copy(lst)
print ('id of the lst_3', id(lst_3)) #2673653999808

lst_4 = copy.deepcopy(lst)
print ('id of the lst_4',id(lst_4)) #2673654072512

print ('id of lst[]0',id(lst[0])) #2214293039168

print ('id of lst_3[0]',id(lst_3[0])) #2214293039168
 
print ('id of lst_4[0]',id(lst_4[0])) #2214293051136
lst_3 [3] = 20
print ('lst after change',lst)
print ('lst_3 after change ',lst_3)

#Here the value is not updated in lst , since those values will not reflect

lst_3 [0][1] = 250
print ('lst after change in nested list ',lst)
print ('lst_3 after change in nested list  ',lst_3)

#Here the values of lst and lst_3 are changed 










