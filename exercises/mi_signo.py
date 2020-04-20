dia = int(input("Ingresa el dia: "))
mes = input("Ingresa el mes: ")

meses = {'DIC': {'down': 'Sagitario', 'up': 'Capricornio', 'dia': 22},
         'ENE': {'down': 'Capricornio', 'up': 'Acuario', 'dia': 20},
         'FEB': {'down': 'Acuario', 'up': 'Piscis', 'dia': 19},
         'MAR': {'down': 'Piscis', 'up': 'Aries', 'dia': 21},
         'ABR': {'down': 'Aries', 'up': 'Tauro', 'dia': 20},
         'MAY': {'down': 'Tauro', 'up': 'Geminis', 'dia': 21},
         'JUN': {'down': 'Geminis', 'up': 'Cancer', 'dia': 21},
         'JUL': {'down': 'Cancer', 'up': 'Leo', 'dia': 23},
         'AGO': {'down': 'Leo', 'up': 'Virgo', 'dia': 23},
         'SEP': {'down': 'Virgo', 'up': 'Libra', 'dia': 23},
         'OCT': {'down': 'Libra', 'up': 'Escorpion', 'dia': 23},
         'NOV': {'down': 'Escorpion', 'up': 'Sagitario', 'dia': 22}}

mes = mes[:3].upper()
signo = meses[mes]['down'] if dia < meses[mes]['dia'] else meses[mes]['up']

print("Tu signo es :", signo)
