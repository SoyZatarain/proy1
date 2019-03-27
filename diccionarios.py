class SIMBOLIZAR:
    """
    Para crear objetos de pares tipo-valor
    """
    def __init__(self, tipo: str, valor: str):
        self.tipo = tipo
        self.valor = valor

simbolos: dict = {
    "<":  SIMBOLIZAR("SYMBOL_OPENTAGS", "<"),
    ">":  SIMBOLIZAR("SYMBOL_CLOSETAG", ">"),
    "/":  SIMBOLIZAR("SYMBOL_DIAGONAL", "/"),
    "=":  SIMBOLIZAR("SYMBOL_EQUALSYM", "="),
    "'":  SIMBOLIZAR("SYMBOL_SINQUOTE", "'"),
    "\"": SIMBOLIZAR("SYMBOL_DOBQUOTE", "\""),
}