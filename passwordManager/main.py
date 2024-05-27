from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT = ("Arial", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    p_word.insert(0, password)


# ---------------------------- SEARCH  ------------------------------------- #


def find_password():
    website = str(web_name.get())
    if website != 00:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showwarning(title="Invalid Entry", message="No data file found.")

        else:
            if website in data:
                x = data.get(website)
                messagebox.showinfo(title=website, message=f"Username: {x['email']}\nPassword: {x['password']}")
            else:
                messagebox.showwarning(title="Invalid Entry", message=f"No details for {website} exist.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = str(web_name.get())
    email = str(email_name.get())
    password = str(p_word.get())
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Invalid Entry", message="Please ensure all the fields are filled.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read current data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update current data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Save updated data
                json.dump(data, data_file, indent=4)
        finally:
            reset_password_manager()


def reset_password_manager():
    web_name.delete(0, "end")
    email_name.delete(0, "end")
    email_name.insert(0, "lindacolenl@gmail.com")
    p_word.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

my_image = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=my_image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:", font=FONT)
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:", font=FONT)
label_email.grid(row=2, column=0)
label_password = Label(text="Password:", font=FONT)
label_password.grid(row=3, column=0)

web_name = Entry(width=22, font=FONT)
web_name.focus()
web_name.grid(row=1, column=1)

email_name = Entry(width=38, font=FONT)
email_name.grid(row=2, column=1, columnspan=2)
email_name.insert(0, "lindacolenl@gmail.com")

p_word = Entry(width=22, font=FONT)
p_word.grid(row=3, column=1)

search_button = Button(width=16, text="Search", font=FONT, command=find_password)
search_button.grid(row=1, column=2)

pass_button = Button(width=16, text="Generate Password", font=FONT, command=generate_password)
pass_button.grid(row=3, column=2)

add_button = Button(width=40, text="Add", font=FONT, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

mainloop()
