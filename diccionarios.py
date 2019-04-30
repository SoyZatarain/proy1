class SIMBOLIZAR:
    """
    Para crear objetos de pares tipo-valor
    """
    def __init__(self, tipo: str, valor: str):
        self.tipo = tipo
        self.valor = valor

class Atributo:
    def __init__(self, nombre: str, valor: str):
        self.nombre = nombre
        self.valor = valor

from typing import List

class Etiqueta:
    def __init__(self, nombre: str, atributos: List[Atributo]):
        self.nombre = nombre
        self.atributos = atributos
        # self.nodoSuperior = nodoSuperior

class TextoInterno:
    def __init__(self, contenido: str, nodoSuperior: Etiqueta):
        self.contenido = contenido
        self.nodoSuperior = nodoSuperior

simbolos: dict = {
    "<":  SIMBOLIZAR("SYMBOL_OPENTAGS", "<"),
    ">":  SIMBOLIZAR("SYMBOL_CLOSETAG", ">"),
    "/":  SIMBOLIZAR("SYMBOL_DIAGONAL", "/"),
    "=":  SIMBOLIZAR("SYMBOL_EQUALSYM", "="),
    "'":  SIMBOLIZAR("SYMBOL_SINQUOTE", "'"),
    "\"": SIMBOLIZAR("SYMBOL_DOBQUOTE", "\""),
}