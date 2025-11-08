import tkinter as tk

# Debes escribir un usuario y contraseña
usuario = "Micha"
password = "1998"
# Funciones
def capturar_credenciales():
  USUARIO = input_usuario.get()
  PASSWORD = input_password.get()

  #El método config admite argumento foreground="" con el cuál podemos especificar el color del texto
  if usuario == USUARIO and password == PASSWORD:
    mensaje.pack()
    mensaje.config(text="Usuario correcto, su igreso a sido exitoso sea Bienvenido", foreground="green")
    mensaje.pack()

  else:
   mensaje.config(foreground="red") 
   mensaje.pack()
   mensaje.config(text ="Ingreso incorrecto, reviselo su contraseña o usuario")
   mensaje.pack()

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title ("Registro de usuario")

# Widgets
separador = tk.Frame(ventana, height=25)
separador.pack()
etiqueta_usuario = tk.Label(ventana, text="Usuario")
etiqueta_usuario.pack()

input_usuario = tk.Entry(ventana)
input_usuario.pack()

separador = tk.Frame(ventana, height=20)
separador.pack()
etiqueta_password = tk.Label(ventana, text="Password")
etiqueta_password.pack()

input_password = tk.Entry(ventana)
input_password.pack()

mensaje = tk.Label(ventana)

separador = tk.Frame(ventana, height=20)
separador.pack()
boton = tk.Button(ventana, text="Haz click aquí", command=capturar_credenciales)
boton.pack()

separador = tk.Frame(ventana, height=20)
separador.pack()
boton = tk.Button(ventana, text="Salir", command=ventana.quit)
boton.pack()
ventana.mainloop()


