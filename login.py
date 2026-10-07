import tkinter as tk
from tkinter import messagebox

from database import authenticate_user
from styles import (
    BG_COLOR,
    CARD_COLOR,
    INPUT_COLOR,
    TEXT_COLOR,
    SECONDARY_TEXT,
    ACCENT_COLOR,
)


class LoginApp:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Login Page")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        self.create_ui()

    def create_ui(self):
        # Main card
        card = tk.Frame(
            self.root,
            bg=CARD_COLOR,
            width=380,
            height=480
        )
        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Title
        tk.Label(
            card,
            text="Welcome Back",
            font=("Segoe UI", 24, "bold"),
            fg=TEXT_COLOR,
            bg=CARD_COLOR
        ).pack(pady=(45, 8))

        # Subtitle
        tk.Label(
            card,
            text="Login to your account",
            font=("Segoe UI", 11),
            fg=SECONDARY_TEXT,
            bg=CARD_COLOR
        ).pack(pady=(0, 35))

        # Username
        tk.Label(
            card,
            text="Username",
            font=("Segoe UI", 10, "bold"),
            fg=TEXT_COLOR,
            bg=CARD_COLOR
        ).pack(anchor="w", padx=45)

        self.username_entry = tk.Entry(
            card,
            font=("Segoe UI", 12),
            bg=INPUT_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat"
        )

        self.username_entry.pack(
            fill="x",
            padx=45,
            ipady=10,
            pady=(8, 20)
        )

        # Password
        tk.Label(
            card,
            text="Password",
            font=("Segoe UI", 10, "bold"),
            fg=TEXT_COLOR,
            bg=CARD_COLOR
        ).pack(anchor="w", padx=45)

        password_frame = tk.Frame(
            card,
            bg=INPUT_COLOR
        )

        password_frame.pack(
            fill="x",
            padx=45,
            pady=(8, 10)
        )

        self.password_entry = tk.Entry(
            password_frame,
            font=("Segoe UI", 12),
            bg=INPUT_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            show="*",
            relief="flat"
        )

        self.password_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=10,
            padx=(10, 0)
        )

        self.show_button = tk.Button(
            password_frame,
            text="Show",
            command=self.toggle_password,
            bg=INPUT_COLOR,
            fg=ACCENT_COLOR,
            activebackground=INPUT_COLOR,
            activeforeground=ACCENT_COLOR,
            relief="flat",
            borderwidth=0,
            cursor="hand2"
        )

        self.show_button.pack(
            side="right",
            padx=8
        )

        # Forgot password
        tk.Button(
            card,
            text="Forgot Password?",
            font=("Segoe UI", 9),
            bg=CARD_COLOR,
            fg=ACCENT_COLOR,
            activebackground=CARD_COLOR,
            activeforeground=ACCENT_COLOR,
            relief="flat",
            borderwidth=0,
            cursor="hand2"
        ).pack(
            anchor="e",
            padx=45,
            pady=(0, 25)
        )

        # Login button
        tk.Button(
            card,
            text="LOGIN",
            command=self.login,
            font=("Segoe UI", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            cursor="hand2"
        ).pack(
            fill="x",
            padx=45,
            ipady=12
        )

        # Register
        register_frame = tk.Frame(
            card,
            bg=CARD_COLOR
        )

        register_frame.pack(pady=25)

        tk.Label(
            register_frame,
            text="Don't have an account?",
            font=("Segoe UI", 9),
            fg=SECONDARY_TEXT,
            bg=CARD_COLOR
        ).pack(side="left")

        tk.Button(
            register_frame,
            text=" Sign Up",
            font=("Segoe UI", 9, "bold"),
            bg=CARD_COLOR,
            fg=ACCENT_COLOR,
            activebackground=CARD_COLOR,
            activeforeground=ACCENT_COLOR,
            relief="flat",
            borderwidth=0,
            cursor="hand2"
        ).pack(side="left")

        # Enter key
        self.root.bind(
            "<Return>",
            lambda event: self.login()
        )

        self.username_entry.focus()

    def toggle_password(self):
        if self.password_entry.cget("show") == "":
            self.password_entry.config(show="*")
            self.show_button.config(text="Show")
        else:
            self.password_entry.config(show="")
            self.show_button.config(text="Hide")

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )
            return

        if authenticate_user(username, password):
            messagebox.showinfo(
                "Login Successful",
                f"Welcome, {username}!"
            )
        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

    def run(self):
        self.root.mainloop()