#importamos la clase Flask desde el modulo flask
from flask import Flask

#creamos una instancia de la clase Flask, esta se convierte en la aplicación web
app = Flask(__name__)

#condiconamos para verificar si el script se está ejecutando directamente (no importado como módulo)
if __name__ == '__main__':
    #este ejecuta la aplicación Flask en el puerto 3000 con el modo de depuración activado
    app.run(port=3000, debug=True)
