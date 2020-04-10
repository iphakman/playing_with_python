"""
adivinar un numero de 1 10

-- input   siempre se caste a string
-- random   nuestro codigo va a definir el numero a adivinar al azar
"""
import random

to_guess = random.randint(1, 10)

mi_guess = 0
count = 0
while True:
    count += 1
    mi_guess = int(input("Adivina mi numero: "))
    if mi_guess == to_guess:
        print("Adivinaste en {} oportunidades!".format(count))
        break
