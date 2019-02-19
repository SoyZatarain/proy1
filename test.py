from htmlgen import *

milestone = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/action.php" method="POST">
        <div>
            <label for="server">Hostname or ip: </label>
            <input type="text" name="server" id="server">
        </div>
        <div>
            <label for="user">Username: </label>
            <input type="text" name="user" id="user">
        </div>
        <div>
            <label for="pass">Password</label>
            <input type="password" name="pass" id="pass">
        </div>
        <input type="submit" value="Log in">
    </form>
</body>
</html>
"""

contenido = HTMLGEN(milestone)

while contenido.caracterActual is not None:
    nodo = contenido.cargarSiguienteSimbolo()
    print("Detectado simbolo %s de tipo %s" % (nodo.valor, nodo.tipo))
    print("=========================================================")