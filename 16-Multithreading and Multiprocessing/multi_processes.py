import multiprocessing
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letter():
    letters = 'abcde'
    for letter in letters:
        time.sleep(2)
        print(f"Letter: {letter}")

# create two processes and assign functions to them

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=print_number)
    p2 = multiprocessing.Process(target=print_letter)

    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p1.join()

    end_time = time.time() - t
    print(f"Time taken: {end_time}")