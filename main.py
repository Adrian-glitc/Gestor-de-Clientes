import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Clientes")
ventana.geometry("700x400")

# Crear menú
menubar = tk.Menu(ventana)
ventana.config(menu=menubar)

# Menú archivo
menu_archivo = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Menú ayuda
menu_ayuda = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=lambda: print("Gestor de Clientes v1.0"))

# Crear pestañas
pestanas = ttk.Notebook(ventana)
pestanas.pack(fill='both', expand=True)

# Crear dos pestañas
pestana_formulario = ttk.Frame(pestanas)
pestana_busqueda = ttk.Frame(pestanas)

# Añadir las pestañas al Notebook
pestanas.add(pestana_formulario, text="Formulario")
pestanas.add(pestana_busqueda, text="Buscar Cliente")

ventana.mainloop()
