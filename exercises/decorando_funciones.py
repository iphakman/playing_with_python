"""
decorators practice

this will print a header line and tail line for each function.

additional will print time spend
"""
import time

def mali(func):
    def fancy_print(*args, **kwargs):
        start_time = time.time()
        print("_" * 10)
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time, "sec")
        print("*" * 10)
    return fancy_print

@mali
def test1():
    for a in range(8):
        print(a * a)


@mali
def counter1(value):
    result = {}
    for k in value:
        try:
            result[k] += 1
        except KeyError:
            result[k] = 1
    
    for key in result.keys():
        print(key, result[key])

if __name__ == "__main__":
    test1()
    counter1("application")
    counter1("esta es una prueba")
