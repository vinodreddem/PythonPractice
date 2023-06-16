def myFunction(parm):
    """ This is DocString of My function"""
    print('My First Function{}'.format(parm))
print(myFunction.__doc__)


def evenBool(num):
    return num%2==0

myList =[1,2,3,4,5,6,7,8,9,10]

even_numbers = filter(evenBool,myList)
print(list(even_numbers))
print('Id of ',id(myList))
print('Id of even_numbers',id(even_numbers))

#here filter is going `to pass each element of list to evalBool function
#evalBool function is going to return True if it is Even else False
#Filter function stores only True values in Even_Numbers variable 
#We need to conver that object into list to see

#Lambda Function
lambda num: num%2==1

odd_Number = filter (lambda num: num%2==1,myList)
print('Odd Numbers ',list(odd_Number))


#Check a list has [1,2,3] in sequence
# def arrayCheck(list_input):
#     length_list =len(list_input)
#     print ('length list_input is ',length_list)
#     for i in range(len(list_input)):
#         if list_input[i]==1:
#             if i+1<length_list:
#                 if list_input[i+1]==2:
#                     if i+2<length_list:
#                         if list_input[i+2]==3:
#                             return True
#     return False

def arrayCheck(list_input):
    length_list =len(list_input)
    print ('length list_input is ',length_list)
    for i in range(len(list_input)):
        if list_input[i]==1:
            if i+1<length_list and list_input[i+1]==2:              
                if i+2<length_list and list_input[i+2]==3:
               # if  list_input[i+2]==3 and i+2<length_list:
                    return True
                        
    return False

def arrayCheck1(list_input):
    length_list =len(list_input)
    print ('length list_input is ',length_list)
    for i in range(len(list_input-2)):
        if list_input[i]==1 and list_input[i+1]==2 and list_input[i+2]==3:
                    return True
                        
    return False

print(arrayCheck([1,2,3]))
print(arrayCheck([0,3,2,1]))
print(arrayCheck([1,2,0,1,2,3]))
                    
def end_other(input1,input2):
    len1 =len(input1)
    len2 =len(input2)
    print('len1 is',len1)
    print('len2 is',len2)
    if len1>len2:
        if input1[-len2:].lower()==input2.lower():
            return True

    elif len1<len2:
        if input1.lower() == input2[-len1:].lower():
            return True
    else:
        if input1.lower() == input2.lower():
            return True 

    return False

def end_other1(input1,input2):
    a = input1.lower()
    b =input2.lower()
    if a.endswith(b) or b.endswith(a):
        return True 
    return False

def end_other2(input1,input2):
    a = input1.lower()
    b =input2.lower()
   
    return a[-(len(b)):]==b or b[(len(-a)):]==a

print("End Other 1",end_other('HIaBc','abc'))
print("End Other 2",end_other('aBc','sgdsabc'))

def Double_Char(str_input):
    ret_st= str()
    for c in str_input:
        print ('C id ',c)
        print ('C** is ',c*2)
        ret_st += str(c*2)
        
    print('print(ret_st)',ret_st)
    return ret_st

print('Double Char is ',Double_Char('ABC'))