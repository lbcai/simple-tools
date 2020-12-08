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

# Make a frame to put the entry box and button in so they can be together :)
frame_main_dir_request = tk.Frame()
frame_main_dir_request.pack()
# Add an input field to window that will display main directory location. To avoid path validity problems,
# we're just not going to allow the user to edit the text in the entry widget.
entry_main = tk.Entry(master=frame_main_dir_request)
entry_main.insert(0, desktop)
entry_main.configure(state="readonly")
entry_main.grid(row=1, column=0, padx=3)

# Add a button that will prompt the user to choose a file location.
btn_choose_dir = tk.Button(master=frame_main_dir_request, text="Choose...", command=lambda: get_main_directory())
btn_choose_dir.grid(row=1, column=1, padx=3)

lbl_cat_num_request = tk.Label(text="Categories (1 to 20):")
lbl_cat_num_request.pack()
entry_num = tk.Entry()
entry_num.insert(0, "5")
entry_num.pack()

frame_end_button = tk.Frame()
frame_end_button.pack()
btn_run = tk.Button(master=frame_end_button, text="Sort", command=lambda: window.destroy()) # fix this later
btn_run.grid(row=1, column=0, padx=3, pady=5)

btn_quit = tk.Button(master=frame_end_button, text="Quit", command=lambda: window.destroy())
btn_quit.grid(row=1, column=1, padx=3, pady=5)

# Show the window.
window.mainloop()


# Use this to get main dir in the main entry field.
#    main_directory = entry_main.get()
#    print(main_directory)
