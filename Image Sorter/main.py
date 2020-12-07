import os
# tkinter is a Python GUI tool.
import tkinter as tk
from tkinter.filedialog import askdirectory

desktop = os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'))

# Use to change the path in an entry field after user has selected another path.
def change_entry_text(entry, text):
    entry.configure(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, text)
    entry.configure(state="readonly")

# Use to ask the user for directory where main Images folder will be created.
def get_main_directory():
    main_directory_holder = askdirectory(initialdir=desktop, title='Choose a location...')
    if os.path.exists(main_directory_holder):
        change_entry_text(entry_main, main_directory_holder)
    else:
        pass

# Make the window.
window = tk.Tk()
window.title("Image Sorter 1.0")

# Label widgets display text and images on the window. Use .pack() to get it onto the window.
lbl_main_directory_request = tk.Label(text="Location to create Images folder:")
lbl_main_directory_request.pack()

# Add an input field to window that will display main directory location. To avoid path validity problems,
# we're just not going to allow the user to edit the text in the entry widget.
entry_main = tk.Entry()
entry_main.insert(0, desktop)
entry_main.configure(state="readonly")
entry_main.pack()

# Add a button that will prompt the user to choose a file location.
btn_choose_dir = tk.Button(text="Choose...", command=lambda: get_main_directory())
btn_choose_dir.pack()

lbl_cat_num_request = tk.Label(text="Categories:")
lbl_cat_num_request.pack()
entry_num = tk.Entry()
entry_num.insert(0, "5")
entry_num.pack()


btn_run = tk.Button(text="Sort", command=lambda: window.destroy()) #fix this later
btn_run.pack(side=tk.LEFT)

btn_quit = tk.Button(text="Quit", command=lambda: window.destroy())
btn_quit.pack()

# Show the window.
window.mainloop()


# Use this to get main dir in the main entry field.
#    main_directory = entry_main.get()
#    print(main_directory)
