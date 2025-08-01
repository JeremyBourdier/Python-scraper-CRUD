import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    """
    Función principal que inicializa el WebDriver, abre una página y la cierra.
    """
    print("Iniciando script de scraping...")

    # Configura el servicio del ChromeDriver automáticamente
    service = Service(ChromeDriverManager().install())

    # Inicializa el navegador Chrome
    driver = webdriver.Chrome(service=service)

    # Abre una page web de prueba
    driver.get("https://www.google.com")

    print("Página abierta. Esperando 5 segundos...")
    time.sleep(5) # Espera para que cargue

    # Cierra el navegador
    driver.quit()
    print("Script finalizado.")


if __name__ == "__main__":
    main()