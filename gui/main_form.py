from tkinter import *
from pathlib import Path
import gui.login_gui as login_form
import os

#region STATIC
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_FOLDER = os.path.join(CURRENT_DIR, "../assets")
LOGO_ICON = os.path.join(ASSETS_FOLDER,"LAlogo.ico")

#endregion

def create_gui():

    root = Tk() #inicialize
    root.title('LA Warehouse')
    root.iconbitmap(LOGO_ICON)

    root.geometry("400x200")
    root['background'] = 'white'

    def open_packskid():
        login_form.call_login_form(LOGO_ICON,'pack_skid')
    def open_admit_boxes():
        login_form.call_login_form(LOGO_ICON,'open_container')

    # pack_skid_btn = Button(root,text='Click me', padx=50, command=open_packskid).grid(row=0,column=0) #padx - width , pady - height of button
    # admit_boxes_btn = Button(root, text='Admin boxes', padx=50, command=open_admit_boxes).grid(row=0,column=0)

    Label(root, text='', bg='white').pack()
    Button(root,text='Pack skid', width=20, command=open_packskid).pack() #padx - width , pady - height of button
    Label(root, text='', bg='white').pack()
    Button(root, text='Admin boxes',width=20, command=open_admit_boxes).pack()
    Label(root, text='', bg='white').pack()
    root.mainloop()