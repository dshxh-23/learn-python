import tkinter as tk

root = tk.Tk()

root.title("User info form")
root.geometry("600x350")


# Functions
def on_submit():
    print(f"Name: {user_fname.get()} {user_lname.get()}")
    print(f"Email: {user_email.get()}")
    en_fname.delete(0, tk.END)
    en_lname.delete(0, tk.END)
    en_email.delete(0, tk.END)


def update_count(*args):
    email_chr_count.set(len(user_email.get()))
    


# Frames
main_frame = tk.Frame(root)
main_frame.pack()

left_frame = tk.Frame(main_frame)
left_frame.grid(row=0, column=0)

right_frame = tk.Frame(main_frame)
right_frame.grid(row=0, column=1)

bottom_frame = tk.Frame(main_frame)
bottom_frame.grid(row=1, column=0, columnspan=2)


# Labels
lbl_fname = tk.Label(left_frame, text="First Name: ")
lbl_fname.grid(row=0, column=0, sticky='w', padx=(0, 10))

lbl_lname = tk.Label(left_frame, text="Last Name: ")
lbl_lname.grid(row=1, column=0, sticky='w')

lbl_email = tk.Label(left_frame, text="Email ID: ")
lbl_email.grid(row=2, column=0, sticky='w')


# Entries
user_fname = tk.StringVar()
en_fname = tk.Entry(right_frame, width=30, textvariable=user_fname)
en_fname.grid(row=0, column=0, sticky='w')

user_lname = tk.StringVar()
en_lname = tk.Entry(right_frame, width=30, textvariable=user_lname)
en_lname.grid(row=1, column=0, sticky='w')

user_email = tk.StringVar()
en_email = tk.Entry(right_frame, width=30, textvariable=user_email)
en_email.grid(row=2, column=0, sticky='w')


# email character count
email_chr_count = tk.IntVar()
lbl_chr_count = tk.Label(bottom_frame, textvariable=email_chr_count)
lbl_chr_count.pack(pady=(10, 10))

user_email.trace_add("write", update_count)

# Submit button
btn_submit = tk.Button(bottom_frame, text="Submit", command=on_submit)
btn_submit.pack()


root.mainloop()