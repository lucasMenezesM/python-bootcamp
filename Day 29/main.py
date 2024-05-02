from tkinter import *
from tkinter import messagebox
import pandas
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from functions import generate_password

def handle_generate_password():
    generated_password = generate_password()

    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
    messagebox.showinfo(title="New Password Generated!", message="The new password was copied.")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()

    new_entry = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password.strip()) == 0 or len(email.strip()) == 0 or len(website.strip()) == 0:
        messagebox.showerror(title="Filds blank", message="Dont leave any fields blank")
        return

    confirme = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\nContinue?")

    if not confirme:
        return 
    
    try:
        with open("Day 29\data.json", mode="r") as data_file:
            # Reading a json file
            data = json.load(data_file)

    except FileNotFoundError:
        with open("Day 29\data.json", mode="w") as data_file:
            # Creating a Json File
            json.dump(new_entry, data_file, indent=4)
            
    else:
        with open("Day 29\data.json", mode="w") as data_file:
            # Updating a Json File
            data.update(new_entry)
            json.dump(data, data_file, indent=4)

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().title()

    if len(website.strip()) == 0:
        return

    try:
        with open("Day 29\data.json") as data_file:
            data = json.load(data_file)
        
        website_found = data[website]

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="You don't have any save password")
    except KeyError:
        messagebox.showerror(title="Error", message=f"the website {website} was not found.")
    else:
        messagebox.showinfo(title="Website Found", message=f"{website}\nEmail: {website_found['email']} \nPassword: {website_found['password']}")


# ---------------------------- UI SETUP ------------------------------- #

# Window Cnfig
window = Tk()
window.config(padx=50, pady=20)
window.title("Password Manager")

# Canvas Config
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="Day 29/logo.png")
logo_image = canvas.create_image(125, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website", pady=10)
website_label.grid(column=0, row=1)

username_label = Label(text="Username:", pady=10)
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", pady=10)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky=EW)
website_entry.focus()

username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
username_entry.insert(0, "lucas@gmail.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky=EW)

# Buttons
generate_password_btn = Button(text="Generate Password", command=handle_generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky=EW)

search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1, sticky=EW)

window.mainloop()