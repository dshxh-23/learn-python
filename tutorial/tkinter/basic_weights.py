import tkinter as tk
import sys

# Test your tkinter setup with tk._test()

def add(event = None):
    text = entry.get()
    if text:
        list_box.insert(tk.END, text)
        entry.delete(0, tk.END)

# Creating the main window
root = tk.Tk()

# Setting window properties
root.title("My first app")
root.geometry("500x400")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# Creating and displaying frame
frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, sticky="nesw")
frame1.columnconfigure(0, weight=1)

# label to frame
entry = tk.Entry(frame1)
entry.grid(row=0, column=0)
entry.bind("<Return>", add)

# Adding button to frame
button = tk.Button(frame1, text="Add", command=add)
button.grid(row=0, column=1)

# Adding listbox to frame
list_box = tk.Listbox(frame1)
list_box.grid(row=1, column=0, columnspan=2, sticky="esw")

# Starting the event loop
root.mainloop()
