import numpy as np 
import time

my_arr = np.arange(100000)
my_list = list(range(100000))

start_time_arr = time.time()
for _ in range(100):
    my_arr = my_arr *2
end_time_arr = time.time()

print (end_time_arr - start_time_arr)

start_time_lst = time.time()
for _ in range(100):
    my_list = [x *2 for x in my_list]
end_time_lst = time.time()
print(end_time_lst - start_time_lst)