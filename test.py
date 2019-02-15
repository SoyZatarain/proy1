from htmlgen import *

contenido = HTMLGEN('<img src="img.jpg" width="100" height="200">')

while contenido.caracterActual is not None:
    nodo = contenido.cargarSiguienteSimbolo()
    print("Detectado simbolo %s de tipo %s" % (nodo.valor, nodo.tipo))
    print("=========================================================")