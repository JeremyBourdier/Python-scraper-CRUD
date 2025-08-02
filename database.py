import sqlite3

DATABASE_NAME = "books.db"

def get_db_connection():
    """Crea y retorna una conexión a la base de datos."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row # Permite acceder a las columnas por nombre
    return conn

def create_table():
    """Crea la tabla 'libros' si no existe."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            precio TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Tabla 'libros' verificada/creada exitosamente.")