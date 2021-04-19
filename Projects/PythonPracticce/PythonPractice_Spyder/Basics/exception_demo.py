# try:
#     x = 10/3
# except (RuntimeError, ValueError, SyntaxError):
#     print("Error Occured") 
# finally:
#     print('Always Exxecutes')
# else: 
#     print('Inside the Else ')
# We will get the Systax Error If we pass finally before an Else part
"""  File "c:\Projects\PythonPracticce\PythonPractice_Spyder\Basics\exception_demo.py", line 7
    else:
    ^
SyntaxError: invalid syntax """

# We can use the multiple except blocks for single try blcok
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass


    