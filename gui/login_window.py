import tkinter as tk
from tkinter.messagebox import showerror


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.username = ""
        self.password = ""

        self.loginFrame = tk.Frame(root, width=200, height=400, padx=50, pady=10)

        usernameLabel = tk.Label(self.loginFrame, text="Username")
        usernameLabel.grid(row=0, column=0)
        self.usernameInput = tk.Entry(self.loginFrame, textvariable=self.username)
        self.usernameInput.grid(row=1, column=0, pady=5)

        passwordLabel = tk.Label(self.loginFrame, text="Password")
        passwordLabel.grid(row=2, column=0)
        self.passwordInput = tk.Entry(self.loginFrame, show="*", textvariable=self.password)
        self.passwordInput.grid(row=3, column=0, pady=5)

        login = tk.Button(self.loginFrame, text="Login", bd="2", command=self.authenticate)
        login.grid(row=4, column=0, pady=5)

        createAccount = tk.Button(self.loginFrame, text="Create Account", bd="2", command=self.createAccountPage)
        createAccount.grid(row=5, column=0, pady=5)

    def authenticate(self):
        if len(self.usernameInput.get()) == 0 and len(self.passwordInput.get()) == 0:
            showerror("Login", "Username and password is required")
            return
        elif len(self.usernameInput.get()) == 0:
            showerror("Login", "Username is required")
            return
        elif len(self.passwordInput.get()) == 0:
            showerror("Login", "Password is required")
            return
        else:
            # sql query
            return

    def createAccountPage(self):
        createAccount = CreateAccount(self.root)
        self.loginFrame.destroy()
        createAccount.createAccountFrame.place(rely=.5, anchor="w")


class CreateAccount:
    def __init__(self, root):
        self.root = root
        self.createAccountFrame = tk.Frame(root, width=200, height=400, padx=50, pady=10)

        usernameLabel = tk.Label(self.createAccountFrame, text="Username")
        usernameLabel.grid(row=0, column=0)
        self.usernameInput = tk.Entry(self.createAccountFrame)
        self.usernameInput.grid(row=1, column=0, pady=5)

        passwordLabel = tk.Label(self.createAccountFrame, text="Password")
        passwordLabel.grid(row=2, column=0)
        self.passwordInput = tk.Entry(self.createAccountFrame, show="*")
        self.passwordInput.grid(row=3, column=0, pady=5)

        repeatPasswordLabel = tk.Label(self.createAccountFrame, text="Repeat Password")
        repeatPasswordLabel .grid(row=4, column=0)
        self.repeatPasswordInput = tk.Entry(self.createAccountFrame, show="*")
        self.repeatPasswordInput.grid(row=5, column=0, pady=5)

        createAccount = tk.Button(self.createAccountFrame, text="Create Account", bd="2", command=self.createAccount)
        createAccount.grid(row=6, column=0, pady=5)

        returnToLoginButton = tk.Button(self.createAccountFrame, text="Return To Login", bd="2", command=self.returnToLogin)
        returnToLoginButton.grid(row=7, column=0, pady=5)

    def createAccount(self):
        if self.passwordInput.get() != self.repeatPasswordInput.get():
            showerror("Create Account", "Password and repeat password do not match")
            return
        if len(self.usernameInput.get()) == 0 or len(self.passwordInput.get()) == 0 or len(self.repeatPasswordInput.get()) == 0:
            showerror("Create Account", "Username, password, and repeat password are required")
            return
        else:
            # sql query
            
            self.returnToLogin()
            return

    def returnToLogin(self):
        login = LoginWindow(self.root)
        self.createAccountFrame.destroy()
        login.loginFrame.place(rely=.5, anchor="w")
