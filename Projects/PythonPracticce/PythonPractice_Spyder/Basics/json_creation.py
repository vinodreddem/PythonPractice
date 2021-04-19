import json 
import requests
#convert Json Object into dictionary 

dict_inp = {
    "ID":10,
    "name":'Vinod',
    "college":'SVCET',"Add":'dvdsbvdfvd'
}

#creation of Json Object 
json_obj = json.dumps(dict_inp, indent = 5,sort_keys=True)
print("json_obj is ", json_obj)
print('Type of Json Object', type(json_obj)) #<class 'str'>

tup_inp = (23,45,'vinod')
# tup_inp = [23,45,'vinod']
json_tup = json.dumps(tup_inp)
print("Type of json_tup is ",type(json_tup)) #<class 'str'>
print ("json_tup is ",json_tup) #[23, 45, "vinod"]

#Deserializing of Json 
dat_des = json.loads(json_obj)
print(dat_des)
print('type of dat_desis ',type(dat_des)) #<class 'dict'>

json_tup_desrlz = json.loads (json_tup)
print(json_tup_desrlz) #[23, 45, 'vinod']
print('type of json_tup_desrlz ',type(json_tup_desrlz)) #<class 'list'>
# Tuple --- > Array ----> List , so inorderto get the tuples then we need to use tup() function

with open("C:/Users/Sanvi/Desktop/Python/data_jsonfile.json",'w') as write_file:
    json.dump(dict_inp,write_file) #it willcreate a json file in mentioned path
   
#    json.dump(json_tup,write_file) #--it will store data into the file 
   # but we were not able to deserialize the data 
   
#      File "c:\users\sanvi\appdata\local\programs\python\python39\lib\json\decoder.py", line 340, in decode   
#     raise JSONDecodeError("Extra data", s, end)
#     json.decoder.JSONDecodeError: Extra data: line 1 column 69 (char 68) 
# """
    
#Read json file data 
with open("C:/Users/Sanvi/Desktop/Python/data_jsonfile.json",'r') as read_file:
    data_desreailize = json.load(read_file)
    print (data_desreailize)
    print (type(data_desreailize)) #<class 'dict'>
    

