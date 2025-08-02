import tkinter as tk
from tkinter import messagebox
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

    def get_selected_book_id():
        """Obtiene el ID del libro seleccionado en la lista."""
        selected_index = listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un libro de la lista.")
            return None
        
        selected_item = listbox.get(selected_index)
        # Extrae el ID del texto del item seleccionado
        book_id = int(selected_item.split(" | ")[0].split(": ")[1])
        return book_id

    def borrar_libro():
        """Borra el libro seleccionado."""
        book_id = get_selected_book_id()
        if book_id:
            database.delete_book(book_id)
            cargar_libros() # Refresca la lista para mostrar el cambio

    def marcar_leido():
        """Actualiza el estado del libro seleccionado a 'Leído'."""
        book_id = get_selected_book_id()
        if book_id:
            database.update_book_status(book_id, "Leído")
            cargar_libros() # Refresca la lista para mostrar el cambio

    # Contenedor para los botones
    action_frame = tk.Frame(root)
    action_frame.pack(pady=10)

    # Botones de acción
    btn_cargar = tk.Button(action_frame, text="Cargar Libros", command=cargar_libros)
    btn_cargar.pack(side='left', padx=5)

    btn_marcar = tk.Button(action_frame, text="Marcar como Leído", command=marcar_leido)
    btn_marcar.pack(side='left', padx=5)

    btn_borrar = tk.Button(action_frame, text="Borrar Seleccionado", command=borrar_libro)
    btn_borrar.pack(side='left', padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()