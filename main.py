import random
import math
import customtkinter
import sys

condition = True

components = ["abcdefghijklmonpqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "@#-_.'!?", "1234567890"]

languages = dict(
    {"Italiano": ["Copia", "Nuova Password", "La password comparirà qui!", "Lettere Minuscole", "Lettere Maiuscole",
                  "Numeri",
                  "Simboli", "Generatore di Password", "Copiato negli Appunti!"],
     "English": ["Copy", "New Password", "The new password will appear here!", "Lowercase Letters", "Uppercase Letters",
                 "Numbers", "Symbols", "Password Generator", "Copied to Clipboard!"]}
)


def start():
    global condition
    condition = True


def stop():
    global condition
    condition = False


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.wm_protocol('WM_DELETE_WINDOW', self.on_close)
        self.stop = True
        self.language = "English"
        self.password_font = customtkinter.CTkFont(size=20)
        self.button_font = customtkinter.CTkFont(size=30, weight="bold")
        self.button_font2 = customtkinter.CTkFont(size=20, weight="bold")
        self.checkbox_font = customtkinter.CTkFont(size=25)
        self.title("")
        self.minsize(1000, 700)
        self.maxsize(1000, 700)
        self.password = ""
        self.frame = customtkinter.CTkFrame(master=self, width=math.floor(self.winfo_width()), height=120,
                                            border_width=2, border_color="#747474")
        self.frame.place(relx=0.12, rely=0.8, anchor="n")
        self.italiano = customtkinter.CTkButton(master=self.frame, text="Italiano", font=self.button_font2,
                                                command=self.on_italiano)
        self.italiano.place(relx=0.5, rely=0.15, anchor="n")
        self.english = customtkinter.CTkButton(master=self.frame, text="English", font=self.button_font2,
                                               command=self.on_english)
        self.english.place(relx=0.5, rely=0.6, anchor="n")
        self.generate_button = customtkinter.CTkButton(master=self, text="", command=self.on_generate, width=300,
                                                       height=100, font=self.button_font)
        self.generate_button.place(relx=0.5, rely=0.1, anchor="n")
        self.copy_button = customtkinter.CTkButton(master=self, text="", command=self.on_copy, width=100,
                                                   height=40, font=self.button_font2, )
        self.copy_label = customtkinter.CTkLabel(master=self, text="",
                                                 font=self.password_font, wraplength=435)
        self.passwordLabel = customtkinter.CTkLabel(master=self, text="",
                                                    font=self.password_font, wraplength=435)
        self.passwordLabel.place(relx=0.5, rely=0.3, anchor="n")
        self.lengthLabel = customtkinter.CTkLabel(master=self,
                                                  text=" 5                                                    100",
                                                  textvariable=self.password, font=self.button_font)
        self.lengthLabel.place(relx=0.5, rely=0.45, anchor="n")
        self.length_slider = customtkinter.CTkSlider(master=self, from_=5, to=100, height=20, width=400,
                                                     command=self.on_length)
        self.current_lengthLabel = customtkinter.CTkLabel(master=self, text=str(round(self.length_slider.get())),
                                                          font=self.checkbox_font)
        self.current_lengthLabel.place(relx=0.5, rely=0.45, anchor="n")
        self.length_slider.place(relx=0.5, rely=0.5, anchor="n")
        self.uppercase_checkbox = customtkinter.CTkCheckBox(master=self, text="",
                                                            font=self.checkbox_font, corner_radius=8, width=100)
        self.uppercase_checkbox.place(relx=0.4, rely=0.6, anchor="w")
        self.lowercase_checkbox = customtkinter.CTkCheckBox(master=self, text="",
                                                            font=self.checkbox_font, corner_radius=8)
        self.lowercase_checkbox.place(relx=0.4, rely=0.7, anchor="w")
        self.numbers_checkbox = customtkinter.CTkCheckBox(master=self, text="", font=self.checkbox_font,
                                                          corner_radius=8)
        self.numbers_checkbox.place(relx=0.4, rely=0.8, anchor="w")
        self.symbols_checkbox = customtkinter.CTkCheckBox(master=self, text="", font=self.checkbox_font,
                                                          corner_radius=8)
        self.symbols_checkbox.place(relx=0.4, rely=0.9, anchor="w")
        self.uppercase_checkbox.select()
        self.uppercase = False
        self.lowercase = False
        self.numbers = False
        self.symbols = False
        self.set_language()

    def on_italiano(self):
        self.language = "Italiano"
        self.set_language()

    def on_english(self):
        self.language = "English"
        self.set_language()

    def set_language(self):
        self.copy_button.configure(text=languages.get(self.language)[0])
        self.generate_button.configure(text=languages.get(self.language)[1])
        if (self.passwordLabel.cget("text") == "") or (" " in self.passwordLabel.cget("text")):
            self.passwordLabel.configure(text=languages.get(self.language)[2])
        self.lowercase_checkbox.configure(text=languages.get(self.language)[3])
        self.uppercase_checkbox.configure(text=languages.get(self.language)[4])
        self.numbers_checkbox.configure(text=languages.get(self.language)[5])
        self.symbols_checkbox.configure(text=languages.get(self.language)[6])
        self.title(languages.get(self.language)[7])
        self.copy_label.configure(text=languages.get(self.language)[8])

    def on_copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.password)
        self.copy_label.place(relx=0.8, rely=0.1, anchor="n")

    def on_length(self, walter_hartwell_white):
        self.current_lengthLabel.configure(text=str(round(self.length_slider.get())))

    def on_generate(self):
        self.options()
        if self.isValid():
            self.new()
            self.passwordLabel.configure(text=self.password)
            self.copy_button.place(relx=0.8, rely=0.14, anchor="n")
            self.copy_label.place_forget()

    def isValid(self):
        return True in (self.lowercase, self.uppercase, self.numbers, self.symbols)

    def options(self):
        self.uppercase = toBoolean(self.uppercase_checkbox.get())
        self.lowercase = toBoolean(self.lowercase_checkbox.get())
        self.numbers = toBoolean(self.numbers_checkbox.get())
        self.symbols = toBoolean(self.symbols_checkbox.get())

    def new(self):
        characters = ""
        self.password = ""
        if self.lowercase:
            characters += components[0]
        if self.uppercase:
            characters += components[1]
        if self.symbols:
            characters += components[2]
        if self.numbers:
            characters += components[3]
        for k in range(round(self.length_slider.get())):
            self.password += characters[random.randint(0, len(characters) - 1)]
        return self.password

    def on_close(self):
        self.stop = False
        self.after(200, sys.exit())


def toBoolean(num):
    if num == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    app = App()
    app.mainloop()
    while stop:
        app.frame.configure()
