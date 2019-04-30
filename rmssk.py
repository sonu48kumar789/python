import tkinter
from tkinter import *
root = tkinter.Tk()

root.config(bg="blue")

root.minsize(1300, 700)
root.maxsize(1300, 700)
root.title(" Sonu Restaurats Management System")
f1 = Label(root, text=".......Sonu Thakre Restaurant Magement System.......", font="arial 28 bold italic", fg="red", bg="blue", padx=0)
f1.grid(row=0, column=0, columnspan=3)
f2 = LabelFrame(root, text=" Msale Dar Food ", width=800, height=500, bg="blue")
f2.grid(row=1, column=1)
f3 = LabelFrame(root, text="Please Click Fist", width=200, height=500, bg="blue")
f3.grid(row=1, column=2)
f4 = Frame(root, width=200, height=600, padx=1, bg="blue", pady=0)
f4.grid(row=1, column=3, columnspan=1)

def button(t, r, c, bg="#740006", master=f2, fg="white"):
    Button(master, text=t, bg=bg, command=lambda: total(t), fg=fg, font="arial 16 bold", width=15, height=4, bd=8).grid(row=r, column=c, padx=12, pady=12)

def actionbtn(text, bg, command, r):
    Button(f3, text=text, bg=bg, font="arial 15 bold", fg="white", command=command, width=14, height=2, bd=8).grid(row=r, column=0, pady=21, padx=25)

set = ""
string = ""

def total(food):
    global set
    global string
    if "Samosa\nRs8"==food:
        price = 8
    elif "Chawmin\nRs30"==food:
        price = 30
    elif "Panir\nRs100"==food:
        price = 10
    elif "Burger\nRs30"==food:
        price = 30
    elif "Egg Roll\nRs30"==food:
        price = 30
    elif "Idli\nRs30"==food:
        price = 30
    elif "Dosa\nRs50"==food:
        price = 50
    elif "Kachori\nRs7"==food:
        price = 7
    elif "Fish\nRs100"==food:
        price =100
    elif "Chicken\nRs90"==food:
        price =90
    elif "Matan\nRs150"==food:
        price =150
    elif "Chhat\nRs15"==food:
        price =15
    else:
        price = 20
    set += str(price)+"+"
    string = food+" = "+str(price)+"/-\n"
    t.insert(END,string)

def final():
    global set
    global string
    set += "0"
    data = eval(set)
    string = "\nTotal Bill = "+str(data)+"/-"
    t.insert(END,string)

def clear():
    global set
    global string
    string = ""
    set = ""
    t.delete(0,END)

def view():
    pass

def setting():
    pass

button("Samosa\nRs8", 0, 0)
button("Chawmin\nRs30", 0, 1)
button("Burger\nRs30", 0, 2)
button("Egg Roll\nRs30", 1, 0)
button("Idli\nRs30", 1, 1)
button("Dosa\nRs50", 1, 2)
button("Kachori\nRs7", 2, 0)
button("Panir\nRs100", 2, 1)
button("Chhat\nRs15", 2, 2)
button("Fish\nRs100", 3, 0)
button("Chicken\nRs90", 3, 1)
button("Matan\nRs150", 3, 2)

actionbtn("Total", "#284635", final, 0)
actionbtn("Clear", "lime", clear, 1)
actionbtn("View", "#8E24AA", view, 2)
actionbtn("Quit", "red", quit, 3)
actionbtn("Setting", "#963572", setting, 4)
button("Panir\nRs100", 2, 1)
button("Chhat\nRs15", 2, 2)

actionbtn("Total", "#673AB7", final, 0)
actionbtn("Clear", "#607D8B", clear, 1)
actionbtn("View", "#4CAF50", view, 2)

t = Listbox(f4, width=50, height=22, font="arial 14 bold", bg="blue")
t.pack()

root.mainloop()