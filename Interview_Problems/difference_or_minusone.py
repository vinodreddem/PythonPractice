# Input list and Output list  --
list_input = [2,4,12,6,2,9,10]
# out_put = [2,8,-1,3,7,1,-1] 

def getdifference(lst_in):
    
    out_lst = []
    for i in range(len(lst_in)):
        is_greater_elm_exists = False
        print (i)
        for j in range (i+1,len(lst_in)):
            if lst_in[i] < lst_in [j]:
                elm = lst_in[j] - lst_in[i]
                out_lst.append(elm)
                is_greater_elm_exists = True
                break
        print (is_greater_elm_exists)
        if is_greater_elm_exists == False:
            out_lst.append(-1)
    return out_lst

print (getdifference(list_input))
