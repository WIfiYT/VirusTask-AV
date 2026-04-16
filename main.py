import tkinter as tk
from tkinter import messagebox, Menu

def scan():
    messagebox.showinfo("Scan", "Scanning for viruses...")

def open_settings():
    messagebox.showinfo("Settings", "Settings menu opened.")

# Initialize main window
root = tk.Tk()
root.title("Antivirus Application")

# Create menu
menu = Menu(root)
root.config(menu=menu)

# Create 'File' menu
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Settings", command=open_settings)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create scan button
scan_button = tk.Button(root, text="Scan", command=scan)
scan_button.pack(pady=20)

# Run the application
root.mainloop()