from tkinter import *
from tkinter import messagebox
import random
import string


# Generates a password and repeatedly generates if the user declines the password
def generate_password():
    characters = string.ascii_letters + string.digits + '!@#$?!@#$?!@#$?'
    password = ''.join(random.choice(characters) for _ in range(10))
    messagebox.showinfo('Generated Password', f'Generated Password: {password}')
    if messagebox.askyesno('Copy to Clipboard', 'Do you want to copy the password to clipboard?'):
        copy_to_clipboard(password)
    else:
        generate_password()


# Copy generated password to clipboard
def copy_to_clipboard(password):
    main_window.clipboard_clear()
    main_window.clipboard_append(password)
    messagebox.showinfo('Password Generated', 'Password has been copied to clipboard.')


# Confirm password and save to data file
def add_password():
    website = website_entry.get()
    em_un = em_un_entry.get()
    password = pw_entry.get()
    confirm_save = None

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please enter a value for the website and password fields. ")
    # prompt a confirmation from user for save
    else:
        confirm_save = messagebox.askokcancel(title=website, message=f"You've entered:\nUsername: {em_un}\nPassword: {password}\nIs this correct?")

    if confirm_save:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website},{em_un},{password}\n")
            website_entry.delete(0, END)
            pw_entry.delete(0, END)
    else:
        website_entry.delete(0, END)
        em_un_entry.delete(0, END)
        pw_entry.delete(0, END)


# Setup of the main UI
main_window = Tk()
main_window.title("Password Manager")
main_window.config(padx=25, pady=25)

bg = Canvas(height=200, width=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
bg.create_image(100, 100, image=logo)
bg.grid(column=0, row=0, columnspan=3)

top_left_lbl = Label(text="Website: ")
top_left_lbl.grid(column=0, row=1)

mid_left_lbl = Label(text="Email/Username: ")
mid_left_lbl.grid(column=0, row=2)

bot_left_lbl = Label(text="Password: ")
bot_left_lbl.grid(column=0, row=3)

website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

em_un_entry = Entry(width=39)
em_un_entry.grid(column=1, row=2, columnspan=2)
em_un_entry.insert(END, "example@example.com")

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)

add_button = Button(text="Add Password", width=37, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

generate_pw = Button(text="Generate Password", command=generate_password)
generate_pw.grid(column=2, row=3)

main_window.mainloop()
