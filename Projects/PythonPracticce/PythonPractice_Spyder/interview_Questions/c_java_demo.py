# input:  is_valid_number (c++)
# output: isValidNumber (Java)

def func(input1):
    pass
    # c_plus = False
    # if '_' in input1:
    #     c_plus = True
    
    # out_str = ""
    # if c_plus:
    #     set_upper = False
    #     for ch in input1:
    #         if ch == '_':
    #             set_upper = True
    #         else:
    #             if set_upper:
    #                 ch= ch.upper()
    #             out_str = out_str + ch
    #             set_upper = False
    # else:
    #     # for ch in input1:
    #         if ch.isupper():
    #             out_str = out_str + '_'
    #         out_str = out_str + ch.lower()
                
    # print (out_str)    
    # print (c_plus)
    
inp = "is_valid_number"
inp2 = "myJavaProgram"
func (inp2)

#Above method will tell us we don't have knowledge on built in functions 
# Use split + Join + Title for snakeCase to CamelCase 
words = inp.split('_')
cam_case = words[0]+"".join([x.title() for x in words[1:]])
print (cam_case)