import os
# tkinter is a Python GUI tool.
import tkinter as tk
from tkinter.filedialog import askdirectory
import tkinter.ttk as ttk

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


def update_fields():
    num_list_var.get()


# Make the window.
window = tk.Tk()
window.title("Image Sorter 1.0")
window.minsize(250, 120)

# Open the window in the center of the screen.
horizontal_position = int(window.winfo_screenwidth()/2 - window.winfo_reqwidth())
vertical_position = int(window.winfo_screenheight()/2 - window.winfo_reqheight())
window.geometry('+{}+{}'.format(horizontal_position, vertical_position))

frame_main = tk.Frame()
#frame_main.grid_rowconfigure([0, 1], weight=1)
#frame_main.grid_columnconfigure([0, 1], weight=1)
frame_main.pack()

# Label widgets display text and images on the window. Use .pack() to get it onto the window.
lbl_main_directory_request = tk.Label(master=frame_main, text="Location to create Images folder:")
lbl_main_directory_request.pack()

# Make a frame to put the entry box and button in so they can be together :)
frame_main_dir_request = tk.Frame(master=frame_main)
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

frame_entry_num = tk.Frame(master=frame_main)
frame_entry_num.pack()
# Add a category number input field that will generate the appropriate number of entries in the next section.
lbl_cat_num_request = tk.Label(master=frame_entry_num, text="Categories:")
lbl_cat_num_request.grid(row=0, column=0, padx=3)
# Make a list of possible categories (1 to 20 in this case) and make a dropdown menu to select desired
# number of categories. Default is set to 1 (num_list[0])
num_list = list(range(1, 21))
num_list_var = tk.StringVar(frame_entry_num)
menu_num = ttk.OptionMenu(frame_entry_num, num_list_var, num_list[0], *num_list)
menu_num.grid(row=0, column=1, padx=3)
# Bind category number dropdown changes to a method that changes the number of fields displayed.
num_list_var.trace_add('write', lambda *args: update_fields())

frame_generated_entries = tk.Frame(master=frame_main)
frame_generated_entries.pack()

# Add a Sort and Quit button.
frame_end_button = tk.Frame(master=frame_main)
frame_end_button.pack()
btn_run = tk.Button(master=frame_end_button, text="Sort", command=lambda: window.destroy())  # fix this later
btn_run.grid(row=1, column=0, padx=3, pady=5)

btn_quit = tk.Button(master=frame_end_button, text="Quit", command=lambda: window.destroy())
btn_quit.grid(row=1, column=1, padx=3, pady=5)

# Show the window.
window.mainloop()


# Use this to get main dir in the main entry field.
#    main_directory = entry_main.get()
#    print(main_directory)
