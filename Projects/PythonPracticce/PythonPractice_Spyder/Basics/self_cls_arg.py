""" 
self: Always use first argument to instance methods
cls : Always use as first argument fto class method
"""

class Demo():
    def insdtance_method (self,name):
        self.name = name
        
    @classmethod
    def class_method (cls,college):
        cls.college = college