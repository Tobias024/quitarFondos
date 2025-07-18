import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove
import io
import os

def seleccionar_imagen():
    archivo = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.webp *.bmp")]
    )
    if archivo:
        entrada_path.set(archivo)
        mostrar_imagen(archivo)

def mostrar_imagen(path):
    imagen = Image.open(path).resize((300, 300))
    foto = ImageTk.PhotoImage(imagen)
    label_imagen.config(image=foto)
    label_imagen.image = foto

def procesar_imagen():
    entrada = entrada_path.get()
    if not entrada:
        messagebox.showwarning("Advertencia", "Seleccioná una imagen primero.")
        return

    with open(entrada, 'rb') as f:
        entrada_bytes = f.read()

    salida_bytes = remove(entrada_bytes)
    imagen_salida = Image.open(io.BytesIO(salida_bytes))

    # Guardar automáticamente en la misma carpeta
    base, ext = os.path.splitext(entrada)
    salida = base + "_sin_fondo.png"
    imagen_salida.save(salida)

    messagebox.showinfo("Listo", f"Imagen sin fondo guardada como:\n{salida}")
    mostrar_imagen(salida)

# GUI
ventana = tk.Tk()
ventana.title("Quitar Fondo de Imagen")
ventana.geometry("400x450")
ventana.resizable(False, False)

entrada_path = tk.StringVar()

tk.Label(ventana, text="Quitar fondo de imagen", font=("Arial", 16)).pack(pady=10)

btn_seleccionar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
btn_seleccionar.pack(pady=10)

label_imagen = tk.Label(ventana)
label_imagen.pack()

btn_procesar = tk.Button(ventana, text="Quitar fondo", command=procesar_imagen, bg="green", fg="white")
btn_procesar.pack(pady=20)

ventana.mainloop()
