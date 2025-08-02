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
    """Función para listar los libros desde la BD."""
    print("\n--- Libros Guardados en la Base de Datos ---")
    libros = database.get_all_books()
    if not libros:
        print("No hay libros en la base de datos.")
    else:
        for libro in libros:
            # dict(libro) convierte la fila de la BD en un diccionario
            print(f"ID: {dict(libro)['id']}, Título: {dict(libro)['titulo']}, Precio: {dict(libro)['precio']}")
    print("------------------------------------------\n")


def main():
    database.create_table()
    
    # Lógica para decidir qué acción tomar
    parser = argparse.ArgumentParser(description="Scraper y gestor de libros.")
    parser.add_argument("--scrape", action="store_true", help="Ejecuta el scraper para buscar y guardar nuevos libros.")
    parser.add_argument("--listar", action="store_true", help="Lista los libros guardados en la base de datos.")
    args = parser.parse_args()

    if args.scrape:
        scrape_books()
    elif args.listar:
        list_books()
    else:
        print("Por favor, especifica una acción: --scrape o --listar")


if __name__ == "__main__":
    main()