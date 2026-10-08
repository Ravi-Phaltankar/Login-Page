import tkinter as tk
from tkinter import messagebox

from database import reset_password

from styles import (
    BG_COLOR,
    CARD_COLOR,
    INPUT_COLOR,
    TEXT_COLOR,
    SECONDARY_TEXT,
    ACCENT_COLOR,
    BUTTON_COLOR
)


class ForgotPasswordWindow:

    def __init__(self, parent):

        self.window = tk.Toplevel(parent)

        self.window.title(
            "Reset Password"
        )

        self.window.geometry(
            "500x600"
        )

        self.window.resizable(
            False,
            False
        )

        self.window.configure(
            bg=BG_COLOR
        )

        self.create_ui()


    def create_ui(self):

        card = tk.Frame(
            self.window,
            bg=CARD_COLOR,
            width=380,
            height=500
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )


        tk.Label(
            card,
            text="Reset Password",
            font=("Segoe UI", 24, "bold"),
            fg=TEXT_COLOR,
            bg=CARD_COLOR
        ).pack(
            pady=(40, 8)
        )


        tk.Label(
            card,
            text="Verify your account and set a new password",
            font=("Segoe UI", 10),
            fg=SECONDARY_TEXT,
            bg=CARD_COLOR,
            wraplength=290
        ).pack(
            pady=(0, 30)
        )


        self.username_entry = self.add_field(
            card,
            "Username"
        )


        self.email_entry = self.add_field(
            card,
            "Email"
        )


        self.password_entry = self.add_field(
            card,
            "New Password",
            True
        )


        self.confirm_entry = self.add_field(
            card,
            "Confirm Password",
            True
        )


        tk.Button(
            card,
            text="RESET PASSWORD",
            command=self.reset,
            font=("Segoe UI", 11, "bold"),
            bg=BUTTON_COLOR,
            fg="white",
            activebackground="#1d4ed8",
            relief="flat",
            borderwidth=0,
            cursor="hand2"
        ).pack(
            fill="x",
            padx=45,
            ipady=12,
            pady=(8, 15)
        )


        tk.Button(
            card,
            text="Back to Login",
            command=self.window.destroy,
            font=("Segoe UI", 9),
            bg=CARD_COLOR,
            fg=ACCENT_COLOR,
            activebackground=CARD_COLOR,
            relief="flat",
            borderwidth=0,
            cursor="hand2"
        ).pack()


    def add_field(
        self,
        parent,
        label,
        password=False
    ):

        tk.Label(
            parent,
            text=label,
            font=("Segoe UI", 10, "bold"),
            fg=TEXT_COLOR,
            bg=CARD_COLOR
        ).pack(
            anchor="w",
            padx=45
        )


        entry = tk.Entry(
            parent,
            font=("Segoe UI", 12),
            bg=INPUT_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat",
            show="*" if password else ""
        )


        entry.pack(
            fill="x",
            padx=45,
            ipady=9,
            pady=(6, 13)
        )


        return entry


    def reset(self):

        username = self.username_entry.get().strip()

        email = self.email_entry.get().strip()

        password = self.password_entry.get()

        confirm = self.confirm_entry.get()


        if not username or not email or not password or not confirm:

            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields.",
                parent=self.window
            )

            return


        if password != confirm:

            messagebox.showerror(
                "Password Error",
                "Passwords do not match.",
                parent=self.window
            )

            return


        if len(password) < 6:

            messagebox.showwarning(
                "Weak Password",
                "Password must contain at least 6 characters.",
                parent=self.window
            )

            return


        success, message = reset_password(
            username,
            email,
            password
        )


        if success:

            messagebox.showinfo(
                "Password Reset",
                message,
                parent=self.window
            )

            self.window.destroy()

        else:

            messagebox.showerror(
                "Reset Failed",
                message,
                parent=self.window
            )