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


def get_search_directory():
    search_directory_holder = askdirectory(initialdir=desktop, title='Choose a location...')
    if os.path.exists(search_directory_holder):
        change_entry_text(entry_search, search_directory_holder)
    else:
        pass


# Change fields for prefix/subfolder dynamically as user selects number from dropdown.
def update_fields():
    lbl_entry_field_1.grid_forget()
    lbl_entry_field_2.grid_forget()
    for i in range(20):
        entry_field_prefix[i].grid_forget()
        entry_field_folder[i].grid_forget()
    chosen_fields = num_list_var.get()
    for i in range(0, int(chosen_fields)):
        lbl_entry_field_1.grid(row=0, column=0, padx=3)
        entry_field_prefix[i].grid(row=2 + i, column=0, padx=3, pady=2)
        lbl_entry_field_2.grid(row=0, column=1, padx=3)
        entry_field_folder[i].grid(row=2 + i, column=1, padx=3, pady=2)
    window.minsize(300, 291 + (int(chosen_fields)*24))

# Create a settings file so variables can persist between openings.
def save_prefs():
    current_file_path = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(os.path.join(current_file_path, 'image_sorter_prefs.txt')), 'w') as prefs:
        prefs.write(entry_main.get() + "\n")
        prefs.write(entry_folder_name.get() + "\n")
        prefs.write(entry_search.get() + "\n")
        prefs.write(num_list_var.get() + "\n")
        for i in entry_field_prefix:
            prefs.write(entry_field_prefix[i].get() + "\n")
        for j in entry_field_folder:
            prefs.write(entry_field_folder[j].get() + "\n")


# Check if a settings file exists and load the variables from that file if so.
def on_startup_prefs_check():
    current_file_path = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(os.path.join(current_file_path, 'image_sorter_prefs.txt')), 'r') as prefs:
        saved_list = prefs.readlines()
        for i in range(len(saved_list)):
            saved_list[i] = saved_list[i].rstrip('\r\n')
        entry_main.configure(state="normal")
        entry_main.delete(0, tk.END)
        entry_main.insert(0, saved_list[0])
        entry_main.configure(state="readonly")
        entry_folder_name.delete(0, tk.END)
        entry_folder_name.insert(0, saved_list[1])
        entry_search.configure(state="normal")
        entry_search.delete(0, tk.END)
        entry_search.insert(0, saved_list[2])
        entry_search.configure(state="readonly")
        num_list_var.set(saved_list[3])
        prefix_counter = 4
        folder_counter = 24
        for i in range(0, len(entry_field_prefix)):
            entry_field_prefix[i].insert(0, saved_list[prefix_counter])
            prefix_counter += 1
        for j in range(0, len(entry_field_folder)):
            entry_field_folder[j].insert(0, saved_list[folder_counter])
            folder_counter += 1


# Check if files are images, move file to appropriate category subfolder. Popup and stop if filename is taken.
def sort_files():
    chosen_fields = num_list_var.get()
    main_file_location = os.path.join(os.path.join(entry_main.get(), entry_folder_name.get()))
    search_file_location = entry_search.get()
    imglist = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.tiff', '.tif', '.bmp']
    for i in range(int(chosen_fields)):
        if not os.path.isdir(os.path.join(os.path.join(main_file_location, entry_field_folder[i].get()))):
            try:
                os.makedirs(os.path.join(os.path.join(main_file_location, entry_field_folder[i].get())))
            except FileExistsError:
                pass
    for file in os.listdir(search_file_location):
        if os.path.splitext(file)[1].lower() in imglist:
            for i in range(int(chosen_fields)):
                if file.startswith(entry_field_prefix[i].get()):
                    try:
                        end_path = os.path.join(os.path.join(main_file_location, entry_field_folder[i].get()))
                        os.rename(os.path.join(os.path.join(search_file_location, file)),
                                  os.path.join(os.path.join(end_path, file)))
                    except:
                        popup_warning(file)
                        raise SystemExit
    popup_complete()


def popup_warning(file):
    popup = tk.Tk()
    popup.title("Warning")
    popup.minsize(300, 100)
    frame_popup = tk.Frame(master=popup, padx=10, pady=5)
    frame_popup.pack(expand=True)
    warning_text = tk.Label(master=frame_popup, text='There is already a file with the name ' + file +
                                                     '\nin the destination folder. The process terminated.')
    warning_text.pack()
    btn_quit_warning = tk.Button(master=frame_popup, text="Close", command=lambda: popup.destroy())
    btn_quit_warning.pack(pady=5)
    horizontal_pop = int(popup.winfo_screenwidth() / 2 - (popup.winfo_reqwidth()))
    vertical_pop = int(popup.winfo_screenheight() / 2 - (popup.winfo_reqheight() / 2))
    popup.geometry('+{}+{}'.format(horizontal_pop, vertical_pop))
    popup.mainloop()


