import tkinter as tk

def callback():
    pass


def search_word(key):
    if(key):
        # db에서 단어 가져오기
        pass
    else:
        #해당 단어는 db에 엢다고 출력하기
        pass

root = tk.Tk()
root.title("Search Word")

# Create labels and entry fields for id and password
label_word = tk.Label(root, text="검색할 단어")
label_word.grid(row=0, column=0, padx=5, pady=5)
entry_word = tk.Entry(root)
entry_word.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(root, text="Search", command=lambda: callback())
search_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()