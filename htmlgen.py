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

    def avanzar(self, pasos=1):
        self.posicion += pasos
        self.columna += pasos
        if self.posicion > len(self.texto) - 1:
            self.caracterActual = None
        else:
            self.caracterAnterior = self.texto[self.posicion-1]
            self.caracterActual = self.texto[self.posicion]

    def simbolosIgnorados(self):
        while self.caracterActual is not None and self.caracterActual.isspace():
            self.avanzar()

    def palabra(self):
        palabras = ""
        if self.caracterAnterior in ['"', "'"]:
            final = self.caracterAnterior
            while self.caracterActual is not None and self.caracterActual != final:
                palabras += self.caracterActual
                self.avanzar()
            return diccionarios.SIMBOLIZAR("ATTR_VALUE", palabras)
        elif self.caracterAnterior == ">":
            while self.caracterActual is not None and self.caracterActual != '<':
                palabras += self.caracterActual
                self.avanzar()
            return diccionarios.SIMBOLIZAR("HTML_INNERTEXT", palabras)
        elif self.caracterAnterior == "<":
            while self.caracterActual is not None and not (self.caracterActual.isspace() or self.caracterActual == ">"):
                palabras += self.caracterActual
                self.avanzar()
            return diccionarios.SIMBOLIZAR("HTML_TAG_"+palabras.upper()+"_OPEN", palabras.upper())
        elif self.caracterAnterior == "/":
            while self.caracterActual is not None and self.caracterActual != '>':
                palabras += self.caracterActual
                self.avanzar()
            return diccionarios.SIMBOLIZAR("HTML_TAG_"+palabras.upper()+"_CLOSE", palabras.upper())
        else:
            while self.caracterActual is not None and (self.caracterActual.isalnum() or self.caracterActual in ["-", "."]):
                palabras += self.caracterActual
                self.avanzar()
            return diccionarios.SIMBOLIZAR("ATTR_NAME", palabras)

    def excepcion(self):
        raise Exception("Caracter no reconocido: " + self.caracterActual)

    def cargarSiguienteSimbolo(self):
        while self.caracterActual is not None:
            if self.caracterActual.isspace():
                if self.caracterActual == "\n":
                    self.linea += 1
                    self.columna = 1
                self.simbolosIgnorados()
                continue
            elif self.caracterAnterior in ["'", '"'] and self.texto[self.posicion-2]=="=":
                return self.palabra()
            elif self.caracterActual.isalpha():
                return self.palabra()
            elif self.caracterActual in list(diccionarios.simbolos.keys()):
                temp = self.caracterActual
                self.avanzar()
                return diccionarios.simbolos.get(temp)
            elif self.caracterActual == "!" and self.caracterAnterior == "<":
                while self.caracterActual is not None and self.caracterActual != ">":
                    self.avanzar()
                return diccionarios.SIMBOLIZAR("COMMENT", "comentario")
            elif self.caracterAnterior == ">":
                return self.palabra()
            else:
                self.excepcion()
        return diccionarios.SIMBOLIZAR("FIN", None)

class Arbol:
    def __init__(self, simbolosAsignados):
        self.simbolosAsignados = simbolosAsignados
        self.simboloAnterior = None
        self.simboloActual = self.simbolosAsignados.cargarSiguienteSimbolo()
        self.estructuraActual = []

    def simboloDump(self):
        return self.simboloActual

    def ensamblar(self, tipoDeSimbolo):
        if self.simboloActual.tipo == tipoDeSimbolo:
            self.estructuraActual.append(self.simboloActual)
            self.simboloAnterior = self.simboloActual
            self.simboloActual = self.simbolosAsignados.cargarSiguienteSimbolo()

    def ensamblarAtributo(self):
        self.ensamblar("ATTR_NAME")
        self.ensamblar("SYMBOL_EQUALSYM")
        self.ensamblar("SYMBOL_DOBQUOTE")
        self.ensamblar("ATTR_VALUE")
        self.ensamblar("SYMBOL_DOBQUOTE")
        return diccionarios.Atributo(self.estructuraActual[0].valor, self.estructuraActual[3].valor)