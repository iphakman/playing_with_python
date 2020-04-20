"""
Hay un area tecnica representada por un grid de M*N bloques. Cada bloque representa un area de parque, denotada por 1, 
o un area comercial, 0. Bloques adjacentes con valor 1 son consideradas parte del mismo parque. Bloques diagonales con valor
1 no son consideradas parte de la continuidad. Se planea encontrar un tesoro en cada area del parque continua.

Escribir un algoritmo que encuentre el numero de tesoros que pueden ser abiertos en el area tecnica.
"""


def check_status(midict, milist):
    for key in midict.keys():
        if milist in midict[key]:
            return key

    return None


def treasureNumbers(rows, columns, grid):
    coord = {}
    status = False
    for g in range(rows):
        for k in range(columns):
            if grid[k][g] == 1:
                if len(coord) == 0:
                    coord[1] = [[k][g]]
                else:
                    if k > 0:
                        key = check_status(coord, [k - 1, g])
                    else:
                        key = None

                    if key is None:
                        if g > 0:
                            key = check_status(coord, [k, g -1])

                    if key is not None:
                        coord[key].append([k, g])
                    else:
                        new = max(coord.keys())
                        coord[new] = [[k, g]]

    return max(coord.keys())


if __name__ == '__main__':
    """
    The input of the function/method consists of three arguments
        rows: an integer representing the number of rows in the grid.
        columns: an integer representing the number of columns in the grid.
        grid: a two-dimentional integer array reprecenting technicia.
    """
    my_grid = [[1, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0]]

    print(treasureNumbers(4, 4, my_grid))
