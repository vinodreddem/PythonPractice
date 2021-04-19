"""Questio-1 --- IMplement Linked List using Nodes"""
# Like arrays, Linked List is a linear data structure. Unlike arrays, 
# linked list elements are not stored at a contiguous location; the elements are linked using pointers.
lst =[]
lst.remove

""" Question 2:  Loop through the dictionary elements If value Exists Overide that one """

base_config = {
    "Location":'Asia/Chennai',
    "Constraints": {'One':'Primary Key','two':'Null' },
    "Names": {'first':'abc','last':'def' },
    'URLS':{
        'public':{
            'Best':'www.google.com',
            'Better':'www.yahoo.com',
            'Medium': 'StayAsItis',
            'ListWebSites':{'primary':'Yaahoo','secondary':'bingo'}
        }
    }
}


ovveride_config = {
    "Location":'Asia/Chennai',
    "Names": {'first':'fgh','last':'tre' },
    'URLS':{
        'public':{
            'Best':'www.dfbjhdfjvb.com',
            'Better':'www.dfhdv.com',
            'ListWebSites':{'primary':'Facebook','secondary':'Gmail'}
        }
    }
}


def ovveriteMethod (base_config, app_config):
    
    for k,v in app_config.items():
        
        print ('App Config Keys',k)
        if base_config.get(k):
                
            if isinstance(v,(dict)):
                ovveriteMethod (base_config.get(k),v)  
            else:
                base_config[k] = v   
    return base_config
                
print(ovveriteMethod (base_config,ovveride_config))
    
    
    