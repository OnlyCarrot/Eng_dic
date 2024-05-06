import tkinter as tk
from tkinter import messagebox
from Register import open_signup_window

def login(username, password):
    # Check if the username and password match a predefined value
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Login")

    # Create labels and entry fields for username and password
    label_username = tk.Label(root, text="Username:")
    label_username.grid(row=0, column=0, padx=5, pady=5)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1, padx=5, pady=5)

    label_password = tk.Label(root, text="Password:")
    label_password.grid(row=1, column=0, padx=5, pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1, padx=5, pady=5)

    # Create a login button
    login_button = tk.Button(root, text="Login", command=lambda: login(entry_username.get(), entry_password.get()))
    login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Create a signup button
    signup_button = tk.Button(root, text="Sign up", command=lambda: open_signup_window())
    signup_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
