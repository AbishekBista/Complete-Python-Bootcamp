import threading
import time

#create two functions

def print_square():
    for i in range(5):
        time.sleep(2)
        print(f"Square of {i}: {i ** 2}")

def print_cube():
    for i in range(5):
        time.sleep(2)
        print(f"Cube of {i}: {i ** 3}")

# create two threads and assign them processes
t1 = threading.Thread(target=print_square)
t2 = threading.Thread(target=print_cube)

t = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time() - t
print(f"Time taken: {end_time}")