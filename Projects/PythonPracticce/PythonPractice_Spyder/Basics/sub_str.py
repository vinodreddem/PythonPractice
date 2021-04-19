# Get all substring from a string
str_inp = "sdfsgb" 

lst_sub_str = []
for i in range (len(str_inp)):
    for j in range(i + 1, len(str_inp) + 1):
        lst_sub_str.append(str_inp[i:j])
        
def get_unique_substrings(str_inp):
    
    lst_sub_str = []
    for i in range (len(str_inp)):
        pre_substr = ""
        for j in range(i + 1, len(str_inp) + 1):
            if str_inp[j-1] in lst_sub_str[-1]:
               print (True)
               break
            lst_sub_str.append(str_inp[i:j])
            pre_substr = str_inp[i:j]
    return lst_sub_str
           
sub_str_list = get_unique_substrings("abcad")
longes_string = max(sub_str_list, key = len)
print (longes_string)
           