import tkinter as tk

def change_theme():
    if theme_var.get() == "Dark":
        root.config(background="black")

    if theme_var.get() == "Light":
        root.configure(background="White")


def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)


# Main window
root = tk.Tk()


# Formatting main window
root.title("Menus")
root.geometry("600x350")


# --- MENUBAR --- #


# Creating a menubar
menubar = tk.Menu(root)
root.config(menu=menubar)


# Creating top-level menus for the menubar
file_menu = tk.Menu(menubar, tearoff=0)
edit_menu = tk.Menu(menubar, tearoff=0)
settings_menu = tk.Menu(menubar, tearoff=0)

# Adding top-level menus to menubar
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="Settings", menu=settings_menu)


# adding items to file menu
file_menu.add_command(label="New", command=lambda: print("Created new file"))
file_menu.add_command(label="Open", command=lambda: print("Opend existing file"))
file_menu.add_command(label="Save", command=lambda: print("Saved current file"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# adding items to edit menu
edit_menu.add_command(label="Undo", command=lambda: print("Undone successfully"))
edit_menu.add_command(label="Redo", command=lambda: print("Redone successfully"))
edit_menu.add_command(label="Cut", command=lambda: print("Text cut"))
edit_menu.add_command(label="Copy", command=lambda: print("Text copied"))
edit_menu.add_command(label="Paste", command=lambda: print("Text pasted "))


# adding items to settings menu
theme_var = tk.StringVar()
theme_var.set("Light")
settings_menu.add_radiobutton(label="Light", variable=theme_var, value="Light", command=change_theme)
settings_menu.add_radiobutton(label="Dark", variable=theme_var, value="Dark", command=change_theme)


# --- TOOLBAR --- #

toolbar = tk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

btn_1 = tk.Button(toolbar, text="new")
btn_2 = tk.Button(toolbar, text="open")

btn_1.pack(side=tk.LEFT, padx=2, pady=2)
btn_2.pack(side=tk.LEFT, padx=2, pady=2)


#=== CONTEXT MENU ===#

context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="cut")
context_menu.add_command(label="copy")
context_menu.add_command(label="paste")

root.bind("<Button-3>", show_context_menu)

root.mainloop()