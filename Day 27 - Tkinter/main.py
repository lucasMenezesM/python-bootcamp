from tkinter import *

# def button_clicked():
#     print("I got clicked")
#     input_result = input.get()
#     print(input_result)
#     main_label["text"] = input_result


window = Tk()
window.title("Miles to KM")
window.minsize(height=100, width=300)
window.config(padx=20, pady=20)

# main_label = Label(text="Hello world", font=("Arial", 25))
# main_label.grid(column=0, row=0)

# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)

# new_button = Button(text="New button")
# new_button.grid(column=2, row=3)

# input = Entry(width=10)
# input.grid(column=3, row=3)


def calculate_miles():
    result = float(miles_input.get()) * 1,609
    km_result.config(text=result)
    return result

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)

km_result = Label(text=0)
km_result.grid(column=1, row=1)
km_result.config(padx=10, pady=10)

km_label= Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate_miles)
calculate_button.grid(column=1, row=2)


window.mainloop()