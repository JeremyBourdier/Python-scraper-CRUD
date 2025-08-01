import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    print("Iniciando script de scraping...")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Navegamos al sitio de práctica
    url = "http://books.toscrape.com/"
    driver.get(url)
    print(f"Página abierta: {url}")

    # Encontramos todos los libros. Cada uno es un <article> con la clase 'product_pod'.
    libros = driver.find_elements(By.CLASS_NAME, "product_pod")

    print("\n--- Títulos de Libros Encontrados ---")
    # Iteramos sobre cada libro para extraer su título
    for libro in libros:
        # El título está dentro de una etiqueta <h3>, dentro de una etiqueta <a>
        titulo = libro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
        print(titulo)
    print("-------------------------------------\n")

    time.sleep(2) # Pequeña pausa
    driver.quit()
    print("Script finalizado.")

if __name__ == "__main__":
    main()