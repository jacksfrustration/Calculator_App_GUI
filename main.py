import tkinter as tk
from tkinter import messagebox

# Global variables
first_num = ""
second_num = ""
separated = False
operator = ""

# Mathematical operations
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x ** y
}

def concatenate_digit(digit):
    """Append the chosen digit to either the first or the second number."""
    global first_num, second_num, separated
    if separated:
        second_num += digit
    else:
        first_num += digit
    update_result_label()

def clear_entry():
    """Delete the last digit in the current value."""
    global first_num, second_num
    if separated:
        second_num = second_num[:-1]
    else:
        first_num = first_num[:-1]
    update_result_label()

def clear_everything_absolute():
    """Clear the text in the screen and reset all variables."""
    clear_everything()
    result_lbl.config(text="")

def clear_everything():
    """Reset all variables."""
    global first_num, second_num, separated, operator
    first_num = ""
    second_num = ""
    separated = False
    operator = ""

def equals_func():
    """Perform the mathematical operation."""
    global first_num, second_num, operator, separated
    try:
        num1 = float(first_num)
        num2 = float(second_num)
        result = operations[operator](num1, num2)
        result_lbl.config(text=f"{first_num} {operator} {second_num} = {result}")
        if checkbutton.get() == 1:
            first_num = str(result)
            second_num = ""
            separated = True
            result_lbl.config(text=f"{first_num}")
        else:
            clear_everything()
    except (ValueError, ZeroDivisionError, KeyError):
        messagebox.showerror(title="Error", message="Invalid input or operation")
        clear_everything()

def op_set(op):
    """Set the operator for the mathematical calculation."""
    global operator, separated
    separated = True
    operator = op

def update_result_label():
    """Update the result label text."""
    global first_num, second_num, operator
    if separated:
        result_lbl.config(text=f"{first_num} {operator} {second_num}")
    else:
        result_lbl.config(text=f"{first_num}")

# GUI setup
window = tk.Tk()
window.title("Calculator App")

result_lbl = tk.Label(text="Mathematical Operations")
result_lbl.grid(row=0, column=0, columnspan=6)

# Buttons for digits
for i in range(1, 10):
    tk.Button(text=str(i), command=lambda i=i: concatenate_digit(str(i))).grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3)

# Other buttons
tk.Button(text="0", command=lambda: concatenate_digit("0")).grid(row=4, column=1)
tk.Button(text=".", command=lambda: concatenate_digit(".")).grid(row=4, column=0)
tk.Button(text="<|", command=clear_entry).grid(row=4, column=2)
tk.Button(text="+", command=lambda: op_set("+")).grid(row=1, column=3)
tk.Button(text="-", command=lambda: op_set("-")).grid(row=2, column=3)
tk.Button(text="/", command=lambda: op_set("/")).grid(row=3, column=3)
tk.Button(text="*", command=lambda: op_set("*")).grid(row=4, column=3)
tk.Button(text="=", command=equals_func).grid(row=3, column=4)
tk.Button(text="^", command=lambda: op_set("^")).grid(row=2, column=4)
tk.Button(text="CE", command=clear_everything_absolute).grid(row=4, column=4)

# Checkbox for continuing with the result
checkbutton = tk.IntVar()
res_check = tk.Checkbutton(window, text="Continue with result", variable=checkbutton, onvalue=1, offvalue=0)
res_check.grid(row=5, column=1)

window.mainloop()