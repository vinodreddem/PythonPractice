"""
Composition is a concept that models a has a relationship.
 It enables creating complex types by combining objects of other types.
 This means that a class Composite can contain an object of another class Component.
 This relationship means that a Composite has a Component.
"""
# Composition --Part Of Relation Ship--- is represented through a line with a diamond at the composite class pointing to the component class.
#  The composite side can express the cardinality of the relationship. 
# The cardinality indicates the number or valid range of Component instances the Composite class will contain.
# Say suppose we have a Employee and Salary classes--Can we apply Inheritence Here?
# No --Salry is not a Employee and Employee is not a Salary
# SO here we can use a composition relationship between Employee and Salary ---Employee class deligates some responibilities to Salary Class
# Salary is part of Employee 

class Salary():
    def __init__(self,pay,bonus):
        self.pay =pay
        self.bonus =bonus
    
    def Annual_Salary(self):
        return (self.pay*12)+self.bonus 

class Employee():
    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age =age
        self.obj_Salary =Salary(pay,bonus)

    def total_salary (self):
        return self.obj_Salary.Annual_Salary ()

emp = Employee("Vinod",30,15000,15000)
print("Employee Salary",emp.total_salary())

# Aggregation - HAS-A ---Instead of creation of the Salary class inside the Employee class, 
# We will create Salary class and we will pass that as an attribute to Employee class
# & Employee class has the salary object as an attribute

class Employee2 ():

    def __init__(self,name,age,salary):
        self.name = name
        self.age =age
        self.obj_Salary =salary

    def total_salary (self):
        return self.obj_Salary.Annual_Salary ()

salary =Salary (15000,15000)
emp2 = Employee2("Avi",24,salary)

print("Employee2 Salary",emp.total_salary())
#-----------------------------------------------------------------------------------------------------------------
#       Composition                                                                     Agreegation
#-----------------------------------------------------------------------------------------------------------------
# 1.    Salary is part of Employee (Part od Relationship)     1.Employee has a Salary (HAS A Relationship)
# 2.    If Employee Object deletes automatically              2. Both objects are individual If we delets one
#       Salary object is going to delete(Inter dependence)       Another is not going to delete. (Uni directional)
# ------------------------------------------------------------------------------------------------------------------