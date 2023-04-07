
import tkinter as tk


class MenuScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Restaurante")

        # Creamos el menú superior
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)


        # Creamos las opciones del menú
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Camaron", command=self.open_file)
        self.file_menu.add_command(label="Langosta", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Precios", command=self.quit_program)
        self.menu_bar.add_cascade(label="Comida", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Limonada", command=self.copy)
        self.edit_menu.add_command(label="Horchata", command=self.paste)
        self.menu_bar.add_cascade(label="Bebida", menu=self.edit_menu)


        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="plato de Camaron$250", command=self.open_file)
        self.file_menu.add_command(label="Orden de Langosta$300", command=self.save_file)
        self.file_menu.add_separator()
        self.menu_bar.add_cascade(label="Precios", menu=self.file_menu)

        # Agregamos algunos widgets a la pantalla
        self.label = tk.Label(self, text="¡Hola!,Bienvenido a nuetro restaurante")
        self.label.pack(pady=20)
        self.button = tk.Button(self, text="Aga clik a la opcion de comida o Bebida", command=self.press_button)
        self.button.pack()

        self.pack()

    def open_file(self):
        print("Camaron")

    def save_file(self):
        print("Langosta")

    def quit_program(self):
        self.master.quit()

    def copy(self):
        print("Limonada")

    def paste(self):
        print("Horchata")

    def press_button(self):
        print("Aga clik a la opcion de comida o Bebida")


root = tk.Tk()
root.geometry("420x380")
app = MenuScreen(root)
app.mainloop()
