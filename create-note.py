import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import os

def create_note():
    note_title = title_entry.get()
    note_format = format_var.get()

    if not note_title:
        status_label.config(text="Enter a note title", fg="red")
        return

    current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    note_name = f"{note_title}.{note_format}"
    
    # Select a folder to save the notes
    folder_path = filedialog.askdirectory()
    if not folder_path:
        status_label.config(text="Select a folder to save the notes", fg="red")
        return

    note_path = os.path.join(folder_path, note_name)
    
    if note_path:
        note_content = note_text.get("1.0", tk.END)

        with open(note_path, 'w', encoding='utf-8') as file:
            file.write(f"Title: {note_title}\nDate and Time: {current_time}\n\n")
            file.write("Content:\n")
            file.write(note_content)

        status_label.config(text=f"Note created: {note_path}", fg="green")
    else:
        status_label.config(text="Note was not created.", fg="red")

# Create the main application window
root = tk.Tk()
root.title("Create Note")

# Adding elements to the interface
title_label = tk.Label(root, text="Note Title:")
title_label.pack()

title_entry = tk.Entry(root)
title_entry.pack()

format_label = tk.Label(root, text="Select Format:")
format_label.pack()

format_var = tk.StringVar()
format_var.set("txt")
format_radio_txt = tk.Radiobutton(root, text="txt", variable=format_var, value="txt")
format_radio_sh = tk.Radiobutton(root, text="sh", variable=format_var, value="sh")
format_radio_txt.pack()
format_radio_sh.pack()

content_label = tk.Label(root, text="Note Content:")
content_label.pack()

# Increase the size of the text input field
note_text = tk.Text(root, height=15, width=50)
note_text.pack()

create_button = tk.Button(root, text="Create Note", command=create_note)
create_button.pack()

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

root.mainloop()
