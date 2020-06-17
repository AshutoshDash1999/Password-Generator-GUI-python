import string
import random
import tkinter as tk
from tkinter import messagebox

def randomStringGenerator():
    stringLength = int(myStringlength.get())
    randomString = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(stringLength):
        password += random.choice(randomString)

    messagebox.showinfo("Password", password)

main = tk.Tk()
main.title("Password Generator")
main.geometry("300x250")
label = tk.Label(main, text="Name of social site: ", font=("Ubuntu Bold", 12)).place(x=10, y=20)

mySite = tk.StringVar()
entry = tk.Entry(width=30, textvariable = mySite).place(x=30, y=50)
# TODO: save the name of site and the password generated in a text file in dictionary format

string_label = tk.Label(main, text="Choose password length: ", font=("Ubuntu Bold", 12)).place(x=10, y=90)

myStringlength = tk.StringVar()
entry = tk.Entry(width=5, textvariable = myStringlength).place(x=230, y=90)

passwordButton = tk.Button(main, text="Generate Password", bg="green", fg = "white", font=("bold", 11), command = randomStringGenerator).place(x=60, y=150)


main.mainloop()