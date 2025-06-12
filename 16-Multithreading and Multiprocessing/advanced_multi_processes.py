from concurrent.futures import ProcessPoolExecutor
import time

def print_cube(number):
    time.sleep(2)
    return f"Cube of {number}: {number ** 3}"


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_cube, numbers)
    
    for result in results:
        print(result)
