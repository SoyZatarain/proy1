Proyecto 1: Generador de HTML5 mediante JavaScript ES5 implementado en Python
=====================================================================================

Python:
=============================================================================
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
=============================================================================

 > Objetivo
 ~~~~~~~~~~~~
 Introducir un documento en estándar XHTML 5.2, para generar un código JavaScript ES5 que
 lo genere con compatibilidad cercana al 100%. Por ejemplo, la entrada del código ->
    <div id="logo" class="encuadrado"><img src="uma.jpg"></div>
 se generaría la siguiente salida ->
    var div0 = document.createElement('div');
    div0.id = 'logo';
    div0.className = 'encuadrado';
    document.getElementsByTagName('body')[0].appendChild(div0);

    var img0 = document.createElement('img');
    img0.src = 'uma.jpg';
    div0.appendChild(img0);

 > Planes
 ~~~~~~~~~~
 1.- Etiquetas con o sin cierre
      <tag attr1="val1" attr2="val2" ... attrn="attrn">Inner of the tag</tag>
      ^ ^  \__________________  _____________________/^\______  ______/\_  _/
      | |                     \/                      |       \/         \/
      | |                 Atributos                   |       |         Cierre de etiqueta
      | |                                            /        |
      | Nombre de la etiqueta                       /     Interior de la etiqueta
      |                                            /
      Simbolo de apertura              Simbolo de cierre

      - Esta es una de las estructuras mas complejas que trataermos a lo largo del desarrollo
      y de ella rescataremos los pedazos que iremos recolectando en la etapa de simbolizacion
      como hemos hecho hasta ahora, pero con un nuevo paradigma.
      Etiqueta = Apertura + nombre + atributos + cierre + interior + cierre de etiqueta

      1.1.- Apertura (Obligatorio):
         Al estar trabajando con el estandar el simbolo de apertura sera siempre este: "<".
      1.2.- Nombre de etiqueta (Obligatorio):
         Ya tenemos un diccionario de etiquetas incluso indicando si son nuevas u obsoletas.
         Aqui habra que hacer otra separacion en una dimension nueva que indique si la etiqueta
         requiere de cierre o no.
      1.3.- Atributos (Opcional):
         La estructura de los atributos es muy simple:
               attribute="value: stylized;"
                   ^    ^^\______  ______/^
                   |    ||       \/       |
                   |    ||       |        \
                  /     ||       |         \
                 /      ||     valor        \
  Nombre de atributo   /  \                comilla o comillas
                      /  Comilla o
          Simbolo igual     comillas
          Atributo = nombre + igual + comillas + valor + comillas
      1.4.-  Simbolo de cierre (Obligatorio):
         Igual que en la apertura, siempre sera: ">"
      1.5.- Interior de la etiqueta (Opcional):
         Puede contener otras etiquetas que seguiran con la descripcion correspondiente o texto.
      1.6.- Cierre de etiqueta (Opcional):
         La estructura de el cierre queda asi:
         </tagname>
         ^^   ^   ^
         ||   |   |
        / |   |    \
Apertura  |   |     Cierre
         /     \
     Diagonal   \
                Nombre de etiqueta a cerrar
         Cierre de etiqueta = apertura + diagonal + nombre + cierre

 2.- Etiquetas especiales
      2.1.- Sera obligatorio incluir una etiqueta html, body y head; estas tres deben cumplir la jerarquia
      2.2.- La etiqueta doctype sera un simbolo especial y se simbolizara entero, ya que no tiene variantes
         validas en HTML5: <!DOCTYPE html>

 > Posibles preguntas
 ~~~~~~~~~~~~~~~~~~~~~~
 1.- P: ¿Cuál es el motivo de hacer este programa?
     R: A veces necesito crear elementos en el DOM de manera dinámica y no quiero perder
        tiempo escribiendo código que es pensar casi nada y escribir mucho.
 2.- P: ¿Por qué en Python?
     R: Necesito que el programa funcione mediante scripting, de los lenguajes que permiten
        esta caracteristica Python es el que mejor conozco. (Respuesta corta: y por qué no?)