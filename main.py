import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    print("Iniciando script de scraping...")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    base_url = "http://books.toscrape.com/"
    driver.get(base_url)
    print(f"Página abierta: {base_url}")

    libros = driver.find_elements(By.CLASS_NAME, "product_pod")
    
    print("\n--- Datos Completos de Libros Encontrados ---")
    for libro in libros:
        # Elemento <a> que contiene tanto el título como la URL
        enlace = libro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
        
        # Extraer título y URL del mismo elemento
        titulo = enlace.get_attribute("title")
        url_relativa = enlace.get_attribute("href")
        url_completa = "http://books.toscrape.com/" + url_relativa #Solucion al bug con la url 
        
        # Extraer el precio
        precio = libro.find_element(By.CLASS_NAME, "price_color").text
        
        # Imprimimos todos los datos
        print(f"Título: {titulo} | Precio: {precio} | URL: {url_completa}")
        
    print("------------------------------------------\n")

    time.sleep(2)
    driver.quit()
    print("Script finalizado.")

if __name__ == "__main__":
    main()