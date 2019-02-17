"""
HTMLGEN: Generador de HTML5 mediante JavaScript ES5.
Copyright 2019 Jesus Alan Ramirez Zatarain.
"""
import diccionarios

class HTMLGEN:
    def __init__(self, texto):
        self.texto = texto
        self.posicion = 0
        self.caracterActual = self.texto[self.posicion]
        self.caracterAnterior = None
        self.columna = 0
        self.linea = 1

    def avanzar(self):
        self.posicion += 1
        self.columna += 1
        if self.posicion > len(self.texto) - 1:
            self.caracterActual = None
        else:
            self.caracterAnterior = self.texto[self.posicion-1]
            self.caracterActual = self.texto[self.posicion]

    def simbolosIgnorados(self):
        while self.caracterActual is not None and self.caracterActual.isspace():
            self.avanzar()

    def palabra(self):
        cadenaEncontrada = ""
        while self.caracterActual is not None and self.caracterActual.isalnum():
            cadenaEncontrada += self.caracterActual
            self.avanzar()
        return diccionarios.etiquetas.get(cadenaEncontrada, diccionarios.SIMBOLIZAR("IDENTIFIER", cadenaEncontrada))

    def cargarSiguienteSimbolo(self):
        while self.caracterActual is not None:
            if self.caracterActual.isspace():
                if self.caracterActual == "\n":
                    self.linea += 1
                self.simbolosIgnorados()
                self.columna = 1
                continue
            elif self.caracterActual.isalpha():
                return self.palabra()
            elif self.caracterActual in list(diccionarios.simbolos.keys()):
                temp = self.caracterActual
                self.avanzar()
                return diccionarios.simbolos.get(temp)
            elif self.caracterActual.isdigit():
                numero = ""
                while self.caracterActual is not None and self.caracterActual.isdigit():
                    numero += self.caracterActual
                    self.avanzar()
                return diccionarios.SIMBOLIZAR("INT_NUMBER", numero)
            raise Exception("Caracter no reconocido: " + self.caracterActual)
        return diccionarios.SIMBOLIZAR("FIN", None)