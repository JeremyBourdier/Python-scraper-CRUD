import time
import argparse #Para manejar argumentos de la terminal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin
import database

def scrape_books():
    """Función para hacer scraping y guardar en la BD."""
    print("Iniciando modo scraping...")
    conn = database.get_db_connection()
    cursor = conn.cursor()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    base_url = "http://books.toscrape.com/"
    driver.get(base_url)
    
    libros = driver.find_elements(By.CLASS_NAME, "product_pod")
    
    for libro in libros:
        enlace = libro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
        titulo = enlace.get_attribute("title")
        url_relativa = enlace.get_attribute("href")
        url_completa = urljoin(base_url, url_relativa)
        precio = libro.find_element(By.CLASS_NAME, "price_color").text
        database.add_book(cursor, titulo, precio, url_completa)
        
    conn.commit()
    conn.close()
    driver.quit()
    print("Scraping y guardado finalizados.")

def list_books():
    """Muestra todos los libros guardados en la base de datos."""
    print("\n--- Libros Guardados en la Base de Datos ---")
    libros = database.get_all_books()
    if not libros:
        print("No hay libros en la base de datos.")
    else:
        for libro in libros:
            # Mostramos tambien el estado
            print(f"ID: {dict(libro)['id']}, Título: {dict(libro)['titulo']}, Precio: {dict(libro)['precio']}, Estado: {dict(libro)['estado']}")
    print("------------------------------------------\n")


def main():
    database.create_table()
    
    # Define todos los comandos que el script puede recibir
    parser = argparse.ArgumentParser(description="Scraper y gestor de libros.")
    parser.add_argument("--listar", action="store_true", help="Lista los libros guardados.")
    
    # Comandos para actualizar y borrar por ID
    parser.add_argument("--actualizar", type=int, help="ID del libro a actualizar.")
    parser.add_argument("--estado", type=str, default="Leído", help="Nuevo estado para el libro.")
    parser.add_argument("--borrar", type=int, help="ID del libro a borrar.")
    
    args = parser.parse_args()

    # Decide qué hacer según el comando
    if args.listar:
        list_books()
    elif args.actualizar:
        database.update_book_status(args.actualizar, args.estado)
    elif args.borrar:
        database.delete_book(args.borrar)
    else:
        print("Por favor, especifica una acción: --listar, --actualizar <ID>, o --borrar <ID>.")


if __name__ == "__main__":
    main()