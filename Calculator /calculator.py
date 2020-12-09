
"""
    docstring for Calculator
    Description:
    This is the main class.
    Record:
    |Sr.No.| Name | Date | Changes made |
    |1.|Ansh Sharma|8th December,2020|Creation of the class|
    |2.|Ansh Shaema|9th December 2020|Basic Calculator|
"""

from tkinter import *

# Imports everything from tkinter


expression = ""


# Globally Declare the expression variable


# Function to update the expression in the text entry box
def press(num):
    # Point out the global expression variable
    global expression

    # Concatenation of String
    expression = expression + str(num)

    # Update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used for handling errors like divbyzero errors,etc.
    try:
        global expression

        # eval Function Evaluates the exprssion and str function converts the result to String
        total = str(eval(expression))

        equation.set(total)

        # Intialize expression variable to an empty string \
        expression = ""

    # If error is generated then handling the error
    except:
        equation.set("Error")
        expression = ""


# Function to clear the contents of the text box
def clear():
    global expression
    expression = ""
    equation.set("")



#Driver code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of the window
    gui.configure(background="black")

    # Set the title of the GUI window
    gui.title("Calculator")

    # Set the size of the window
    gui.geometry("270x150")

    # StringVar() is the variable class we create as an instance of this class
    equation = StringVar()

    # Create the text entry box for showing the expression
    expression_field = Entry(gui, textvariable=equation)

    # Grid Method is used for placing the widgets at respective positions in a table like structure
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set("Enter expression")

    # Create buttons and place at a particular location inside the root window
    # When user presses the button, the command or the function affiliated to it is executed

    button1 = Button(gui, text='1', fg="white", bg="orange", command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text='2', fg="white", bg="orange", command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text='3', fg="white", bg="orange", command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text='4', fg="white", bg="orange", command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text='5', fg="white", bg="orange", command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text='6', fg="white", bg="orange", command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text='7', fg="white", bg="orange", command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text='8', fg="white", bg="orange", command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text='9', fg="white", bg="orange", command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text='0', fg="white", bg="orange", command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text='+', fg="white", bg="orange", command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text='-', fg="white", bg="orange", command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text='*', fg="white", bg="orange", command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text='/', fg="white", bg="orange", command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text='=', fg="white", bg="orange", command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='clear', fg="white", bg="orange", command=clear, height=1, width=7)
    clear.grid(row=5, column=1)

    decimal = Button(gui, text='.', fg="white", bg="orange", command=lambda: press("."), height=1, width=7)
    decimal.grid(row=6, column=0)

    gui.mainloop()
