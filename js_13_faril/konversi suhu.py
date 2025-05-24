import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry.get())
        if var.get() == 1:  # Celsius to Fahrenheit
            converted = (temperature * 9/5) + 32
            result_label.config(text=f"{temperature} Celsius = {converted} Fahrenheit")
        elif var.get() == 2:  # Fahrenheit to Celsius
            converted = (temperature - 32) * 5/9
            result_label.config(text=f"{temperature} Fahrenheit = {converted} Celsius")
    except ValueError:
        result_label.config(text="Masukkan nilai suhu yang valid!")

root = tk.Tk()
root.title("Konversi Suhu")

label = tk.Label(root, text="Masukkan nilai suhu:")
label.pack()

entry = tk.Entry(root)
entry.pack()

var = tk.IntVar()

celsius_to_fahrenheit = tk.Radiobutton(root, text="Celsius ke Fahrenheit", variable=var, value=1)
celsius_to_fahrenheit.pack()

fahrenheit_to_celsius = tk.Radiobutton(root, text="Fahrenheit ke Celsius", variable=var, value=2)
fahrenheit_to_celsius.pack()

convert_button = tk.Button(root, text="Konversi", command=convert_temperature)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()