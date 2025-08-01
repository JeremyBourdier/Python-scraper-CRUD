import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    print("Iniciando script de scraping...")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = "http://books.toscrape.com/"
    driver.get(url)
    print(f"Página abierta: {url}")

    libros = driver.find_elements(By.CLASS_NAME, "product_pod")
    
    print("\n--- Datos de Libros Encontrados ---")
    for libro in libros:
        # Extraer el título (como antes)
        titulo = libro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
        
        # NUEVO: Extraer el precio
        # El precio está en un párrafo <p> con la clase 'price_color'
        precio = libro.find_element(By.CLASS_NAME, "price_color").text
        
        # Imprimimos ambos datos
        print(f"Título: {titulo} | Precio: {precio}")
        
    print("-------------------------------------\n")

    time.sleep(2)
    driver.quit()
    print("Script finalizado.")

if __name__ == "__main__":
    main()