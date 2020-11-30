from tkinter import *

def open_packskid_main_window(icon_path,user):
    window = Toplevel()
    window.title('LA Pack skid')
    window.iconbitmap(icon_path)

    window.geometry("600x600")
    window['background'] = 'white'

    Label(window,text='Project',bg='white').pack()
    project_options = user.get_projects()
    clicked = StringVar()
    clicked.set(project_options[0])
    drop = OptionMenu(window,clicked,*project_options)
    drop.pack()