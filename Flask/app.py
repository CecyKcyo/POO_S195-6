from flask import Flask,Request

#importamos la clase Flask desde el modulo flask
from flask import Flask

#creamos una instancia de la clase Flask, esta se convierte en la aplicación web
app = Flask(__name__)

#Ruta simple
@app.route('/')
def principal():
    return 'Hola mundo Flask'


#Ruta doble 
@app.route('/usuario')
@app.route('/saludar')
def saludo():
    return 'Hola, Ivan Isay'

#Rutas con parametros 
@app.route('/hi/<nombre>')
def hi(nombre):
    return 'Hola '+nombre+'!!!'

#Definicion de metodos de trabajo
@app.route('/formulario/', methods=['GET', 'POST'])
def formulario():
    if Request.method == 'GET':
        return 'No es seguro mandar password por GET, no seas tibio'
    elif Request.method == 'POST':
        return 'SI es seguro mandar password por POST'
    
#Manejador de exepciones 
@app.errorhandler(404)
def paginano(e):
    return'Revisa tu sintaxis, no encontre nada'
    

    


#condiconamos para verificar si el script se está ejecutando directamente (no importado como módulo)
if __name__ == '__main__':
    #este ejecuta la aplicación Flask en el puerto 3000 con el modo de depuración activado
    app.run(port=3000, debug=True)
