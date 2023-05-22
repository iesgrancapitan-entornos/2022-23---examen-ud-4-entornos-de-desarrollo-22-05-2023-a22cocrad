"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""


class Vehiculo:
    """
    Superclase Vehiculo de la clase Coche.
    :autor: Adrian Cordovero
    """
    color = 'rojo';
    fabricante = 'seat';
    num_serie = 1;


class Coche(Vehiculo):
    """
    Clase coche que hereda de Vehiculo.
    """

    cilindrada = 1000;

    def __init__(self):
        """
        Constructor para crear objeto coche.
        """
        pass;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        """

        :param num_serie: Numero de serie del coche
        :param cilindrada: Cilindrada del coche
        :param fabricante: Fabricante del coche
        :param color: Color del coche
        """
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def num_serie(self):
        """

        :return: Devuelve el numero de serie del coche
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """

        :param value: Recibe un nuevo valor para el numero de serie del coche
        :return: None
        """
        self.__num_serie = value

    @property
    def color(self):
        """

        :return: Devuelve el color del coche
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        """

        :param value: Recibe el nuevo valor para el color del coche
        :return: None
        """
        self.__color = value

    @property
    def cilindrada(self):
        """

        :return: Devuelve la cilindrada del coche
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """

        :param value: Recibe el nuevo valor para la cilindrada del coche
        :return: None
        """
        self.__cilindrada = value

    @property
    def fabricante(self):
        """

        :return: Devuelve el fabricante del coche
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """

        :param value: Recibe el nuevo valor para el fabricante del coche
        :return: None
        """
        self.__fabricante = value
