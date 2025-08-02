import sqlite3

DATABASE_NAME = "books.db"

def get_db_connection():
    """Crea y retorna una conexión a la base de datos."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    """Crea la tabla 'libros' si no existe."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Comando SQL en una variable
    sql_crear_tabla = '''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            precio TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE,
            estado TEXT NOT NULL DEFAULT 'Pendiente',
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    '''

    print("--- Ejecutando la siguiente instrucción SQL: ---")
    print(sql_crear_tabla)
    print("---------------------------------------------")

    cursor.execute(sql_crear_tabla)

    conn.commit()
    conn.close()
    print("Tabla 'libros' verificada/creada exitosamente.")

def add_book(cursor, titulo, precio, url):
    """Añade un nuevo libro usando un cursor existente."""
    try:
        cursor.execute(
            "INSERT INTO libros (titulo, precio, url) VALUES (?, ?, ?)",
            (titulo, precio, url)
        )
        print(f"Libro preparado para añadir: {titulo}")
    except sqlite3.IntegrityError:
        print(f"El libro ya existe en la base de datos: {titulo}")
        
def get_all_books():
    """Recupera todos los libros de la base de datos."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM libros ORDER BY id DESC")
    libros = cursor.fetchall()
    conn.close()
    return libros

def update_book_status(id, estado):
    """Actualiza el estado de un libro por su ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE libros SET estado = ? WHERE id = ?", (estado, id))
    conn.commit()
    # rowcount nos dice cuántas filas fueron afectadas.
    if cursor.rowcount == 0:
        print(f"Error: No se encontró ningún libro con el ID {id}.")
    else:
        print(f"Libro con ID {id} actualizado al estado '{estado}'.")
    conn.close()

def delete_book(id):
    """Borra un libro por su ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id,))
    conn.commit()
    if cursor.rowcount == 0:
        print(f"Error: No se encontró ningún libro con el ID {id}.")
    else:
        print(f"Libro con ID {id} ha sido borrado.")
    conn.close()