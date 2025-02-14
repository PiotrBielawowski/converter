import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        value = float(entry_value.get())
        conversion_type = selected_type.get()

        if conversion_type == "Temperature":
            from_unit = entry_from.get().capitalize()
            to_unit = entry_to.get().capitalize()

            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
                result_label.config(text=f"{value} °C = {result:.2f} °F")
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
                result_label.config(text=f"{value} °F = {result:.2f} °C")
            else:
                messagebox.showerror("Error", "Please enter valid temperature units (Celsius/Fahrenheit)!")

        elif conversion_type == "Distance":
            from_unit = entry_from.get().capitalize()
            to_unit = entry_to.get().capitalize()

            if from_unit == "Kilometers" and to_unit == "Miles":
                result = value * 0.621371
                result_label.config(text=f"{value} km = {result:.2f} mi")
            elif from_unit == "Miles" and to_unit == "Kilometers":
                result = value / 0.621371
                result_label.config(text=f"{value} mi = {result:.2f} km")
            else:
                messagebox.showerror("Error", "Please enter valid distance units (Kilometers/Miles)!")

        elif conversion_type == "Weight":
            from_unit = entry_from.get().capitalize()
            to_unit = entry_to.get().capitalize()

            if from_unit == "Kilograms" and to_unit == "Pounds":
                result = value * 2.20462
                result_label.config(text=f"{value} kg = {result:.2f} lbs")
            elif from_unit == "Pounds" and to_unit == "Kilograms":
                result = value / 2.20462
                result_label.config(text=f"{value} lbs = {result:.2f} kg")
            else:
                messagebox.showerror("Error", "Please enter valid weight units (Kilograms/Pounds)!")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def update_units(event=None):
    category = selected_type.get()

    if category == "Temperature":
        entry_from.delete(0, tk.END)
        entry_to.delete(0, tk.END)
        entry_from.insert(0, "Celsius")
        entry_to.insert(0, "Fahrenheit")
    elif category == "Distance":
        entry_from.delete(0, tk.END)
        entry_to.delete(0, tk.END)
        entry_from.insert(0, "Kilometers")
        entry_to.insert(0, "Miles")
    elif category == "Weight":
        entry_from.delete(0, tk.END)
        entry_to.delete(0, tk.END)
        entry_from.insert(0, "Kilograms")
        entry_to.insert(0, "Pounds")

def swap_units():
    temp = entry_from.get()
    entry_from.delete(0, tk.END)
    entry_from.insert(0, entry_to.get())
    entry_to.delete(0, tk.END)
    entry_to.insert(0, temp)

root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x400")


tk.Label(root, text="Unit Converter", font=("Arial", 18, "bold"), background="#f0f0f0").pack(pady=15)

selected_type = tk.StringVar(value="Temperature")
category_frame = tk.Frame(root)
category_frame.pack(pady=5)

tk.Radiobutton(category_frame, text="Temperature", variable=selected_type, value="Temperature", command=update_units).pack(side="left", padx=10)
tk.Radiobutton(category_frame, text="Distance", variable=selected_type, value="Distance", command=update_units).pack(side="left", padx=10)
tk.Radiobutton(category_frame, text="Weight", variable=selected_type, value="Weight", command=update_units).pack(side="left", padx=10)

unit_frame = tk.Frame(root)
unit_frame.pack(pady=10)

entry_from = tk.Entry(unit_frame, font=("Arial", 12), width=15)
entry_from.pack(side="left", padx=5)

tk.Label(unit_frame, text="to", font=("Arial", 12)).pack(side="left", padx=5)

entry_to = tk.Entry(unit_frame, font=("Arial", 12), width=15)
entry_to.pack(side="left", padx=5)

swap_button = tk.Button(root, text="Swap Units", command=swap_units)
swap_button.pack(pady=10)

tk.Label(root, text="Enter value to convert:", font=("Arial", 12)).pack(pady=10)
entry_value = tk.Entry(root, font=("Arial", 14))
entry_value.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), foreground="blue")
result_label.pack(pady=10)

update_units()

root.mainloop()
