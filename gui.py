import tkinter as tk

def main():
    # Crear la ventana principal
    root = tk.Tk()
    
    # Ponerle un título a la ventana
    root.title("Gestor de Libros")
    
    # Definir el tamaño de la ventana (ancho x alto)
    root.geometry("700x500")
    
    # Iniciar el bucle principal de la aplicación para que la ventana se mantenga abierta
    root.mainloop()

if __name__ == "__main__":
    main()