import os
import glob
from tkinter import *


class Aplication:
    def __init__(self, master=None):
        # Main container
        self.main_container = Frame(master)
        self.main_container["pady"] = 15
        self.main_container["padx"] = 25
        self.main_container["bg"] = "#ebedee"
        self.main_container.pack()

        # Secondary container
        self.second_container = Frame(master)
        self.second_container["pady"] = 5
        self.second_container["padx"] = 25
        self.second_container["bg"] = "#ebedee"
        self.second_container.pack()

        # Third container
        self.third_container = Frame(master)
        self.third_container["pady"] = 15
        self.third_container["padx"] = 25
        self.third_container["bg"] = "#ebedee"
        self.third_container.pack()

        # Main container

        # Browser message
        self.browser_title = Label(self.main_container, text="Navegue para o diretório onde deseja executar a limpeza:",
                                   pady=10, background="#ebedee")
        self.browser_title.pack()

        # Button for search
        self.btn_search = Button(self.main_container, text="Buscar", background="#9dc419")
        self.btn_search.pack(side=RIGHT)

        # Label for current directory
        self.print_current_directory = Label(self.main_container, text=os.getcwd(), background="#ebedee")
        self.print_current_directory.pack(side=LEFT)

        # End of Main container

        # Second container

        # Input character message
        self.input_title = Label(self.second_container, text="Defina quais arquivos deseja remover filtrando por "
                                                             "caracteres:", pady=10, background="#ebedee")
        self.input_title.pack()

        self.input_examples = Label(self.second_container, text="use examples: x*.jpg and (2).jpg", background="#ebedee")
        self.input_examples.pack()

        # Input character
        self.input_character = Entry(self.second_container)
        self.input_character.pack()

        # End of Second container

        # Third container

        # Button Rip
        self.btn_rip = Button(self.third_container, text="RIP", background="#9dc419", width=8, command=self.to_cleaner)
        self.btn_rip.pack()

    # Methods
    def to_cleaner(self):
        for self.file in glob.glob(self.receive_cleaner()):
            print(self.file)
            os.remove(self.file)

    def receive_cleaner(self):
        return self.input_character.get()


root = Tk()
root.title("SRF (Simple Rip Files)")
root["bg"] = "#ebedee"
Aplication(root)
root.mainloop()