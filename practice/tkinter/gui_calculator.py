import tkinter as tk
from tkinter import ttk

# Define dark theme colors
BG_COLOR = '#23272e'           # Main background
FRAME_COLOR = '#2c313c'        # Frame background
ENTRY_BG = '#393e46'           # Entry background
ENTRY_FG = '#f8f8f2'           # Entry text
FOCUS_BG = '#44475a'           # Entry focus background
BTN_BG = '#44475a'             # Button background
BTN_FG = '#f8f8f2'             # Button text
BTN_ACTIVE_BG = '#6272a4'      # Button active background
LBOX_BG = '#282a36'            # Listbox background
LBOX_FG = '#f8f8f2'            # Listbox text
RADIO_BG = '#2c313c'           # Radiobutton background
RADIO_FG = '#f8f8f2'           # Radiobutton text


def focus_in(e):
    e.widget.config(bg=FOCUS_BG)

def focus_out(e):
    e.widget.config(bg=ENTRY_BG)

def show_context_menu():
    pass

def clear_entries():
    en_num1.delete(0, tk.END)
    en_num2.delete(0, tk.END)

def calculate(e=None):
    try:
        num1 = float(en_num1.get())
        num2 = float(en_num2.get())
    except ValueError:
        lbox_res.insert(tk.END, "Invalid input!")
        clear_entries()
        return
    if en_num1.get() and en_num2.get():
        if operation.get() == 'add':
            lbox_res.insert(tk.END, f"{num1} + {num2} = {(num1+num2):.2f}")
        if operation.get() == 'sub':
            lbox_res.insert(tk.END, f"{num1} - {num2} = {(num1-num2):.2f}")
        if operation.get() == 'mul':
            lbox_res.insert(tk.END, f"{num1} * {num2} = {(num1*num2):.2f}")
        if operation.get() == 'div':
            if num2 != 0:
                lbox_res.insert(tk.END, f"{num1} / {num2} = {(num1/num2):.2f}")
            else:
                lbox_res.insert(tk.END, "Division by zero not possible!")
        clear_entries()


root = tk.Tk()
style = ttk.Style()

# Set dark theme for ttk widgets
style.theme_use('clam')
style.configure('.', background=BG_COLOR, foreground=BTN_FG, font=('Segoe UI', 11))
style.configure('TButton', background=BTN_BG, foreground=BTN_FG, borderwidth=0, focusthickness=3, focuscolor=FOCUS_BG)
style.map('TButton', background=[('active', BTN_ACTIVE_BG)])
style.configure('TLabel', background=FRAME_COLOR, foreground=BTN_FG)

root.title("Calculator")
root.geometry("400x450")
root.configure(bg=BG_COLOR)

main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill='both', expand=True)

frame1 = tk.Frame(main_frame, bg=FRAME_COLOR)
frame1.pack(pady=(20, 0), padx=20, fill='x')

# Creating labels
lbl_num1 = ttk.Label(frame1, text="Number 1: ")
lbl_num1.grid(row=0, column=0, padx=(0,10), pady=8, sticky='w')

lbl_num2 = ttk.Label(frame1, text="Number 2: ")
lbl_num2.grid(row=1, column=0, padx=(0,10), pady=8, sticky='w')


# Entry widgets with dark theme
en_num1 = tk.Entry(frame1, background=ENTRY_BG, foreground=ENTRY_FG, insertbackground=ENTRY_FG, relief='flat', highlightthickness=1, highlightbackground=FOCUS_BG)
en_num1.grid(row=0, column=1, pady=8, ipady=3)
en_num1.bind("<FocusIn>", focus_in)
en_num1.bind("<FocusOut>", focus_out)

en_num2 = tk.Entry(frame1, background=ENTRY_BG, foreground=ENTRY_FG, insertbackground=ENTRY_FG, relief='flat', highlightthickness=1, highlightbackground=FOCUS_BG)
en_num2.grid(row=1, column=1, pady=8, ipady=3)
en_num2.bind("<FocusIn>", focus_in)
en_num2.bind("<FocusOut>", focus_out)


#-----------------------END OF FRAME 1-----------------------#


# Creating new frame for buttons and output
frame2 = tk.Frame(main_frame, bg=FRAME_COLOR)
frame2.pack(pady=(20, 0), padx=20, fill='x')


# Creating radio buttons to display operations
operation = tk.StringVar()
operation.set("add")

rbtn_add = tk.Radiobutton(frame2, text="Addition", variable=operation, value="add", width=15, anchor='w', bg=RADIO_BG, fg=RADIO_FG, selectcolor=BTN_ACTIVE_BG, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_FG, font=('Segoe UI', 10))
rbtn_add.grid(row=0, column=0, pady=5, padx=5)

rbtn_sub = tk.Radiobutton(frame2, text="Subtraction", variable=operation, value="sub", width=15, anchor='w', bg=RADIO_BG, fg=RADIO_FG, selectcolor=BTN_ACTIVE_BG, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_FG, font=('Segoe UI', 10))
rbtn_sub.grid(row=0, column=1, pady=5, padx=5)

rbtn_mul = tk.Radiobutton(frame2, text="Multiplication", variable=operation, value="mul", width=15, anchor='w', bg=RADIO_BG, fg=RADIO_FG, selectcolor=BTN_ACTIVE_BG, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_FG, font=('Segoe UI', 10))
rbtn_mul.grid(row=1, column=0, pady=5, padx=5)

rbtn_div = tk.Radiobutton(frame2, text="Division", variable=operation, value="div", width=15, anchor='w', bg=RADIO_BG, fg=RADIO_FG, selectcolor=BTN_ACTIVE_BG, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_FG, font=('Segoe UI', 10))
rbtn_div.grid(row=1, column=1, pady=5, padx=5)


#-----------------------END OF FRAME 2-----------------------#


# creating the 3rd frame for submit button and answer
frame3 = tk.Frame(main_frame, bg=FRAME_COLOR)
frame3.pack(pady=(20, 0), padx=20, fill='x')


# Creating the calculate button
btn_calc = ttk.Button(frame3, text='Calculate', command=calculate, width=10)
btn_calc.grid(row=0, column=0, padx=(0, 10), pady=10)
btn_calc.bind("<Return>", calculate)
btn_calc.bind("<FocusIn>", focus_in)
btn_calc.bind("<FocusOut>", focus_out)

lbox_res = tk.Listbox(frame3, background=LBOX_BG, foreground=LBOX_FG, selectbackground=BTN_ACTIVE_BG, selectforeground=BTN_FG, relief='flat', highlightthickness=1, highlightbackground=FOCUS_BG, font=('Consolas', 11))
lbox_res.grid(row=0, column=1, padx=(10, 0), pady=10, ipadx=10, ipady=5)

root.bind("<Button-3>", show_context_menu)

# The main loop
root.mainloop()