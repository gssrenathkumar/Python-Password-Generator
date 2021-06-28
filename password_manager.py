# Generate a Password & Copy it to the Clipboard
import tkinter
from tkinter import messagebox
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    #Adding into the list
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    mailid=mail_input.get()
    password=password_input.get()
    
    if len(website)==0 or len(mailid)==0 or len(password)==0:
        messagebox.showinfo("Oops","Don't Leave the Spaces Empty")
    
    else:
        is_save=messagebox.askokcancel(title=website,message="Given details are\n" f"Email/Username:{mailid}\n" f"Password:{password}\n" "Is it correct?")
        if is_save:
            with open("D:\\Learning\\Project Innovative Ideas\\Software Projects\\Completed\\Password generator GUI\\file3.txt","a") as file:
                file.write(f"\n{website_input.get()} | {mail_input.get()} | {password_input.get()} ")
                website_input.delete(0,"end")
                password_input.delete(0,"end")

# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")
canvas=tkinter.Canvas(width=200,height=200,bg="white",highlightthickness=0)
lock_image=tkinter.PhotoImage(file="D:\Learning\Project Innovative Ideas\Software Projects\Completed\Password generator GUI\logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)

website=tkinter.Label(text="Website:  ",fg="black",font=("Arial",10,"bold"),bg="white")
website.grid(column=0,row=1)

website_input=tkinter.Entry(width=35)
website_input.grid(column=1,row=1,columnspan=2)
#Adding the corsor to the input box on startup
website_input.focus()


mail=tkinter.Label(text="Email/Username:  ",fg="black",font=("Arial",10,"bold"),bg="white")
mail.grid(column=0,row=2)

mail_input=tkinter.Entry(width=35)
mail_input.grid(column=1,row=2,columnspan=2)
mail_input.insert(0,"srenath@gmail.com")


password=tkinter.Label(text="Password:  ",fg="black",font=("Arial",10,"bold"),bg="white")
password.grid(column=0,row=3)

password_input=tkinter.Entry(width=21)
password_input.grid(column=1,row=3,columnspan=1)

generate_button=tkinter.Button(text="Generate Passowrd",bg="white",highlightthickness=0,command=generate_password)
generate_button.grid(column=2,row=3,columnspan=1)

add_button=tkinter.Button(text="Add",bg="white",width=35,command=save)
add_button.grid(column=1,row=4,columnspan=13)


window.mainloop()