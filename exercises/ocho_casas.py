"""
Ocho casas representadas por celdas, estan alineadas en linea, cada dia cada una compite contra sus celdas adjacentes
Un valor entero de 1 representa la celula activa, y 0 las celulas inactivas. Si las celulas adjacentes en ambos lados de una 
celula son iguals(activos o inactivos), la celula se vuelve inactiva en el siguiente dia, de lo contrario la celula se activa.

Las 2 celdas en cada lado que solo cuentan con una celda adjacente, asumimos que el espacio no ocupado al lado contrario es
una celda inactiva. Incluso despues de actualizar el status de la celda, considear su estado anterior al actualizar las otras
celdas.
El status de todas las celdas debe ser actualizado simultaneamente.

Escribe un algoritmo que regrese el estado de cada celda despues del numero dado de dias.
"""


def neighbor_compare(states, days):
    result = [0 for x in range(len(states))]
    for d in range(days):
        for cell in range(len(states)):
            n = p = 0
            if cell == 0:
                p = 0
            else:
                p = states[cell - 1]

            if cell == len(states) - 1:
                n = 0
            else:
                n = states[cell + 1]

            result[cell] = 0 if p == n else 1

        states = [x for x in result]

    return states


if __name__ == '__main__':
    """
    input:
        states: list of integers representing the current state of cells.
        days: an integer representing the number of days.
    """
    st = [1, 0, 0, 0, 0, 1, 1, 0]
    print(neighbor_compare(st, 9))
