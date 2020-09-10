from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


#configuracion de la base de datos y la coneccion a la misma
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'anfetasa'
app.config['MYSQL_PASSWORD'] = 'qawsed123'
app.config['MYSQL_DB'] = 'proyecto_agenda'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

#ruta principal que renderiza el template html del formulario de registro

@app.route('/')
def index():
    return render_template('registro.html')

#ruta para agregar un usuario

@app.route('/add_user', methods=['POST' ,'GET'])
def add_user():

    #aca se reciben todos los datos otorgados en el formulario html

    if request.method =='POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        confirmar_pass = request.form['confirmar_pass']
        
        cur = mysql.connection.cursor()

        #se hace una validacion de que las contraseñas coincidan

        if contraseña == confirmar_pass:
            cur.execute('INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s,%s,%s)', (nombre, correo, contraseña))

            mysql.connection.commit()
            #El comando flash almacena el mensaje que sobrepone en pantalla y se imprime en el html
            flash('Usuario agregado satisfactoriamente')
            return redirect(url_for('index'))

        else:
            return 'Error al registrar el usuario'


if __name__ == '__main__':
    app.run(port= 3000, debug= True)