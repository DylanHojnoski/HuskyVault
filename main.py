import tkinter as tk
import src.loginPage as loginPage


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master


root = tk.Tk()
root.wm_title("Husky Vault")
app = Window(root)

loginPage = loginPage.LoginPage(root)
loginPage.loginFrame.place(rely=.5, anchor="w")

root.mainloop()
