from get_mi_object import mi_gen
import sys

with(open('mi_data.txt', 'r')) as f:
    print("file object SIZE: {}".format(sys.getsizeof(f)))
    ge = mi_gen(f)
    print(type(f))
    print("GENERATOR SIZE: {}".format(sys.getsizeof(ge)))
    print(type(ge))
    print(next(ge))
    print(next(ge))

# file object SIZE: 128
# <class '_io.TextIOWrapper'>
# GENERATOR SIZE: 48
# <class 'generator'>
