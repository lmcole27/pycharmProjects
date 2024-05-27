from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def calculate():
    x = float(input.get()) * 1.60934
    ans_label = Label(text=x, font=("Arial", 14, "bold"))
    ans_label.config(pady=20, padx=20)
    ans_label.grid(column=1, row=1)


km_label = Label(text="KM", font=("Arial", 14, "bold"))
km_label.config(pady=20, padx=20)
km_label.grid(column=2, row=1)

mi_label = Label(text="Miles", font=("Arial", 14, "bold"))
mi_label.config(pady=20, padx=20)
mi_label.grid(column=2, row=0)

eq_label = Label(text="is equal to", font=("Arial", 14, "bold"))
eq_label.config(pady=20, padx=20)
eq_label.grid(column=0, row=1)

my_button = Button(text="Calculate", font=("Arial", 14, "bold"), command=calculate)
my_button.config(pady=20, padx=20)
my_button.grid(row=2, column=1)

input = Entry()
input.grid(row=0, column=1)
input.focus()

mainloop()
