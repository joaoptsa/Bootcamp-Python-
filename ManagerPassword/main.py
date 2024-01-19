from tkinter import *
from tkinter import messagebox
import random
import json
from cryptography.fernet import Fernet


password = ""
SECRET_KEY='OtOX-Mi4ao7__ci8KB1a3eY6Ur-eeGEcCZNYPOdgmiY='
cipher_suite = Fernet(SECRET_KEY)

def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0''1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '+', '*']

    nr_letters=random.randint(7,10)
    nr_numbers=random.randint(4,10)
    nr_symbols=random.randint(2,10)


    nrLetters =[random.choice(letters) for _ in range(nr_letters)]
    nrSymbols =[random.choice(numbers) for _ in range(nr_numbers)]
    nrNumbers =[random.choice(symbols) for _ in range(nr_symbols)]

    passwordList = nrLetters + nrSymbols + nrNumbers

    random.shuffle(passwordList)
    password_entry.delete(0, END)
    global password
    password=""
    password ="".join(passwordList)
    password_entry.insert(0,password)

def encrypt_data(data):
    return cipher_suite.encrypt(json.dumps(data).encode()).decode()

def decrypt_data(encrypted_data):
    return json.loads(cipher_suite.decrypt(encrypted_data.encode()).decode())

def save_file():
    
    
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    
    data_user = {
    "email": email,
    "password": password,
    }
    
    data_website={}
    
    if len(website)==0 or len(password)==0 or len(email)==0 :
        messagebox.showinfo(title="Ooops", message="you need to fill in the fields")
    else:
        data_website[website] = encrypt_data(data_user)
        try:
            with open("data.json","r") as data_file:
               data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(data_website, data_file, indent=4)
        else:
            data.update(data_website)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
              
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)



def search_password():
    
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="Not Found")
    else:
        for website, encrypted_data in data.items():
            tex = decrypt_data(encrypted_data)
            email = tex["email"]
            password = tex["password"]
            messagebox.showinfo(title=f"All Websites", message=f"{website}\nEmail: {email}\nPassword: {password}\n")
            


window=Tk()
window.title("Generator Passaword")
window.config(padx=50,pady=50)

canvas=Canvas(height=300,width=300)
logo=PhotoImage(file="cand.png")
canvas.create_image(150,150,image=logo)
canvas.grid(row=0,column=0)

website=Label(text="Website")
website.grid(row=1,column=0)
email=Label(text="Email")
email.grid(row=2,column=0)
password=Label(text="Password")
password.grid(row=3,column=0)

generate_password=Button(text="Generate Password",command=generate_password)
generate_password.grid(row=0,column=0)

search_button=Button(text="Search",command=search_password)
search_button.grid(row=0,column=1)

add_button=Button(text="Add",width=32,command=save_file)
add_button.grid(row=4,column=1)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)

password_entry=Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)




window.mainloop()





