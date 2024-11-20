from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de hoteles y hostales
@app.route('/hoteles')
def hoteles():
    conn = sqlite3.connect('hoteles.db')
    c = conn.cursor()
    
    # Consultar los hoteles y hostales
    c.execute('SELECT nombre, direccion, tipo FROM hoteles')
    hoteles_data = c.fetchall()
    
    conn.close()
    
    # Renderizar la plantilla de hoteles con los datos obtenidos
    return render_template('hoteles.html', hoteles=hoteles_data)

if __name__ == '__main__':
    app.run(debug=True)
