"""
Kaprekar's constant

The number 6174 is known as Kaprekar's constant. It is the ultimate convergence point of the Kaprekar's routine, an algorithm thought up by Indian mathematician D.R. Kaprekar in 1949.

The routine is as follows:
1. Take any four-digit number (at least two different digits must be used, zeroes allowed).
2. Arrange the digits in descending and then in ascending order to get two four-digit numbers.
3. Subtract the smaller number from the larger and get the result.
4. Repeat steps 2-4 with the new number.

After a few iterations, the algorithm converges to a fixed point and starts to result in the same number  - 6174 - the so-called Kaprekar's constant.
"""
def get_num_ordered(n):
    order_num = []
    for k in str(n):
        order_num.append(k)
    order_num.sort()
    return int(''.join(order_num))

    
def get_k(n):
    sort_n = get_num_ordered(n)
    
    reversed = int(str(sort_n)[::-1])
    if sort_n < 1000:
        reversed *= 10
    if sort_n > reversed:
        print("{} - {} = {}".format(sort_n, reversed, sort_n - reversed))
        return sort_n - reversed
    else:
        print("{} - {} = {}".format(reversed, sort_n, reversed - sort_n))
        return reversed - sort_n
        

if __name__ == "__main__":
    num = 9832
    a = get_num_ordered(num)
    
    print(a)
    while num != 6174 and num >101:
        num = get_k(num)
