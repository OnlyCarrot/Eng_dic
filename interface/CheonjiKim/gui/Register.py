import tkinter as tk
from tkinter import messagebox

def signup(id, password, confirm_password, signup_window):
    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Password Error", "Passwords do not match!")
        return

    # Placeholder function for sign up functionality
    # Here you can implement your sign-up logic, such as saving the new user to a database

    # id, pw, id, is_manager, level 여기다가 넣어라.

    messagebox.showinfo("Sign Up", f"Signed up successfully!\nid: {id}\nPassword: {password}")

    # Destroy the sign-up window after successful sign-up
    signup_window.destroy()

def open_signup_window():
    # Create the sign-up window
    signup_window = tk.Tk()
    signup_window.title("Sign Up")

    label_id = tk.Label(signup_window, text="ID:")
    label_id.grid(row=0, column=0, padx=5, pady=5)
    entry_id = tk.Entry(signup_window)
    entry_id.grid(row=0, column=1, padx=5, pady=5)

    label_password = tk.Label(signup_window, text="Password:")
    label_password.grid(row=1, column=0, padx=5, pady=5)
    entry_password = tk.Entry(signup_window, show="*")
    entry_password.grid(row=1, column=1, padx=5, pady=5)

    label_confirm_password = tk.Label(signup_window, text="Confirm Password:")
    label_confirm_password.grid(row=2, column=0, padx=5, pady=5)
    entry_confirm_password = tk.Entry(signup_window, show="*")
    entry_confirm_password.grid(row=2, column=1, padx=5, pady=5)

    label_username = tk.Label(signup_window, text="Username:")
    label_username.grid(row=3, column=0, padx=5, pady=5)
    entry_username = tk.Entry(signup_window, show="*")
    entry_username.grid(row=3, column=1, padx=5, pady=5)
    


    signup_button = tk.Button(signup_window, text="Sign Up", command=lambda: signup(entry_id.get(), entry_password.get(), entry_confirm_password.get(), signup_window))
    signup_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    # Run the Tkinter event loop for the sign-up window
    signup_window.mainloop()

if __name__ == "__main__":
    open_signup_window()
