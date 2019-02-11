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
 Primeramente, lo que ya se tiene es lo siguiente:
 1.- Diccionario de etiquetas validas para HTML5 en tres categorías; TAG, HTMLNW Y DPRCATD
 2.- Clase para simbolizar etiquetas con tipo y valor
 3.- Método para recorrer el contenido de la entrada y simbolizar cada nombre de etiquetas
 Los planes de aquí en adelante son:
 1.- Diccionario de simbolos
 2.- Diccionario de atributos
 3.- Leer archivo, no entrada estándar
 4.- Detectar uso de etiquetas obsoletas
 5.- Detectar uso de atributos incorrectos

 > Posibles preguntas
 ~~~~~~~~~~~~~~~~~~~~~~
 1.- P: ¿Cuál es el motivo de hacer este programa?
     R: A veces necesito crear elementos en el DOM de manera dinámica y no quiero perder
        tiempo escribiendo código que es pensar casi nada y escribir mucho.
 2.- P: ¿Por qué en Python?
     R: Necesito que el programa funcione mediante scripting, de los lenguajes que permiten
        esta caracteristica Python es el que mejor conozco. (Respuesta corta: y por qué no?)