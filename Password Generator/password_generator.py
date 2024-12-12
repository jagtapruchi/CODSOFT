import random
import string
import tkinter as tk

#function to dynamically generate passwords
def password_generator():
    length = scale.get()
    chars = ""
    if var_digits.get():
        chars+= string.digits
    if var_lowercaseletters.get():
        chars+=string.ascii_lowercase
    if var_uppercaseletters.get():
        chars+=string.ascii_uppercase
    if var_symbols.get():
        chars+=string.punctuation
    
    #join the selected characters    
    password= "".join(random.choices(chars,k=length))    
    password_label.config(text=f"Generated Password: {password}",fg="white",font=("arial",20,"bold","underline"))


root = tk.Tk()
root.geometry("500x500")
main_frame = tk.Frame(root,bg="darkblue")
main_frame.pack(fill="both",expand=True)

#heading label
heading = tk.Label(main_frame,fg="white",bg="darkblue",font=("arial",35,"bold"),text="Generate passwords with our random password generator.",anchor="w",justify="left")
heading.pack(padx=10,pady=10)

#frame (includes scale and length label)
content_frame = tk.Frame(main_frame,bg="darkblue")
content_frame.pack(padx=20,pady=14)

def on_slide(value):
    label.config(text=f"Length({value})")
    
label = tk.Label(content_frame,text=("Length(1)"),fg="white",bg="darkblue",font=("arial",20))
label.pack(padx=20,pady=13)

scale = tk.Scale(content_frame,from_=1, to=127,orient="horizontal",bg="white",length=700,troughcolor="lightgray",highlightthickness=5,showvalue=1,command=on_slide)
scale.set(1)
scale.pack(padx=10,pady=16)

var_digits=tk.BooleanVar()
var_lowercaseletters=tk.BooleanVar()
var_uppercaseletters=tk.BooleanVar()
var_symbols=tk.BooleanVar()

#frame for checkbuttons
checkbox_frame=tk.Frame(main_frame,bg="darkblue")
checkbox_frame.pack(pady=5)

btn1 = tk.Checkbutton(checkbox_frame,text="Digits",fg="White",bg="darkblue",font=("arial",15,"bold"),variable=var_digits,onvalue=True,offvalue=False)
btn1.pack(side="left",padx=10, pady=3)

btn2 = tk.Checkbutton(checkbox_frame,text="Lowercase Letters",fg="White",bg="darkblue",font=("arial",15,"bold"),variable=var_lowercaseletters,onvalue=True,offvalue=False)
btn2.pack(side="left",padx=15, pady=3)

btn3 = tk.Checkbutton(checkbox_frame,text="Uppercase Letters",fg="White",bg="darkblue",font=("arial",15,"bold"),variable=var_uppercaseletters,onvalue=True,offvalue=False)
btn3.pack(side="left",padx=15, pady=3)

btn4 = tk.Checkbutton(checkbox_frame,text="Symbols",fg="White",bg="darkblue",font=("arial",15,"bold"),variable=var_symbols,onvalue=True,offvalue=False)
btn4.pack(side="left",padx=10, pady=3)

#pre selected buttons:
var_digits=tk.IntVar(value=1)
var_symbols=tk.IntVar(value=1)

#frame for label and strength indicator
f1 = tk.Frame(main_frame,bg="darkblue")
f1.pack(pady=100)

password_label=tk.Label(f1,width=200,height=2,font=("arial",25,"bold","underline"),fg="white",bg="darkblue")
password_label.pack(padx=10,pady=10)

#strength indicator
def strength_indicator():
    password = password_label.cget("text").replace("Generated Password: ","")
    has_digits = any(char.isdigit() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_symbols = any(char in string.punctuation for char in password)
    
    if len(password)>=8 and has_digits and has_lowercase and has_uppercase and has_symbols:
        btn5.config(text="Strong Password",bg="green",fg="white")
    elif len(password)>=6 and sum([has_digits,has_symbols,has_lowercase,has_uppercase])>=3:
        btn5.config(text="Moderate Password",bg="orange",fg="white")
    else:
        btn5.config(text="Weak Password",bg="red",fg="white")
    
btn5 = tk.Button(f1,text="Check Strength",bg="whitesmoke",fg="black",command=strength_indicator,font=("arial",15,"bold"))
btn5.pack(padx=10,pady=20)

#frame for final buttons:
btn_frame = tk.Frame(main_frame,bg="darkblue")
btn_frame.pack(pady=2)

password_btn = tk.Button(btn_frame,text="Generate Password",command=password_generator,font=("arial",15,"bold"),bg="lightblue",fg="black")
password_btn.pack(side="left",padx=30)

def copy_btn():
    password=password_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    
button1 = tk.Button(btn_frame,text="COPY",fg="black",activebackground="darkgray",bg="white",width=5,height=2,font=("arial",10,"bold"),command=copy_btn)
button1.pack(side="left",padx=20)



root.mainloop()