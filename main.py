from tkinter import *
from tkinter import messagebox
import random

new_line = '\n'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # Python List Comprehension to choose random letters, symbols, and numbers
    letter_list = [random.choice(letters) for char in range(nr_letters)]
    symbol_list = [random.choice(symbols) for char2 in range(nr_symbols)]
    number_list = [random.choice(numbers) for char3 in range(nr_numbers)]

    # for every item in the list for the 3 lists, append the character to the password list
    for letter in letter_list:
        password_list.append(letter)
    for symbol in symbol_list:
        password_list.append(symbol)
    for number in number_list:
        password_list.append(number)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    password_entry.insert(0, f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = website_var.get()
    password = passw_var.get()
    email = email_var.get()

    if (not website) or (not password) or (not email):
        is_empty = messagebox.showerror(title="Error" , message="Please don't leave any fields empty!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")


    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
            website_entry.delete(0, END)
            emailUsername_entry.delete(0, END)
            password_entry.delete(0, END)

        pw_txtfile = open("data.txt", "r")
        print(pw_txtfile.read())


#tkinter insert and delete function to clear our the entry boxes after clicking add
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#save website, email, and pw into data.txt with | in between them, use append not write
website_var = StringVar()
passw_var = StringVar()
email_var = StringVar()

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(window, textvariable=website_var, width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

emailUsername_label = Label(text="Email/Username:")
emailUsername_label.grid(row=2, column=0)
emailUsername_entry = Entry(window, textvariable=email_var, width=35)
emailUsername_entry.grid(row=2, column=1, columnspan=2)
#emailUsername_entry.insert(0, "example@gmail.com") -- wouldnt work as textvariable for some reason

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(window, textvariable=passw_var, width=18)
password_entry.grid(row=3, column=1)

generatePassword_button = Button(text="Generate Password", command=generatePassword)
generatePassword_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=add)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()