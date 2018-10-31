# coding: utf-8
import os
import glob
from tkinter import *
from tkinter.filedialog import askdirectory


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
        self.btn_search = Button(self.main_container, text="Buscar", fg="white", background="#2C3E50",
                                 activebackground="#1C2833", activeforeground="white", command=self.browser_dir)
        self.btn_search.pack(side=RIGHT)

        # Entry for current directory
        self.dir_str = StringVar()
        self.txt_output = Entry(self.main_container, width=40, textvariable=self.dir_str)
        self.txt_output.pack(side=LEFT, ipady=3)

        # End of Main container

        # Second container

        # Input character message
        self.input_title = Label(self.second_container, text="Defina quais arquivos deseja remover filtrando por "
                                                             "caracteres:", pady=10, background="#ebedee")
        self.input_title.pack()

        self.input_examples = Label(self.second_container, text="exemplos: x*.jpg ou (2).mp4", background="#ebedee")
        self.input_examples.pack()

        # Input character
        self.input_character = Entry(self.second_container)
        self.input_character.pack()

        # End of Second container

        # Third container

        # Button Rip
        self.btn_rip = Button(self.third_container, text="RIP", fg="white", background="#2C3E50",
                              activebackground="#1C2833", activeforeground="white", width=8, command=self.to_cleaner)
        self.btn_rip.pack()

        # End of Third container

    # Methods
    def to_cleaner(self):
        for self.file in glob.glob(self.receive_cleaner()):
            print(self.file)
            os.remove(self.file)

    def receive_cleaner(self):
        return self.input_character.get()

    def browser_dir(self):
        folder = askdirectory(initialdir='~/Downloads')
        os.chdir(folder)
        self.dir_str = folder
        self.txt_output.delete(0, END)
        self.txt_output.insert(0, self.dir_str)


root = Tk()
root.title("SRF (Simple Rip Files)")
root.geometry('460x280')
root.resizable(0, 0)
root["bg"] = "#ebedee"
Aplication(root)
root.mainloop()