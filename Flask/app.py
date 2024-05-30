from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

#importamos la clase Flask desde el modulo flask

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']  = ''
app.config['MYSQL_DB'] = 'bdflask'
mysql =MySQL(app)
#creamos una instancia de la clase Flask, esta se convierte en la aplicación web


#Ruta simple
@app.route('/PruebaConexion')
def PruebaConexion():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("Select 1")
        datos = cursor.fetchone()
        return jsonify({'status:':'conexion exitosa','data':datos})
    except Exception as ex:
         return jsonify({'status:':'error conexion ','mensaje ':str(ex)})



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
    if request.method == 'GET':
        return 'No es seguro mandar password por GET, no seas tibio'
    elif request.method == 'POST':
        return 'SI es seguro mandar password por POST'
    
#Manejador de exepciones 
@app.errorhandler(404)
def paginano(e):
    return'Revisa tu sintaxis, no encontre nada'
    

    


#condiconamos para verificar si el script se está ejecutando directamente (no importado como módulo)
if __name__ == '__main__':
    #este ejecuta la aplicación Flask en el puerto 3000 con el modo de depuración activado
    app.run(port=3000, debug=True)
