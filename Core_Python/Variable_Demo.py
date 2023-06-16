x=6;
y=5
print(x+y)

#The _ will holds the last output of operation,
#this will work only in python shell
#z =_+7
#print(z)
#we did not defined , so we will get an excpetion called Name Error



str = "YOUTUBE"
#Str starts from 0 to end , say suppose
# Y  O  U  T  U  B  E
# 0  1  2  3  4  5  6
#-7 -6 -5 -4 -3 -2 -1

#print one char in a string
print(str[4])
print(str[-4])

#print multiple char in a string
print(str[1:4])

#here 1 -- Start index it is inclusive
#4 is end index ---which is exclusive
print (str[1:])

#here end index is not mentioned , so it will automatically takes end index as last
print(str[:5])

#same as above

print('str[:25] is',str[:25])

#Here we are giving outof range index , the string does not have
#25 characters , But we are giving as 25 char
#unlike in java , we are not getting any exception here , if it is in java we were
#getting Arrayindexoutofrange exception something like that


#If we want to modify the string say supppose
str[1:3]="MY"

#Traceback (most recent call last):
#  File "C:/Python3.4/MyScripts/Variable_Demo.py", line 44, in <module>
#    str[1:3]="MY"
#TypeError: 'str' object does not support item assignment

print(str) # This will not execute ,since we got an exception in the
#above sentence.





