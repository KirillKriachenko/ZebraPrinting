from tkinter import *
from pathlib import Path
import gui.packskid_gui as packskid_form
from odoo_api import  la_odoo_api
from tkinter import messagebox
import os

def call_login_form(icon_path, choosen_option):
    login_form = Toplevel()
    login_form.title('LA Login')
    login_form.iconbitmap(icon_path)

    login_form.geometry("400x200")
    login_form['background'] = 'white'

    Label(login_form, text='Login: ', bg='white').pack()
    login_entry = Entry(login_form)
    login_entry.pack()
    Label(login_form, text='', bg='white').pack()
    Label(login_form, text='Password: ', bg='white').pack()
    password_entry = Entry(login_form, show="*")
    password_entry.pack()
    Label(login_form, text='', bg='white').pack()

    def login():
        email = login_entry.get()
        password = password_entry.get()
        user = la_odoo_api.check_login_user(email,password)
        if user:
            print('success')
            if choosen_option == 'pack_skid':
                packskid_form.open_packskid_main_window(icon_path,user)
                login_form.destroy()
        else:
            # message type: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
            messagebox.showinfo("Authentication failed","User doesn't exist. \n Check your email and password.")


    Button(login_form,text='Login', width=20, command=login).pack() #padx - width , pady - height of button
    login_form.mainloop()