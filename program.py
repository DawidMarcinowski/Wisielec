#implementacja bibliotek
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
x=0
i=0
allleter=[]
entrylenght=0
#main window
root = tkinter.Tk()
root.geometry("1920x1000")

#disable resizable window 
root.resizable(width=False,height=False)

#loading screan 
Images=[]
Images.append(ImageTk.PhotoImage(Image.open("0.png")))
Images.append(ImageTk.PhotoImage(Image.open("1.png")))
Images.append(ImageTk.PhotoImage(Image.open("2.png")))
Images.append(ImageTk.PhotoImage(Image.open("3.png")))
Images.append(ImageTk.PhotoImage(Image.open("4.png")))
Images.append(ImageTk.PhotoImage(Image.open("5.png")))
Images.append(ImageTk.PhotoImage(Image.open("6.png")))
Images.append(ImageTk.PhotoImage(Image.open("7.png")))
Images.append(ImageTk.PhotoImage(Image.open("8.png")))
Images.append(ImageTk.PhotoImage(Image.open("9.png")))
Images.append(ImageTk.PhotoImage(Image.open("10.png")))
Images.append(ImageTk.PhotoImage(Image.open("11.png")))
Images.append(ImageTk.PhotoImage(Image.open("12.png")))

goodletter=[]
oldletter=[]
finaltab=[10]


#loading background
tkinter.Label(root).place(x=0, y=0)
label = Label(root, image=Images[x])
label.pack()
info = Label(root, text="This letter has already been entered, please enter another letter.",font=("Arial", 20))
#function limiting the maximum number of letters
def validate_input(new_letter):
    if len(new_letter) > 1:
        return False
    return True

# function to change background and load enter letter
def change_image():
    global x
    global len
    global letterwasword
    global passwordtab
    global finaltab
    global i
    global oldletter
    global goodletter
    letterword = letter.get()
    global entrylenght
    global allletter

    

    if letterword in allleter:
        info.place(x=400, y=200)
        #info.config(text="This letter has already been entered, please enter another letter.",bg="white")
    else:
        #info.config(text="                                                                                              ",bg="white")
        info.place_forget()
        allleter.append(letterword)
        if entrylenght==0:
            #enter good letter
            if letterword in passwordtab:
                i+=1
                goodletter.append(letterword)
                result_label = Label(root, text=" ",font=("Arial", 20))
                result_label.config(text=f"previously good letters: {goodletter}")
                result_label.place(x=0, y=600)

            #enter bad letter  
            else:
                oldletter.append(letterword)
                x+=1
                print (x)
                label.configure(image=Images[x])
                label.image = Images[x] 
                #wyświetlanie wartości rezystancji na ekranie 
                result_label = Label(root, text=" ",font=("Arial", 20))
                result_label.config(text=f"previously bad letters: {oldletter}")
                result_label.place(x=0, y=400)
    
            #loss game
            if x==12:
                messagebox.showinfo("","you loss :(")
                root.destroy()

            #win game
            if i==passwordlen:
                messagebox.showinfo("","you winn :)")
                root.destroy()
        

#tab with passwords
randomword=random.randint(0,4)
WORDS=[]
WORDS=['work', 'dog', 'cat', 'car', 'nokia']
Password=WORDS[randomword]
passwordtab=[]

for letter in Password:
    passwordtab.append(letter)
print(passwordtab)

passwordlen=len(passwordtab)
print("pawsswordlen")
print(passwordlen)
#hellow text
label1 = Label(root, text="Hi welcome to my game ",font=("Arial", 20))
label1.place(x=10, y=10)

#loadind letter
label1 = Label(root, text="enter a letter",font=("Arial", 20))
label1.place(x=0, y=150)

validate_input_cmd = root.register(validate_input)
letter = Entry(root, validate="key", validatecommand=(validate_input_cmd, "%P"),font=("Arial", 20),borderwidth=3)
letter.place(x=0, y=200)

# button
button = Button(root, text="check the letter",font=("Arial", 20), command=change_image)
button.place(x=0, y=300)

mainloop()