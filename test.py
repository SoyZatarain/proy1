# 1.- Texto de prueba, en este caso, un atributo generico que me invente
pruebaatributos = 'cref="listo"'

# 2.- Hacemos pasar el texto de prueba por el constructor de la clase HTMLGEN
#     para obtener los simbolos que lo componen y guardamos el  resultado  en
#     la variable "simbolos"
simbolos = HTMLGEN(pruebaatributos)

# 3.- Hacemos pasar la lista de simbolos obtenida en el paso anterior por  el
#     constructor de la clase Arbol para que la incorpore  como  uno  de  los
#     miembros del objeto resultante al instanciarle, el cual guardamos en la
#     variable "estructuras"
estructuras = Arbol(simbolos)

# 4.- Como nosotros ya sabemos que se trata de un atributo, nos  saltamos  la
#     deteccion, por lo que directamente pedimos que se enamble como tal.
final = estructuras.ensamblarAtributo()

# 5.- Finalmente, imprimimos esta cadena, que muestra el nombre y  valor  del
#     atributo una vez ensamblado
print("%s: %s" % (final.nombre, final.valor))

# - - -   A T E N C I O N   - - - 
# Esto solo es una prueba de concepto de el ensamblado de estructuras tomando
# en cuenta los simbolos generados, dependiendo de cada  simbolo  inicial  se
# tomara la decision de que tipo de estructura es. Ya estoy tomando en cuenta
# la jerarquia de las tructuras, por lo que a las clases creadas para  servir
# de contenedores tienen un atrubito en su constructor que hace referencia  a
# el nodo que las anvuelve. Los amo.