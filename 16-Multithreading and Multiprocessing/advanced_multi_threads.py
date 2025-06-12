from concurrent.futures import ThreadPoolExecutor
import time

def print_square(number):
    time.sleep(2)
    return f"Square of {number}: {number ** 2}"

numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_square, numbers)

for result in results:
    print(result)