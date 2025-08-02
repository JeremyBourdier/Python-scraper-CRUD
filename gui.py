import tkinter as tk
import database

def main():
    root = tk.Tk()
    root.title("Gestor de Libros")
    root.geometry("800x600")

    # Contenedor principal
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10, fill='both', expand=True)

    # Lista para mostrar libros
    listbox = tk.Listbox(frame, height=20, width=100)
    listbox.pack(side='left', fill='both', expand=True)
    
    # Scrollbar para la lista
    scrollbar = tk.Scrollbar(frame, orient='vertical')
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side='right', fill='y')
    listbox.config(yscrollcommand=scrollbar.set)
    
    def cargar_libros():
        """Carga los libros de la base de datos en la lista."""
        listbox.delete(0, tk.END)
        libros = database.get_all_books()
        for libro in libros:
            libro_dict = dict(libro)
            listbox.insert(tk.END, f"ID: {libro_dict['id']} | Título: {libro_dict['titulo']} | Precio: {libro_dict['precio']} | Estado: {libro_dict['estado']}")

    # Botón para cargar los datos
    btn_cargar = tk.Button(root, text="Cargar Libros", command=cargar_libros, padx=10, pady=5)
    btn_cargar.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()