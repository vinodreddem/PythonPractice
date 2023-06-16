import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,),daemon=True)
    #daemon=True ---Then the last Print after sleep function i.e. 10:27:10: Thread 1: finishing will not log 
    # It will shutdown thread when the program exists , i.e. If main function executes completely then the 
    # program  
    #x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    # This will tell Main thread to pause untill thread x to execute so thar after x execution the main thread code execute
    logging.info("Main    : all done")
    
    