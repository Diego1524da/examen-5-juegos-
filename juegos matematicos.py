import tkinter as tk
import random
from tkinter import messagebox

# Segundo código: Menú y juegos con colores agradables

def iniciar_juego(modo):
    if modo == "Matemáticas Rápidas":
        matematicas_rapidas()
    elif modo == "Secuencia Numérica":
        secuencia_numerica()
    elif modo == "Adivina la Operación":
        adivina_la_operacion()

def crear_ventana_juego(titulo, color_fondo):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry("500x500")
    ventana.configure(bg=color_fondo)
    return ventana

def matematicas_rapidas():
    ventana = crear_ventana_juego("Matemáticas Rápidas", "#FFEB3B")
    tk.Label(ventana, text="Matemáticas Rápidas", font=("Arial", 16, "bold"), bg="#FFEB3B").pack(pady=10)
    puntaje = 0
    pregunta_label = tk.Label(ventana, text="", font=("Arial", 14), bg="#FFEB3B")
    pregunta_label.pack(pady=10)
    entrada = tk.Entry(ventana, font=("Arial", 14))
    entrada.pack(pady=10)
    resultado_label = tk.Label(ventana, text="", font=("Arial", 14), bg="#FFEB3B")
    resultado_label.pack(pady=10)
    puntaje_label = tk.Label(ventana, text=f"Puntaje: {puntaje}", font=("Arial", 12), bg="#FFEB3B")
    puntaje_label.pack(pady=5)
    
    def nueva_pregunta():
        nonlocal puntaje
        a, b = random.randint(1, 10), random.randint(1, 10)
        operacion = random.choice(['+', '-', '*', '/'])
        if operacion == '/':
            a *= b
        resultado = eval(f"{a} {operacion} {b}")
        pregunta_label.config(text=f"{a} {operacion} {b} = ?")
        entrada.delete(0, tk.END)
        
        def verificar_respuesta():
            nonlocal puntaje
            try:
                respuesta_usuario = float(entrada.get())
                if respuesta_usuario == resultado:
                    puntaje += 1
                    resultado_label.config(text="¡Correcto!", fg="green")
                    puntaje_label.config(text=f"Puntaje: {puntaje}")
                    ventana.after(1000, nueva_pregunta)
                else:
                    resultado_label.config(text="Incorrecto", fg="red")
            except ValueError:
                resultado_label.config(text="Ingresa un número válido", fg="red")
        
        if not hasattr(nueva_pregunta, "boton_responder"):
            nueva_pregunta.boton_responder = tk.Button(ventana, text="Responder", font=("Arial", 12), command=verificar_respuesta)
            nueva_pregunta.boton_responder.pack(pady=10)
    
    nueva_pregunta()
    
    btn_reiniciar = tk.Button(ventana, text="Reiniciar", font=("Arial", 12), bg="#FF5733", fg="white", command=matematicas_rapidas)
    btn_reiniciar.pack(side="left", padx=20, pady=20)
    btn_salir = tk.Button(ventana, text="Salir", font=("Arial", 12), bg="#FF5733", fg="white", command=ventana.destroy)
    btn_salir.pack(side="right", padx=20, pady=20)

def secuencia_numerica():
    ventana = crear_ventana_juego("Secuencia Numérica", "#D4F1F4")
    tk.Label(ventana, text="Secuencia Numérica", font=("Arial", 16, "bold"), bg="#D4F1F4").pack(pady=10)
    
    secuencia_label = tk.Label(ventana, text="", font=("Arial", 14), bg="#D4F1F4")
    secuencia_label.pack(pady=10)
    entrada = tk.Entry(ventana, font=("Arial", 14))
    entrada.pack(pady=10)
    resultado_label = tk.Label(ventana, text="", font=("Arial", 14), bg="#D4F1F4")
    resultado_label.pack(pady=10)
    puntaje = 0
    puntaje_label = tk.Label(ventana, text=f"Puntaje: {puntaje}", font=("Arial", 12), bg="#D4F1F4")
    puntaje_label.pack(pady=5)
    
    def nueva_secuencia():
        nonlocal puntaje
        base = random.randint(1, 5)
        secuencia = [base * (2 ** i) for i in range(3)]
        secuencia.append("?")
        secuencia_label.config(text=" , ".join(map(str, secuencia)))
        entrada.delete(0, tk.END)
    
    def verificar_secuencia():
        nonlocal puntaje
        try:
            respuesta_usuario = int(entrada.get())
            base = int(secuencia_label.cget("text").split(" , ")[0])
            correcta = base * (2 ** 3)
            if respuesta_usuario == correcta:
                puntaje += 1
                resultado_label.config(text="¡Correcto!", fg="green")
                puntaje_label.config(text=f"Puntaje: {puntaje}")
                ventana.after(1000, nueva_secuencia)
            else:
                resultado_label.config(text="Incorrecto", fg="red")
        except ValueError:
            resultado_label.config(text="Ingresa un número válido", fg="red")
    
    btn_responder = tk.Button(ventana, text="Responder", font=("Arial", 12), bg="#33FF57", fg="white", command=verificar_secuencia)
    btn_responder.pack(pady=10)
    
    nueva_secuencia()
    
    btn_reiniciar = tk.Button(ventana, text="Reiniciar", font=("Arial", 12), bg="#33FF57", fg="white", command=secuencia_numerica)
    btn_reiniciar.pack(side="left", padx=20, pady=20)
    btn_salir = tk.Button(ventana, text="Salir", font=("Arial", 12), bg="#FF5733", fg="white", command=ventana.destroy)
    btn_salir.pack(side="right", padx=20, pady=20)

