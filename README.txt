Proyecto 1: Generador de HTML5 mediante JavaScript ES5 implementado en Python
=====================================================================================

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
 !!! SIMBOLIZACION SENCILLA TERMINADA, SIGUE EL ENSAMBLADO EN ESTRUCTURAS

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