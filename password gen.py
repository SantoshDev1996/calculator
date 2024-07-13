from tkinter import * 
from tkinter.ttk import Combobox
from tkinter import messagebox
import string,random

root =Tk()
root.geometry ("560x481+500+100")
root.title("Santosh password Genertor")
root.config(bg="Yellowgreen")
root.resizable(False,False)

selector={}

def password_generate():
    try:
        length_password = soildbox.get()
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits =string.digits
        special_character = string.punctuation
        all_list =[]
        all_list.extend(list(small_letters))
        all_list.extend(list( capital_letters))
        all_list.extend(list( digits ))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_password]))
    except:
        messagebox.askretrycancel ("A Problem Has Been Occured","Please Try Again")


all_no = {"1" : "1","2" : "2","3" : "3","4" : "4","5" :"5" , "6" : "6" , "7 " : "7","8" : "8","9" : "9" ,"10":"10", "11":"11","12":"12","13":"13","14":"14","15":"15","16":"16","17":"17","18":"18","19":"19","20":"20","21":"21","22":"22","23":"23","24":"24","25":"25","26":"26","27":"27","28":"28","29":"29","30":"30"}

Title = Label(root, text="Santosh password Genertor",bg="Yellowgreen",fg="black",font=("futura",15,"bold"))
Title.pack(anchor="center",pady="20px")

length = Label(root,text="select the length of your password :-",bg="Yellowgreen",fg="brown",font=("ubunt",12))
length.place(x="20px",y="70px")


def on_enter():
    generate_btn['bg'] ="grey"
    generate_btn['fg'] ="white"

def on_leave():
    generate_btn['bg'] ="orange"
    generate_btn['fg'] ="black"

soildbox = IntVar()
selector = Combobox(root,textvariable = soildbox,state="read")
selector['values'] =[i for i in all_no.keys()]
selector.current(7)
selector.place(x="200px",y="75px")

generate_btn = Button(root,text="generate Password",bg="orange",fg="black",font=("ubuntu",15),cursor="hand2",command=password_generate)
generate_btn.bind("<Enter>",on_enter)
generate_btn.bind("<Leave>",on_leave)
generate_btn.pack(anchor="center",pady="50px")

result_lable = Label(root,text="Generated Password Here:-",bg="Yellowgreen",fg="brown",font=("ubuntu",12))
result_lable.place(x="20px",y="200px")

password =StringVar()
password_final =Entry(root, textvariable= password,state="readonly",fg="blue", font=("ubuntu",15))
password_final.place(x="200px",y="200px")

root.mainloop()



