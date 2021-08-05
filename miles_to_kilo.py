from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=50)

# blank label

blank_label = Label()
blank_label.grid(column=0, row=0)
blank_label.config(padx=20, pady=5)

# Miles Entry
miles_entry = Entry(width=10)
miles_entry.grid(column=0, row=0)

# Miles Label

miles_label = Label(text="Miles")
miles_label.grid(column=1, row=0)
miles_label.config(padx=5, pady=5)


def button_click():
    miles = int(miles_entry.get())
    kilometers = miles * 1.609
    equal_label.config(text=f"is equal to {kilometers} Km")




# button calc

calculate = Button(text="Caclulate", command=button_click)
calculate.grid(column=1, row=1)

# Equal label

equal_label = Label(text=f"is equal to {0} Km")
equal_label.grid(column=0, row=1)
equal_label.config(padx=5, pady=5)
window.mainloop()