def popup_complete():
    popup_fin = tk.Tk()
    popup_fin.title("Sorting complete!")
    popup_fin.minsize(150, 100)
    frame_popup_fin = tk.Frame(master=popup_fin)
    frame_popup_fin.pack(expand=True)
    finished_text = tk.Label(master=frame_popup_fin, text='Sorting complete!')
    finished_text.pack()
    btn_quit_fin = tk.Button(master=frame_popup_fin, text="Close", command=lambda: popup_fin.destroy())
    btn_quit_fin.pack(pady=5)
    horizontal_pop_fin = int(popup_fin.winfo_screenwidth() / 2 - (popup_fin.winfo_reqwidth() / 1.6))
    vertical_pop_fin = int(popup_fin.winfo_screenheight() / 2 - (popup_fin.winfo_reqheight() / 2))
    popup_fin.geometry('+{}+{}'.format(horizontal_pop_fin, vertical_pop_fin))
    popup_fin.mainloop()


# Make the window.
window = tk.Tk()
window.title("Image Sorter 1.0")
frame_master = tk.Frame(padx=10, pady=5)
frame_master.pack(expand=True)

# Open the window in the center of the screen.
horizontal_position = int(window.winfo_screenwidth()/2 - window.winfo_reqwidth())
vertical_position = int(window.winfo_screenheight()/2 - window.winfo_reqheight())
window.geometry('+{}+{}'.format(horizontal_position, vertical_position))

frame_top = tk.Frame(master=frame_master, bd=2, relief=tk.GROOVE, padx=5, pady=5)
frame_top.pack(pady=(5,0))
# Label widgets display text and images on the window. Use .pack() to get it onto the window.
lbl_main_directory_request = tk.Label(master=frame_top, text="Location of main folder:")
lbl_main_directory_request.pack()
# Make a frame to put the entry box and button in so they can be together :)
frame_main_dir_request = tk.Frame(master=frame_top)
frame_main_dir_request.pack()
# Add an input field to window that will display main directory location. To avoid path validity problems,
# we're just not going to allow the user to edit the text in the entry widget.
entry_main = tk.Entry(master=frame_main_dir_request)
entry_main.insert(0, desktop)
entry_main.configure(state="readonly")
entry_main.grid(row=1, column=0, ipadx=20, padx=3)
# Add a button that will prompt the user to choose a file location.
btn_choose_dir = tk.Button(master=frame_main_dir_request, text="Choose...", command=lambda: get_main_directory())
btn_choose_dir.grid(row=1, column=1, padx=3)


frame_mid = tk.Frame(master=frame_master, padx=5, pady=5)
frame_mid.pack(pady=(0,5))
lbl_folder_name_request = tk.Label(master=frame_mid, text="Name of main folder \n (will be created if does not exist):")
lbl_folder_name_request.pack()
entry_folder_name = tk.Entry(master=frame_mid)
entry_folder_name.insert(0, 'Images')
entry_folder_name.pack()

frame_bot = tk.Frame(master=frame_master, bd=2, relief=tk.GROOVE, padx=5, pady=5)
frame_bot.pack()
lbl_search_dir_request = tk.Label(master=frame_bot, text="Location of items to be sorted:")
lbl_search_dir_request.pack()
frame_search_dir_request = tk.Frame(master=frame_bot)
frame_search_dir_request.pack()
entry_search = tk.Entry(master=frame_search_dir_request)
entry_search.insert(0, desktop)
entry_search.configure(state="readonly")
entry_search.grid(row=1, column=0, ipadx=20, padx=3)
btn_choose_s_dir = tk.Button(master=frame_search_dir_request, text="Choose...", command=lambda: get_search_directory())
btn_choose_s_dir.grid(row=1, column=1, padx=3)

frame_entry_num = tk.Frame(master=frame_master)
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

# Set up some dictionaries for dynamic updating window based on input. Will be able to retrieve inputs later.
frame_generated_entries = tk.Frame(master=frame_master)
entry_field_prefix = {}
entry_field_folder = {}
lbl_entry_field_1 = tk.Label(master=frame_generated_entries, text="Images with prefix:")
lbl_entry_field_2 = tk.Label(master=frame_generated_entries, text="Will go in category:")
for i in range(20):
    entry_field_prefix[i] = tk.Entry(master=frame_generated_entries)
    entry_field_folder[i] = tk.Entry(master=frame_generated_entries)
update_fields()
frame_generated_entries.pack()

# Add a Save Settings, Sort, and Quit button.
frame_end_button = tk.Frame(master=frame_master)
frame_end_button.pack()
btn_run = tk.Button(master=frame_end_button, text="Save Prefs", command=lambda: save_prefs())
btn_run.grid(row=1, column=0, padx=3, pady=5)

btn_save = tk.Button(master=frame_end_button, text="Sort Images", command=lambda: sort_files())
btn_save.grid(row=1, column=1, padx=3, pady=5)

btn_quit = tk.Button(master=frame_end_button, text="Quit Program", command=lambda: window.destroy())
btn_quit.grid(row=1, column=2, padx=3, pady=5)

on_startup_prefs_check()
# Show the window.
window.mainloop()


# Use this to get main dir in the main entry field.
#    main_directory = entry_main.get()
#    print(main_directory)
