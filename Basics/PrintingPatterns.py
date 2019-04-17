#Print the below pattern

####
####
####
####

"""
Smart thinking -Over thinking
print('####')
print('####')
print('####')
print('####')
"""

i=4;
while i>0:
    j = 4
    while j>0:
        print ('#',end ="")
        j= j-1
    print()
    i =i-1

#Second way -using for loop with range function insted of the intail variables
for i in range(4):
    for j in range(4):
        print('#',end='')
    print()

# 2nd Pattern
"""
*
**
***
****
"""
for i in range(4):
    for j in range(4):
        if j>i :
            break
        print('*',end='')
    print()

# Second way of printing above pattern
for i in range(4):
    for j in range(i+1):
        print('*',end='')
    print()

#3rd Printing Pattern
"""
      &
     &&
    &&&
   &&&&
  &&&&&   
"""

for i in range (6):
    for j in range (5,-1,-1):
        if j>i :
            print (end=" ")
        else :
            print('&',end='')
    print()



#4th Pattern

"""
&&&&
&&&
&&
&
"""

"""
for i in range (5):
    for j in range (5):
        if j<=i :
            print (end="")
        else :
            print('&',end='')
    print()

"""
