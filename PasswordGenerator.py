import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring


class PasswordGenerator:
    def __init__(self, window):
        #self.generate_password()
        window.title("Parooligeneraator")
        window_width = 300
        window_height = 300
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        window.geometry(f'{window_width}x{window_height}+{x}+{y}')


        #Loome framed
        self.frame = tk.Frame(window, background='lightblue')
        self.frame.pack(fill=tk.BOTH)

        self.frame2 = tk.Frame(window, background='lightyellow')
        self.frame2.pack(fill=tk.BOTH)

        #Loo vidinad (Widgets)
        self.lbl_previous = self.all_widgets()



    def all_widgets(self):
        tk.Label(self.frame, text='Vali parooli tingimused:', background='lightblue').pack(side=tk.TOP, padx=3, pady=3)  # Label luuakse, pannakse ja sinna jääb #padx ja pady kui palju ruumi jätta

        self.password_length = None
        self.add_symbols_var = tk.BooleanVar()
        self.add_numbers_var = tk.BooleanVar()
        self.add_capital_letters_var = tk.BooleanVar()


        checkbox_symbols = tk.Checkbutton(self.frame, text="Sisaldab sümboleid", variable=self.add_symbols_var, background='lightblue')
        checkbox_symbols.pack(anchor=tk.CENTER)

        checkbox_numbers = tk.Checkbutton(self.frame, text="Sisaldab numbreid", variable=self.add_numbers_var, background='lightblue')
        checkbox_numbers.pack(anchor=tk.CENTER)

        checkbox_capital_letters = tk.Checkbutton(self.frame, text="Sisaldab suuri tähti", variable=self.add_capital_letters_var, background='lightblue')
        checkbox_capital_letters.pack(anchor=tk.CENTER)

        # Nupp (Button)
        btn_submit = tk.Button(self.frame, text='Näita', command=self.generate_password)
        btn_submit.pack(side=tk.BOTTOM, padx=3, pady=3)
        btn_length = tk.Button(self.frame, text='Pikkus', command=self.ask_length)
        btn_length.pack(side=tk.BOTTOM, padx=3, pady=3)

        lbl_PASSWORD = tk.Label(self.frame2, text='PAROOL: ', background='lightyellow')
        lbl_PASSWORD.grid(row=0, column=0)
        self.lbl_password2 = tk.Label(self.frame2, text='', background='lightyellow')
        self.lbl_password2.grid(row=0, column=1)

        return lbl_PASSWORD, self.lbl_password2

    def ask_length(self):
        password_length = askstring('Parooli pikkus.', 'Mis on parooli pikkus?(1-100)')
        #print(password_length)
        if password_length is None:
            return
        try:
            self.password_length = int(password_length)
            if not 1 <= self.password_length <= 100:
                raise ValueError('Parooli pikkus on vale, sisesta pikkus vahemikus 1-100')
        except ValueError as e:
            messagebox.showerror('Viga', f'{e}')

    def get_character_pool(self):
        characters = string.ascii_lowercase #Väiketähed vaikimisi
        if self.add_symbols_var.get():
            characters += string.punctuation
        if self.add_numbers_var.get():
            characters += string.digits
        if self.add_capital_letters_var.get():
            characters += string.ascii_uppercase

        if not characters:
            messagebox.showerror('Viga!', 'Vali tingimused')
            return None
        #print(characters)
        return characters


    def generate_password(self):
        if self.password_length is None:
            self.password_length = 12

        characters = self.get_character_pool()

        password = ''.join(random.choice(characters) for _ in range(self.password_length))
        self.lbl_password2['text'] = password
        #print(password)
        return password


