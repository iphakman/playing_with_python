"""
Happy Numbers

If the repeated sum of squares of the digits of a number is equal to 1, it is considered to be happy.
"""

def sep(val, n=20):
    print("*" * num, val)

def get_sum(n):
    result = 0
    op = []
    for k in str(n):
        op.append(k)
        result += int(k) * int(k)
    op = '+'.join(op)
    print(op + " = " + str(result))
    return result


if __name__ == "__main__":
    range_num = 50
    
    for num in range(10, range_num + 1):
        a = num
        sep(num)
        while a > 9:
            a = get_sum(a)
        if a == 1:
            print("{} is a Happy number!".format(num))
        else:
            print("{} is NOT a Happy number!".format(num))
