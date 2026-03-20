import tkinter as tk
from tkinter import ttk

def change_theme(event=None):
    selected_theme = theme_var.get()
    style.theme_use(selected_theme)

root = tk.Tk()
root.title("TTK Theme Switcher")

style = ttk.Style()

# Print available themes
available_themes = style.theme_names()
print("Available themes:", available_themes)

# Dropdown to select themes
theme_var = tk.StringVar()
theme_menu = ttk.Combobox(root, textvariable=theme_var, values=available_themes, state="readonly")
theme_menu.pack(pady=10)
theme_menu.set(style.theme_use())       # set current theme as default
theme_menu.bind("<<ComboboxSelected>>", change_theme)

# Some ttk widgets to reflect the theme
ttk.Label(root, text="This is a Label").pack(pady=10)
ttk.Entry(root).pack(pady=10)
ttk.Button(root, text="Click Me").pack(pady=10)

root.mainloop()