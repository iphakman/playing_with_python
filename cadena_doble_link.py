class slavon:
    """
    Clase slavon: contiene la referencia hacia adelante y hacia atras.
    al momento de crearse por default los valores pre/post son nulos.
    ambos valores son a su vez objetos de la clases slavon.
    """
    def __init__(self, name, pre=None, post=None):
        self.name = name
        self.pre = pre
        self.post = post

    def __str__(self):
        return "{}".format(self.name)


class cadena:
    """
    Recibira objetos tipo slavon.
    """
    slavones = []

    def __init__(self, inicio):
        """
        Al declarar esta variable, definimos el nombre y lo asignamos a inicio.
        Este sera nuestro punto de partida y no tendra referencias aun.

        NOTA: debe ser un objeto de tipo slavon
        """
        self.inicio = inicio
        self.last = None

    def agregar(self, new_s):
        """
        Agregara al final de la de nuestra cadena.
        Si unicamente tenemos 1 elemento(self.inicio), simplemente creara referencia en este elemneto
        (atributo .post) y asignara el nuevo elemento a self.last
        En este ultimo ligara el inicio en el atributo .pre

        En caso de que ya exista el self.last:
          - en el ultimo elemento pasaremos como atributo al nuevo slavon en post.
          - creamos un valor temporal pre_temp
          - reasignamos self.last con el nuevo slavon
          - en el nuevo self.last.pre, ligamos el slavon temporal
        """
        if self.last is not None:
            self.last.post = new_s
            pre_temp = slavon(self.last.name, self.last.pre, self.last.post)
            self.last = new_s
            self.last.pre = pre_temp
        else:
            self.inicio.post = new_s
            self.last = new_s
            self.last.pre = slavon(self.inicio)

        print("fin agregado: ", self.last.pre, self.last.name, self.last.post)

    def remover(self, i=0):
        """
        Removera el ultimo elemento del final de la cadena
        si pasamos 1(o cualquier valor) eliminara el elemento al inicio.
        """
        if not i:
            self.last = slavon(self.last.pre.name, self.last.pre.pre, None)
        else:
            self.inicio = slavon(self.inicio.post.name, None, self.inicio.post.post)

    def __str__(self):
        return "Inicia en {}".format(self.inicio)

    def show(self, i=0):
        """
        mostraremos en pantalla cada elemento slavon de la cadena.
        si pasamos 1(o cualquier valor) se mostraran en reversa.
        :param i:
        :return:
        """
        print("*" * 30)
        print("SHOW:")
        if not i:
            val = slavon(self.inicio.name, self.inicio.pre, self.inicio.post)
            while val.post is not None:
                print("{}->{}->{}".format(val.pre, val.name, val.post))
                print("new slavon: ", val.post.pre, val.post.name, val.post.post)
                if val.post.post is None:
                    val = slavon(val.post.name, val.post.pre, None)
                else:
                    val = slavon(val.post.name, val.post.pre, val.post.post)

            if self.last is None or val.name == self.last.name:
                print("{}<-{}<-{}".format(val.pre, val.name, val.post))
        else:
            if self.last is not None:
                val = slavon(self.last.name, self.last.pre, self.last.post)
            else:
                val = slavon(self.inicio.name, self.inicio.pre, self.inicio.post)
            while val.pre is not None:
                print("{}<-{}<-{}".format(val.pre, val.name, val.post))
                val = slavon(val.pre.name, val.pre.pre, val.pre.post)

            print("{}<-{}<-{}".format(self.inicio.pre, self.inicio.name, self.inicio.post))

        print("*" * 30)


if __name__ == '__main__':
    es1 = slavon('primero')
    es2 = slavon('dos')
    es3 = slavon('tres')
    es4 = slavon('cuatro')
    es5 = slavon('cinco')

    c = cadena(es1)
    c.show(1)
    c.show()
    c.agregar(es2)
    c.agregar(es3)
    c.agregar(es4)
    c.agregar(es5)
    c.remover()
    c.show()
    c.show(1)
