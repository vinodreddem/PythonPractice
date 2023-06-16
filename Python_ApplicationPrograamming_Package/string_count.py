in_str = 'aabbcdd'
out_str = ''
for i in in_str:
    if i not in out_str:
        char_cnt = i+str(in_str.count(i))
        out_str = out_str+str(char_cnt)
print(out_str) 