def adivina_la_operacion():
    ventana = crear_ventana_juego("Adivina la Operación", "#FFEB3B")
    tk.Label(ventana, text="Adivina la Operación", font=("Arial", 16, "bold"), bg="#FFEB3B").pack(pady=10)
    
    operacion_label = tk.Label(ventana, text="", font=("Arial", 14), bg="#FFEB3B")
    operacion_label.pack(pady=10)
    entrada = tk.Entry(ventana, font=("Arial", 14))
    entrada.pack(pady=10)
    resultado_label = tk.Label(ventana, text="", font=("Arial", 14), bg="#FFEB3B")
    resultado_label.pack(pady=10)
    puntaje = 0
    puntaje_label = tk.Label(ventana, text=f"Puntaje: {puntaje}", font=("Arial", 12), bg="#FFEB3B")
    puntaje_label.pack(pady=5)
    
    def nueva_operacion():
        nonlocal puntaje
        a, b = random.randint(1, 10), random.randint(1, 10)
        operacion = random.choice(['+', '-', '*', '/'])
        resultado = eval(f"{a} {operacion} {b}")
        operacion_label.config(text=f"{a} {operacion} {b} = ?")
        entrada.delete(0, tk.END)
        
        def verificar_respuesta():
            nonlocal puntaje
            try:
                respuesta_usuario = float(entrada.get())
                if respuesta_usuario == resultado:
                    puntaje += 1
                    resultado_label.config(text="¡Correcto!", fg="green")
                    puntaje_label.config(text=f"Puntaje: {puntaje}")
                    ventana.after(1000, nueva_operacion)
                else:
                    resultado_label.config(text="Incorrecto", fg="red")
            except ValueError:
                resultado_label.config(text="Ingresa un número válido", fg="red")
        
        if not hasattr(nueva_operacion, "boton_responder"):
            nueva_operacion.boton_responder = tk.Button(ventana, text="Responder", font=("Arial", 12), bg="#FF5733", fg="white", command=verificar_respuesta)
            nueva_operacion.boton_responder.pack(pady=10)
    
    nueva_operacion()
    
    btn_reiniciar = tk.Button(ventana, text="Reiniciar", font=("Arial", 12), bg="#FF5733", fg="white", command=adivina_la_operacion)
    btn_reiniciar.pack(side="left", padx=20, pady=20)
    btn_salir = tk.Button(ventana, text="Salir", font=("Arial", 12), bg="#FF5733", fg="white", command=ventana.destroy)
    btn_salir.pack(side="right", padx=20, pady=20)

# Menú principal con un color agradable de fondo y título con degradado
def menu():
    menu_ventana = tk.Tk()
    menu_ventana.title("Juegos Matemáticos")
    menu_ventana.geometry("400x400")
    
    # Fondo difuminado
    menu_ventana.configure(bg="#FF64B5")
    canvas = tk.Canvas(menu_ventana, width=400, height=400, bg="#FF64B5", bd=0, highlightthickness=0)
    canvas.place(x=0, y=0)

    # Título con un gradiente de color
    label_titulo = tk.Label(menu_ventana, text="Juegos Matemáticos", font=("Arial", 24, "bold"), fg="white", bg="#FF64B5")
    label_titulo.pack(pady=30)

    # Botones de juegos
    juegos = [
        "Matemáticas Rápidas",
        "Secuencia Numérica",
        "Adivina la Operación"
    ]
    
    for juego in juegos:
        btn = tk.Button(menu_ventana, text=juego, font=("Arial", 14), width=20, height=2, bg="#64B5F6", 
                        fg="white", command=lambda juego=juego: iniciar_juego(juego))
        btn.pack(pady=10)
    
    menu_ventana.mainloop()

menu()
