lst = ['abt','bta','tab','bar','dsksllkd','tba']
print ('length of list is ',len(lst))
out_lst =[]
for i in range(len(lst)):
    fir_el = lst[i]
    grp_lst =[]
    grp_lst.append(fir_el)
    print ('fir_elis ',fir_el)
    print('I value is ',i)
    if i<len(lst)-1:        
        for j in range(i+1,len(lst)):            
            sec_el = lst[j]
            same_el = True
            for c in sec_el:                
                if c not in fir_el:
                    print ('C is ',c)
                    print ('Inside the If character not present')
                    same_el = False
                    break
            if same_el:                                
                print ('removed_element is ',sec_el)
                grp_lst.append(sec_el)
    out_lst.append(grp_lst)

print ('Out List is ',out_lst)
        
        
#Method 2 - We can Use dictionary concept
#Keep values in sorted order as Keys and append elements to a listed values
#Here for all elements we will have sorted Keys 
#lst = ['abt','bta','tab','bar','dsksllkd'] ---for abt, bta the key is abt like that for that key we will store all values

dict_in = {}

for i in range (len(lst)):
    j = "".join(sorted(lst[i]))
    
    if dict_in.get(j):
        x = dict_in.get(j)
        x.append(lst[i])
        dict_in[j]= x
    else :
        dict_in[j]= [lst[i]]    
        
print(dict_in.values())
    
