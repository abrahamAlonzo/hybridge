import tkinter as tk
from tkinter import messagebox, font

def agregar_tarea():
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, escribe una tarea.")

def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_seleccionada)
    except IndexError:
        messagebox.showwarning("Error", "No hay ninguna tarea seleccionada.")

def completar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_seleccionada)
        # Verificar si la tarea ya está completada
        if tarea.startswith("✔"):
            tarea = tarea[2:]  # Remover el "✔ "
        else:
            tarea = f"✔ {tarea}"  # Agregar "✔ " al principio
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tarea_seleccionada, tarea)
    except IndexError:
        messagebox.showwarning("Error", "No hay ninguna tarea seleccionada.")


ventana = tk.Tk()
ventana.title("Lista de Tareas")
fuente_completada = font.Font(family="Helvetica", size=10, slant="italic")

entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)

# Botones para acciones
boton_agregar = tk.Button(ventana, text="Agregar", width=15, command=agregar_tarea)
boton_agregar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar", width=15, command=eliminar_tarea)
boton_eliminar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Completar/Desmarcar", width=15, command=completar_tarea)
boton_completar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# Iniciar el bucle de la aplicación
ventana.mainloop()
