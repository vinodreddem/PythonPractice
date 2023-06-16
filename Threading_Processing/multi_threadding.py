import threading 
import logging
import time 

def thread_function(name):
    logging.info("Threads %s starting ",name)
    time.sleep(3)
    logging.info("Threads %s Ending ",name)
    
if __name__ == "__main__":
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S")
    
    threads = list()
    
    for  i in range(5):
        logging.info ("Main : Create and Strting Thread : %d", i)
        x = threading.Thread (target=thread_function,args=(i,))
        threads.append (x)
        x.start()
    for index, thread in enumerate(threads):
        logging.info("Main : before Joining the thread %d",index)
        thread.join()
        logging.info("Main  : Thread %d done ",index )
        
    