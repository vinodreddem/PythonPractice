import threading 
import time 
""" 
https://realpython.com/intro-to-python-threading/#what-is-a-thread

Python threads are a form of parallelism that allow your program to run multiple procedures at once.
Parallelism in Python can also be achieved using multiple processes, but threads are particularly well
suited to speeding up applications that involve significant amounts of I/O (input/output).
Tking inputs from other APIs.

Example I/O-bound operations include making web requests and reading data from files. 
In contrast to I/O-bound operations, CPU-bound operations (like performing math with the Python standard library)
will not benefit much from Python threads.
"""

def func ():
    print ("Run")
    time.sleep(2)
    print ('Done')
    print (threading.__name__)

thre = threading.Thread(target = func)
thre.start()
print (threading.activeCount())

print (threading.active_count())
print (threading.get_native_id)

""" 
Run ----New Thread Output Operation , due to sleep come back to original thread and execute the statements 
2 --goes back to original thread.
2
<built-in function get_native_id>
Done
threading
"""

