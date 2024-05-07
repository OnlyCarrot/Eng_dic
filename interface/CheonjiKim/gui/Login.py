import tkinter as tk
from tkinter import messagebox
from Register import open_signup_window
from LoadVoca import open_voca_window

def login(id, password, window):
    # username parameter를 추가해야 한다. 
    # Check if the id and password match a predefined value
    if id == "admin" and password == "password":
        messagebox.showinfo("alert", f"환영합니다. {id}님!")
        window.destroy()
        open_voca_window()
    
    # elif(1):
    #     # id와 pw가 적절하면
    #     # 환영합니다. id님 출력한다.
    #     pass

    else:
        messagebox.showerror("Login", "Invalid id or password")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Login")

    # Create labels and entry fields for id and password
    label_id = tk.Label(root, text="id:")
    label_id.grid(row=0, column=0, padx=5, pady=5)
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1, padx=5, pady=5)

    label_password = tk.Label(root, text="Password:")
    label_password.grid(row=1, column=0, padx=5, pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1, padx=5, pady=5)

    # Create a login button
    login_button = tk.Button(root, text="Login", command=lambda: login(entry_id.get(), entry_password.get(), root))
    login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Create a signup button
    signup_button = tk.Button(root, text="Sign up", command=lambda: open_signup_window())
    signup_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
