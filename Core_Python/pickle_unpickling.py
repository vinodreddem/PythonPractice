import pickle


def pickling_data ():
    omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
    'age' : 21, 'pay' : 40000}

    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
    'age' : 50, 'pay' : 50000}
  
  
    #db
    db = {}
    db['omkar'] = omkar
    db['jagadish'] = Jagdish
    file_name =  open("C:/Users/Sanvi/Desktop/Python/data_pickle",'ab')  
    pickle.dump(db, file_name)   
    """
    Traceback (most recent call last):
    File "c:\Projects\PythonPracticce\PythonPractice_Spyder\Basics\pickle.py", line 30, in <module>     
    pickling_data()
    File "c:\Projects\PythonPracticce\PythonPractice_Spyder\Basics\pickle.py", line 17, in pickling_data
    pickle.dump(db, file_name)
    AttributeError: module 'pickle' has no attribute 'dump'

    Reason: Since I have named the module name as pickle.py -- so I am getting above error. 
    """ 
    file_name.close()
    
def read_picklie_data():
    read_file =  open("C:/Users/Sanvi/Desktop/Python/data_pickle",'rb')  
    data = pickle.load(read_file)
    
    print (data)
    
    read_file.close()
    

if __name__ == '__main__':
    pickling_data()
    read_picklie_data()    

    
    
    
    