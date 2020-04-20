"""
El maximo comun divisor (greatest common divisor - GCD), tambien llamado el factor comun mas alto (highest common factor -HCF)
de N numeros, es el entero positivo mas alto que divide todos los numeros sin regresar un residuo.

Escribir un algoritmo que determine el GCD de N enteros positivos.
"""


def generalGCD(num, arr):
    results = []
    for n in range(num):
        d = 1
        if n == 0:
            while d <= arr[n]:
                if arr[n] % d == 0:
                    results.append(d)
                d += 1
        else:
            valid = [x for x in results]
            results = []
            for v in valid:
                if arr[n] % v == 0:
                    results.append(v)

        print(arr[n], results)

    return max(results)


if __name__ == '__main__':
    """
    input:
        num: an integer representing the number of positive integers (N).
        arr: a list of positive integers.
    """

    l = [2, 4, 6, 8, 10]
    print(generalGCD(5, l))
