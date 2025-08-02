import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin
import database

def main():
    print("Iniciando script...")
    database.create_table()

    conn = database.get_db_connection()
    cursor = conn.cursor()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    base_url = "http://books.toscrape.com/"
    driver.get(base_url)
    print(f"Página abierta: {base_url}")

    libros = driver.find_elements(By.CLASS_NAME, "product_pod")

    print("\n--- Guardando Libros en la Base de Datos ---")
    for libro in libros:
        enlace = libro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
        titulo = enlace.get_attribute("title")
        url_relativa = enlace.get_attribute("href")
        url_completa = urljoin(base_url, url_relativa)
        precio = libro.find_element(By.CLASS_NAME, "price_color").text

        database.add_book(cursor, titulo, precio, url_completa)

    print("------------------------------------------\n")

    conn.commit()
    conn.close()
    print("Cambios guardados y conexión a la base de datos cerrada.")

    driver.quit()
    print("Script finalizado.")

if __name__ == "__main__":
    main()