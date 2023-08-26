import rh_panel
from tkinter import Tk, Label, Button, Entry, ttk, messagebox


def create_user(Windows1):
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry('1024x768')
    Windows.title("Rh_Acesso")
    Windows.iconbitmap("imagens/rh.ico")
    Windows.config(background='white')
    
    txt_tittle = Label(Windows, text="Preencha o Formulário", background="white", font=('Arial', 30))
    txt_tittle.pack(padx=50, pady=50)
    
    txt_name = Label(Windows, text="Nome Completo", background="white", font=('Arial', 20))
    txt_name.pack(padx=10, pady=10)
    inbox_name = Entry(Windows, text="Login", font=('Arial',15), background='white')
    inbox_name.pack(padx=10, pady=10)
    
    txt_mail = Label(Windows, text="Email", background="white", font=('Arial', 20))
    txt_mail.pack(padx=10, pady=10)
    inbox_mail = Entry(Windows, font=('Arial',15), background='white')
    inbox_mail.pack(padx=10, pady=10)
    
    txt_registration = Label(Windows, text="Mátricula", background="white", font=('Arial', 20))
    txt_registration.pack(padx=10, pady=10)
    inbox_registration = Entry(Windows,  font=('Arial',15), background='white')
    inbox_registration.pack(padx=10, pady=10)
    
    txt_sector = Label(Windows, text="Setor", background="white", font=('Arial', 20))
    txt_sector.pack(padx=10, pady=10)
    inbox_sector = Entry(Windows, font=('Arial',15), background='white')
    inbox_sector.pack(padx=10, pady=10)
    
    txt_office = Label(Windows, text="Cargo", background="white", font=('Arial', 20))
    txt_office.pack(padx=10, pady=10)
    inbox_office = Entry(Windows, font=('Arial',15), background='white')
    inbox_office.pack(padx=10, pady=10)
    
    button_exe = Button(Windows, text='Executar', font=('Arial', 20), background='blue', fg='white', width=10)
    button_exe.pack(padx=20, pady=10)
    button_back = Button(Windows, text='Voltar', font=('Arial', 20), background='blue', fg='white', width=10)
    button_back["command"] = lambda button_back=button_back: open_panel(Windows)
    button_back.pack(padx=20, pady=10)
    
def open_panel(self):
    rh_panel.main_panel(self)