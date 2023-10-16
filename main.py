import tkinter as tk
from tkinter import ttk


def bd():
    num = binary_entry.get()
    decimal = int(num, 2)
    result_label.config(text=f"{decimal} is the equivalent")


def bo():
    num = binary_entry.get()
    decimal = int(num, 2)
    octal = oct(decimal)
    result_label.config(text=f"{octal} is the equivalent")


def bh():
    num = binary_entry.get()
    decimal = int(num, 2)
    hexadecimal = hex(decimal)
    result_label.config(text=f"{hexadecimal} is the equivalent")


def db():
    num = decimal_entry.get()
    binary = bin(int(num))
    result_label.config(text=f"{binary} is equivalent")


def do():
    num = decimal_entry.get()
    octal = oct(int(num))
    result_label.config(text=f"{octal} is equivalent")


def dh():
    num = decimal_entry.get()
    hexadecimal = hex(int(num))
    result_label.config(text=f"{hexadecimal} is equivalent")


def on_choice_select(event):
    choice = choice_var.get()
    if choice.startswith("Decimal"):
        decimal_entry.config(state="normal")
        binary_entry.config(state="disabled")
    else:
        binary_entry.config(state="normal")
        decimal_entry.config(state="disabled")


def switch():
    option_mapping = {
        "Binary to Decimal": 1,
        "Binary to Octal": 2,
        "Binary to Hexadecimal": 3,
        "Decimal to Binary": 4,
        "Decimal to Octal": 5,
        "Decimal to Hexadecimal": 6
    }
    choice = option_mapping.get(choice_var.get())

    if choice is not None:
        if choice == 1:
            bd()
        elif choice == 2:
            bo()
        elif choice == 3:
            bh()
        elif choice == 4:
            db()
        elif choice == 5:
            do()
        elif choice == 6:
            dh()
    else:
        result_label.config(text="Naaaaaaah, you got nothing 🚀")


root = tk.Tk()
root.title("Number Converter")

# Style for buttons and labels
style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 12))
style.configure("TLabel", font=('Helvetica', 12))

# Create a frame for layout
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Create a Combobox for choosing an option
ttk.Label(mainframe, text="Choose an option:").grid(column=1, row=1)
options = ["Binary to Decimal", "Binary to Octal", "Binary to Hexadecimal", "Decimal to Binary", "Decimal to Octal",
           "Decimal to Hexadecimal"]
choice_var = tk.StringVar()
choice_combobox = ttk.Combobox(mainframe, textvariable=choice_var, values=options)
choice_combobox.grid(column=2, row=1, padx=10, pady=10)
choice_combobox.set(options[0])

# Create a binary entry
ttk.Label(mainframe, text="Enter your binary number:").grid(column=1, row=2)
binary_entry = ttk.Entry(mainframe)
binary_entry.grid(column=2, row=2, padx=10, pady=10)

# Create a decimal entry
ttk.Label(mainframe, text="Enter your decimal number:").grid(column=1, row=3)
decimal_entry = ttk.Entry(mainframe)
decimal_entry.grid(column=2, row=3, padx=10, pady=10)

# Create a result label
result_label = ttk.Label(mainframe, text="", anchor="center")
result_label.grid(column=1, row=4, columnspan=2, pady=10)

# Create a Convert button
convert_button = ttk.Button(mainframe, text="Convert", command=switch)
convert_button.grid(column=2, row=5, padx=10, pady=10)

# Bind the dropdown event to the on_choice_select function
choice_combobox.bind("<<ComboboxSelected>>", on_choice_select)

# Adjust the spacing around widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Start the GUI main loop
root.mainloop()
