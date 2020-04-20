"""Pandigital Numbers

If a number contains each of the digits from 0 to 9 at least once (0 not being the leading digit), it is considered to be pandigital.
"""

def is_pandigital(n):
    for k in range(10):
        if str(k) not in str(n):
            return False
    return True


if __name__ == "__main__":
    test1 = 1234567890
    test2 = 893938383910
    
    if is_pandigital(test1):
        print("{} is pan".format(test1))
    
    if is_pandigital(test2):
        print("{} is pan".format(test2))
