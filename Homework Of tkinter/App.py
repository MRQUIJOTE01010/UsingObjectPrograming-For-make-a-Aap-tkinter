import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.geometry("400x300")
        master.title("Registro de usuario")

        self.usuario = "Micha"
        self.password = "1998"

        self.separador1 = tk.Frame(master, height=25)
        self.separador1.pack()

        self.etiqueta_usuario = tk.Label(master, text="Usuario")
        self.etiqueta_usuario.pack()

        self.input_usuario = tk.Entry(master)
        self.input_usuario.pack()

        self.separador2 = tk.Frame(master, height=20)
        self.separador2.pack()

        self.etiqueta_password = tk.Label(master, text="Password")
        self.etiqueta_password.pack()

        self.input_password = tk.Entry(master)
        self.input_password.pack()

        self.mensaje = tk.Label(master)

        self.separador3 = tk.Frame(master, height=20)
        self.separador3.pack()

        self.boton_ingresar = tk.Button(master, text="Haz click aquí", command=self.capturar_credenciales)
        self.boton_ingresar.pack()

        self.separador4 = tk.Frame(master, height=20)
        self.separador4.pack()

        self.boton_salir = tk.Button(master, text="Salir", command=master.quit)
        self.boton_salir.pack()

    def capturar_credenciales(self):
        USUARIO = self.input_usuario.get()
        PASSWORD = self.input_password.get()

        if self.usuario == USUARIO and self.password == PASSWORD:
            self.mensaje.config(text="Usuario correcto, su ingreso ha sido exitoso sea Bienvenido", foreground="green")
            self.mensaje.pack()
        else:
            self.mensaje.config(text="Ingreso incorrecto, revise su contraseña o usuario", foreground="red")
            self.mensaje.pack()
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop() 
