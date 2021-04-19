""" Q. ABCDE --- Move 2 positions cyclic (Use Mod to length of string if Cyclic position is greater than length)
    Now result is ---CDEAB
    ABCDE
      CDEAB  
    """
    
str_o = "ABCDE"
    
str_part1 =  str_o [0:2]
    
str_part2 = str_o [2:]
str_output = str_part2 + str_part1
    
print (str_output)

# Say we need to moe 8 poistions then we can not use slice directly ,then we need to use Mod i.e.  8/5 ---3 
# So we need to use str_o[0;3]

