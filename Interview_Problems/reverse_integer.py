quotent = 123653
out = ''
while quotent > 10:
    quotent, reminder = divmod(quotent,10)
    print(quotent,reminder)
    out = out + str(reminder)
    if quotent < 10:
        out = out + str(quotent)
    
print (out)
exponent = 0
quotent = 123653

out = 0
while quotent > 10:
    quotent, reminder = divmod(quotent,10)
    print(quotent,reminder)
    out = (out *  10) + (reminder )
    if quotent < 10:
       out = out * 10 + quotent
    print (out)
print (out)

#Swecond method
str_inp = str (quotent)
out_inp = str_inp[::-1]