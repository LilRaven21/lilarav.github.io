import sqlite3

def init_db():
    conn = sqlite3.connect('hoteles.db')
    c = conn.cursor()

    # Crear la tabla de hoteles si no existe
    c.execute('''
        CREATE TABLE IF NOT EXISTS hoteles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')

    # Insertar algunos datos de ejemplo
    c.execute('INSERT INTO hoteles (nombre, direccion, tipo) VALUES (?, ?, ?)',
              ('Hotel Amazonia', 'Av. Principal 123, Amazonas', 'Hotel'))
    c.execute('INSERT INTO hoteles (nombre, direccion, tipo) VALUES (?, ?, ?)',
              ('Hostal EcoPatagonia', 'Calle Torres del Paine, Patagonia', 'Hostal'))
    c.execute('INSERT INTO hoteles (nombre, direccion, tipo) VALUES (?, ?, ?)',
              ('Hostal Pura Vida', 'Playa Manuel Antonio, Costa Rica', 'Hostal'))

    conn.commit()
    conn.close()

# Llamar a la función para inicializar la base de datos
if __name__ == '__main__':
    init_db()
