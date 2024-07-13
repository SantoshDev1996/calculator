import tkinter as tk

def btnClear():
    global Val
    val=""
    input_value.set("")

def btnEquals():
        global val
        result = str(val.replace('÷','/'))
        input_value.set(result)

# Create the main window
main = tk.Tk()
main.title("mycalci")
main.geometry("360x381+500+200")

# Variable to hold the operator and input value
operator = ""
input_value = tk.StringVar()

# Entry widget to display input
display = tk.Entry(main, textvariable=input_value, bd=29, justify="right", bg="yellow", font=("Arial", 20, "bold",))
display.grid(row=0, columnspan=4)

# Define function to update input_value when button is clicked
def button_click(number):
    current = input_value.get()
    input_value.set(current + number)

# Buttons for numbers
btn7 = tk.Button(main, text="7", font=("Arial", 20, "bold"), command=lambda: button_click("7"))
btn7.grid(row=1, column=0)
btn8 = tk.Button(main, text="8", font=("Arial", 20, "bold"), command=lambda: button_click("8"))
btn8.grid(row=1, column=1)
btn9 = tk.Button(main, text="9", font=("Arial", 20, "bold"), command=lambda: button_click("9"))
btn9.grid(row=1, column=2)
btn_add = tk.Button(main, text="+", font=("Arial", 20, "bold"), command=lambda: button_click("+"))
btn_add.grid(row=1, column=3)


btn4 = tk.Button(main, text="4", font=("Arial", 20, "bold"), command=lambda: button_click("4"))
btn4.grid(row=2, column=0)
btn5 = tk.Button(main, text="5", font=("Arial", 20, "bold"), command=lambda: button_click("5"))
btn5.grid(row=2, column=1)
btn6= tk.Button(main, text="6", font=("Arial", 20, "bold"), command=lambda: button_click("6"))
btn6.grid(row=2, column=2)
btn_sub = tk.Button(main, text="-", font=("Arial", 20, "bold"), command=lambda: button_click("-"))
btn_sub.grid(row=2, column=3)

btn1 = tk.Button(main, text="1", font=("Arial", 20, "bold"), command=lambda: button_click("1"))
btn1.grid(row=3, column=0)
btn2 = tk.Button(main, text="2", font=("Arial", 20, "bold"), command=lambda: button_click("2"))
btn2.grid(row=3, column=1)
btn3 = tk.Button(main, text="3", font=("Arial", 20, "bold"), command=lambda: button_click("3"))
btn3.grid(row=3, column=2)
btn_mul= tk.Button(main, text="*", font=("Arial", 20, "bold"), command=lambda: button_click("*"))
btn_mul.grid(row=3, column=3)

btnc = tk.Button(main, text="c", font=("Arial", 20, "bold"), command=btnClear)
btnc.grid(row=4, column=0)
btn0 = tk.Button(main, text="0", font=("Arial", 20, "bold"), command=lambda: button_click("0"))
btn0.grid(row=4, column=1)
btndiv = tk.Button(main, text="÷", font=("Arial", 20, "bold"), command=lambda: button_click("÷"))
btndiv.grid(row=4, column=2)
btnequal = tk.Button(main, text="=", font=("Arial", 20, "bold"), command=btnEquals)
btnequal.grid(row=4, column=3)

# Start the main loop
main.mainloop()