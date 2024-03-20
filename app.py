import tkinter as tk
from tkinter import font
import gui.login_window as login_window


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.defaultFont = font.nametofont("TkDefaultFont")

        self.defaultFont.configure(family="Helvetica", size=12)


root = tk.Tk()
text = tk.Text(root)
root.wm_title("Husky Vault")
app = Window(root)

loginWindow = login_window.LoginWindow(root)
loginWindow.loginFrame.place(rely=.5, anchor="w")

root.mainloop()
