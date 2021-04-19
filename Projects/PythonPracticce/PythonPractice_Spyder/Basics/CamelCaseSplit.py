

# Python3 program Split camel case  
# string to individual strings 
  
def camel_case_split(str): 
    words = [[str[0]]] 
    print ('Words are ',words)
    for c in str[1:]: 
        if words[-1][-1].islower() and c.isupper(): 

            words.append(list(c)) 
        else: 
            words[-1].append(c) 
        print ('Words are ',words)
    for word in words:
        print ('word is',word)
    return [''.join(word) for word in words] 
      
# Driver code 
str = "GeeksForGeeks"
print(camel_case_split(str)) 