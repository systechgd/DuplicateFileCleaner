import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import defaultdict

def hash_file(file_path):
    """Compute the MD5 hash of the file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicates(root_folder):
    """Find duplicate files in the given folder."""
    hashes = defaultdict(list)
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hash_file(file_path)
            hashes[file_hash].append(file_path)
    return {key: value for key, value in hashes.items() if len(value) > 1}

def print_duplicates(duplicates):
    """Display duplicates in the listbox with color coding."""
    listbox.delete(0, tk.END)
    if duplicates:
        listbox.insert(tk.END, "Duplicate Files Found:")
        for file_list in duplicates.values():
            # Display the original file in green
            listbox.insert(tk.END, file_list[0])
            listbox.itemconfig(tk.END, {'fg': 'green'})
            # Display the duplicates in red
            for file_path in file_list[1:]:
                listbox.insert(tk.END, file_path)
                listbox.itemconfig(tk.END, {'fg': 'red'})
    else:
        listbox.insert(tk.END, "No duplicate files found.")

def delete_files(duplicates):
    """Delete all duplicate files, keeping the first occurrence."""
    for file_list in duplicates.values():
        for file_path in file_list[1:]:  # Keep the first file, delete the rest
            try:
                os.remove(file_path)
                listbox.insert(tk.END, f"Deleted: {file_path}")
                listbox.itemconfig(tk.END, {'fg': 'blue'})  # Show deleted files in blue
            except Exception as e:
                listbox.insert(tk.END, f"Error deleting {file_path}: {e}")
                listbox.itemconfig(tk.END, {'fg': 'orange'})  # Show errors in orange

def clear_listbox():
    """Clear the listbox to allow new searches."""
    listbox.delete(0, tk.END)

def select_folder():
    root_folder = filedialog.askdirectory()
    if root_folder:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, root_folder)
        duplicates = find_duplicates(root_folder)
        print_duplicates(duplicates)

def delete_action():
    if messagebox.askyesno("Delete Duplicates", "Do you want to delete all duplicates?"):
        root_folder = entry_path.get()
        if os.path.isdir(root_folder):
            duplicates = find_duplicates(root_folder)
            delete_files(duplicates)
            messagebox.showinfo("Info", "Duplicate files deleted.")
        else:
            messagebox.showerror("Error", "The provided path is not a valid directory.")

# GUI setup
app = tk.Tk()
app.title("File Cleaner")
app.geometry("800x680")
app.config(bg="#d4edda")  # Light green background

# Frame for folder selection
frame = tk.Frame(app, bg="#d4edda")
frame.pack(padx=20, pady=20)

lbl_path = tk.Label(frame, text="Folder Path:", bg="#d4edda", font=("Helvetica", 12))
lbl_path.grid(row=0, column=0, sticky="e")

entry_path = tk.Entry(frame, width=50, font=("Helvetica", 12))
entry_path.grid(row=0, column=1, padx=5)

btn_browse = tk.Button(frame, text="Browse", command=select_folder, bg="#28a745", fg="white", font=("Helvetica", 12))
btn_browse.grid(row=0, column=2)

# Listbox for displaying results
listbox = tk.Listbox(app, width=100, height=20, font=("Helvetica", 12))
listbox.pack(padx=20, pady=10)

# Buttons for actions
btn_delete = tk.Button(app, text="Delete Duplicates", command=delete_action, width=20, bg="#dc3545", fg="white", font=("Helvetica", 12))
btn_delete.pack(pady=5)

btn_clear = tk.Button(app, text="Clear History", command=clear_listbox, width=20, bg="#17a2b8", fg="white", font=("Helvetica", 12))
btn_clear.pack(pady=5)

# Add a heading and tagline
heading = tk.Label(app, text="File Cleaner", font=("Helvetica", 24, "bold"), bg="#d4edda")
heading.pack(pady=10)

tagline = tk.Label(app, text="Find and Remove Duplicate Files Effortlessly", font=("Helvetica", 14), bg="#d4edda")
tagline.pack(pady=5)

# Set a custom icon (change the path to your .ico file)
app.iconbitmap("filecleaner.ico")

app.mainloop()
