# Proyecto Scraper y Gestor de Libros (Python-scraper-CRUD)

Este es un proyecto de práctica que construye una aplicación de escritorio completa. El programa extrae (hace scraping) datos de libros desde la web y permite al usuario gestionarlos a través de una base de datos local y una interfaz gráfica simple.

## Características Principales

* **Web Scraper:** Usa Selenium para extraer automáticamente los títulos, precios y URLs de los libros desde la página `books.toscrape.com`.
* **Backend CRUD:** Toda la lógica para Crear, Leer, Actualizar y Borrar registros está implementada usando Python y una base de datos SQLite.
* **Interfaz de Terminal:** Permite gestionar la base de datos a través de comandos simples en la terminal (ej: `--listar`, `--borrar <ID>`).
* **Interfaz Gráfica (GUI):** Una ventana fácil de usar creada con Tkinter para visualizar, borrar y actualizar los libros guardados.

## Requisitos

* Python 3.x

## Instalación y Uso

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/JeremyBourdier/Python-scraper-CRUD)
    cd Python-scraper-CRUD
    ```

2.  **Crea y activa un entorno virtual:**
    * En Windows:
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * En macOS / Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación:**
    * Para usar la **interfaz gráfica** (recomendado):
        ```bash
        python gui.py
        ```
    * Para usar la **terminal**:
        ```bash
        # Para añadir libros a la base de datos
        python main.py --scrape

        # Para listar los libros guardados
        python main.py --listar
        ```

---
## Próxima Versión 

Para la siguiente versión del proyecto, el plan es enfocarse en mejorar la estructura del código y la experiencia del usuario. Lo que haré será:

1.  **Refactorizar el Código a Clases (OOP):** Organizaré la lógica del scraper y de la base de datos en Clases de Python. Esto hará el código más limpio, profesional y fácil de mantener.
2.  **Mejorar la Interfaz Gráfica:** Añadiré nuevas funciones a la ventana, como un campo para buscar libros o un formulario para poder editar el título y el precio de un libro existente.
3.  **Crear un Archivo Ejecutable:** Convertiré el proyecto en una aplicación independiente (`.exe` para Windows) usando `PyInstaller`, para que cualquier persona pueda usarla sin necesidad de tener Python instalado.
