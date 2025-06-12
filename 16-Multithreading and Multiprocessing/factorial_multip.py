import multiprocessing
import sys
import math
import time

sys.set_int_max_str_digits(100000)


def factorial(n):
    print(f"Compute factorial of {n}")
    result = math.factorial(n)
    print(f"Factorial of {n}: {result}")
    return result


if __name__ == "__main__":

    numbers = [5000, 6000, 7000]
    processes = []

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    end_time = time.time() - start_time

    print(f"Results: {results}")
    print(f"Time taken: {end_time}")