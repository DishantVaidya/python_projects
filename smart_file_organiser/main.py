import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------------------
# Function: Organize all files in a selected folder
# ---------------------------
def organize_files():
    # Get the folder path from the input box
    path = path_entry.get()

    # Check if the entered path exists
    if not os.path.exists(path):
        messagebox.showerror("Error", "Please select a valid folder.")
        return

    # List all items (files + folders) in the selected path
    files = os.listdir(path)

    # If the folder is empty, show a message and stop
    if not files:
        messagebox.showinfo("Info", "The selected folder is empty.")
        return

    # Go through every file in the folder
    for file in files:
        file_path = os.path.join(path, file)  # complete file path

        # Skip if it's a folder (we only want to move files)
        if os.path.isdir(file_path):
            continue

        # Split filename and extension
        filename, extension = os.path.splitext(file)
        extension = extension[1:]  # remove the dot from extension ('.jpg' -> 'jpg')

        # Handle files with no extension
        if extension == "":
            extension = "No Extension"

        # Create a folder for that extension (if it doesn’t already exist)
        folder_path = os.path.join(path, extension)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file into the respective folder
        shutil.move(file_path, os.path.join(folder_path, file))

    # Once done, show a success message
    messagebox.showinfo("Success", "Files organized successfully!")


# ---------------------------
# Function: Open file explorer to pick a folder
# ---------------------------
def browse_folder():
    folder_selected = filedialog.askdirectory()  # opens system folder picker
    path_entry.delete(0, tk.END)                 # clear previous text
    path_entry.insert(0, folder_selected)        # put selected path in input box


# ---------------------------
# Main Window Setup
# ---------------------------
root = tk.Tk()
root.title("File Organizer")        # window title
root.geometry("500x250")            # window size
root.config(bg="#1e1e1e")           # dark background color

# Title label at the top
title = tk.Label(root, text="📂 File Organizer", font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="#ff0051")
title.pack(pady=15)

# Frame to hold the input box and Browse button side by side
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

# Input box where the selected folder path will appear
path_entry = tk.Entry(frame, width=40, font=("Arial", 12))
path_entry.pack(side=tk.LEFT, padx=5)

# Button to browse for a folder
browse_btn = tk.Button(frame, text="Browse", command=browse_folder,
                       bg="#007acc", fg="white", font=("Arial", 10, "bold"))
browse_btn.pack(side=tk.LEFT, padx=5)

# Main button to organize files
organize_btn = tk.Button(root, text="Organize Files", command=organize_files,
                         bg="#00ff88", fg="black", font=("Arial", 12, "bold"), width=20)
organize_btn.pack(pady=20)

# Exit button at the bottom
exit_btn = tk.Button(root, text="Exit", command=root.quit,
                     bg="#ff5555", fg="white", font=("Arial", 10, "bold"), width=10)
exit_btn.pack()

# Keep the window running
root.mainloop()
