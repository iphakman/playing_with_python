"""
input: mes/dia de nacimiento

-- radom: respuesta.

lista con 5 predicciones
"""
from random import randint

opt = ['good_vibe', 'bad_vibe', 'neutral_vibe']
predicciones = {'good_vibe': ['Hoy sera un gran dia!',
                              'Tendras una llamada inesperada',
                              'Encontraras tu destino',
                              'Cambia el canal',
                              'Toma la desicion que estabas postergando!'],
                'bad_vibe': ['Ni te levantes!',
                             'Desiste de tu idea',
                             'No apuestes hoy',
                             'Rindete',
                             'Todo pinta mal hoy'],
                'neutral_vibe': ['Todo esta borroso',
                                 'Ni idea',
                                 'Intentalo',
                                 'mmm...',
                                 'Piensalo de nuevo...']}

meses = {"ENE": 1, "FEB": 2, "MAR": 3, "ABR": 4, "MAY": 5, "JUN": 6,
         "JUL": 7, "AGO": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DIC": 12}

mes = input("Ingresa tu mes de nacimiento: ")
dia = int(input("Ingresa tu dia de nacimiento: "))

if mes.isdigit():
    mes = int(mes)
else:
    mes = meses[mes[:3].upper()]

m = opt[randint(0, 2)]
