from tkinter import *
from tkinter import messagebox
import json
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


# Searches file for existing password with website name
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as pw_list:
            db = json.load(pw_list)
            if website in db:
                lookup_email = db[website]["email"]
                lookup_pw = db[website]["password"]
                messagebox.showinfo(title=website, message=f"Email/Username: {lookup_email}\nPassword:{lookup_pw}")

    except FileNotFoundError:
        messagebox.showinfo(message="There are currently no passwords stored. Please input one before searching. ")
    else:
        messagebox.showinfo(message="No information found for search parameters.")
    finally:
        website_entry.delete(0, END)


# Confirm password and save to data file
def add_password():
    website = website_entry.get()
    em_un = em_un_entry.get()
    password = pw_entry.get()
    confirm_save = None
    new_pw = {
        website: {
            "email": em_un,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please enter a value for the website and password fields. ")
    # prompt a confirmation from user for save
    else:
        confirm_save = messagebox.askokcancel(title=website, message=f"You've entered:\nUsername: {em_un}\nPassword: {password}\nIs this correct?")

    if confirm_save:
        try:
            with open("data.json", "r") as pw_list:
                data = json.load(pw_list)
                data.update(new_pw)
        except FileNotFoundError:
            with open("data.json", "w") as pw_list:
                json.dump(new_pw, pw_list, indent=4)
        else:
            data.update(new_pw)
            with open("data.json", "w") as pw_list:
                json.dump(new_pw, pw_list, indent=4)
        finally:
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

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

pw_search = Button(text="Search", width=13, command=find_password)
pw_search.grid(column=2, row=1)

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
