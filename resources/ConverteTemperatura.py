
class ConverteTemperatura(object):

    @classmethod
    def checa_conversao(cls, unidadeOrigem=None, valor=None, unidadeDestino=None):

        temperatura_convertida = cls.executa_conversao(
            valor, unidadeOrigem, unidadeDestino)
        return temperatura_convertida

    @classmethod
    def executa_conversao(cls, valor, unidadeOrigem,  unidadeDestino):

        celsius = cls.para_celsius(float(valor), unidadeOrigem)

        temperatura_convertida = cls.de_celsius(celsius, unidadeDestino)
        return temperatura_convertida

    @staticmethod
    def para_celsius(temperatura, unidadeOrigem):

        if unidadeOrigem == 'F':
            return ((temperatura - 32) / 1.8)
        elif unidadeOrigem == 'K':
            return temperatura - 273.15
        elif unidadeOrigem == 'C':
            return temperatura
        return 'Temperatura inválida'

    @staticmethod
    def de_celsius(celsius, unidadeDestino):

        if unidadeDestino == 'F':
            return (celsius * 1.8) + 32
        elif unidadeDestino == 'K':
            return celsius + 273.15
        elif unidadeDestino == 'C':
            return celsius
        return 'Temperatura inválida'
