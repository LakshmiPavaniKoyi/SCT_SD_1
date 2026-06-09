# ==========================================================
# TEMPERATURE CONVERTER
# Software Development Internship - Task 1
# Developed using Python & Tkinter
# ==========================================================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# ==========================================================
# LIST TO STORE CONVERSION HISTORY
# ==========================================================

history = []

# ==========================================================
# FUNCTION TO CONVERT TEMPERATURE
# ==========================================================

def convert_temperature():

    try:
        # Get temperature from entry box
        temp = float(temp_entry.get())

        # Get selected units
        from_unit = from_combo.get()
        to_unit = to_combo.get()

        # -------------------------------
        # Conversion Logic
        # -------------------------------

        if from_unit == to_unit:
            result = temp

        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (temp * 9 / 5) + 32

        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = temp + 273.15

        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (temp - 32) * 5 / 9

        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = ((temp - 32) * 5 / 9) + 273.15

        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = temp - 273.15

        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = ((temp - 273.15) * 9 / 5) + 32

        # -------------------------------
        # Display Result
        # -------------------------------

        result_label.config(
            text=f"Result: {result:.2f} {to_unit}"
        )

        # -------------------------------
        # Store Conversion History
        # -------------------------------

        record = (
            f"{temp} {from_unit}  →  "
            f"{result:.2f} {to_unit}"
        )

        history.append(record)

        # Keep only last 5 records
        if len(history) > 5:
            history.pop(0)

        history_box.delete(0, END)

        for item in history:
            history_box.insert(END, item)

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid numeric value."
        )

# ==========================================================
# FUNCTION TO CLEAR ALL DATA
# ==========================================================

def clear_fields():

    temp_entry.delete(0, END)

    result_label.config(text="Result:")

    history_box.delete(0, END)

    history.clear()

# ==========================================================
# MAIN WINDOW
# ==========================================================

root = Tk()

root.title("Temperature Converter")

root.geometry("550x600")

root.resizable(False, False)

# Soft pastel blue background
root.configure(bg="#EAF4FF")

# ==========================================================
# TITLE
# ==========================================================

title_label = Label(
    root,
    text="Temperature Converter",
    font=("Segoe UI", 22, "bold"),
    fg="#1E3A5F",      # Ink Blue
    bg="#EAF4FF"
)

title_label.pack(pady=15)

# ==========================================================
# TEMPERATURE INPUT
# ==========================================================

temperature_label = Label(
    root,
    text="Enter Temperature",
    font=("Segoe UI", 11),
    fg="#324A5F",
    bg="#EAF4FF"
)

temperature_label.pack()

temp_entry = Entry(
    root,
    width=25,
    font=("Segoe UI", 11),
    relief="solid",
    bd=1
)

temp_entry.pack(pady=8)

# ==========================================================
# FROM UNIT
# ==========================================================

from_label = Label(
    root,
    text="From",
    font=("Segoe UI", 11),
    fg="#324A5F",
    bg="#EAF4FF"
)

from_label.pack()

from_combo = ttk.Combobox(
    root,
    values=[
        "Celsius",
        "Fahrenheit",
        "Kelvin"
    ],
    width=22,
    state="readonly"
)

from_combo.pack(pady=8)

from_combo.current(0)

# ==========================================================
# TO UNIT
# ==========================================================

to_label = Label(
    root,
    text="To",
    font=("Segoe UI", 11),
    fg="#324A5F",
    bg="#EAF4FF"
)

to_label.pack()

to_combo = ttk.Combobox(
    root,
    values=[
        "Celsius",
        "Fahrenheit",
        "Kelvin"
    ],
    width=22,
    state="readonly"
)

to_combo.pack(pady=8)

to_combo.current(1)

# ==========================================================
# BUTTON FRAME
# ==========================================================

button_frame = Frame(
    root,
    bg="#EAF4FF"
)

button_frame.pack(pady=20)

# ==========================================================
# CONVERT BUTTON
# ==========================================================

convert_button = Button(
    button_frame,
    text="Convert",
    width=12,
    command=convert_temperature,
    font=("Segoe UI", 10, "bold"),
    bg="#A8D5BA",           # Pista Green
    activebackground="#95C9A8",
    relief="flat",
    cursor="hand2"
)

convert_button.grid(
    row=0,
    column=0,
    padx=10
)

# ==========================================================
# CLEAR BUTTON
# ==========================================================

clear_button = Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_fields,
    font=("Segoe UI", 10, "bold"),
    bg="#F4B6B6",           # Soft Coral
    activebackground="#E89E9E",
    relief="flat",
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)

# ==========================================================
# RESULT LABEL
# ==========================================================

result_label = Label(
    root,
    text="Result:",
    font=("Segoe UI", 14, "bold"),
    fg="#1E3A5F",
    bg="#EAF4FF"
)

result_label.pack(pady=15)

# ==========================================================
# HISTORY TITLE
# ==========================================================

history_title = Label(
    root,
    text="Recent Conversions",
    font=("Segoe UI", 12, "bold"),
    fg="#324A5F",
    bg="#EAF4FF"
)

history_title.pack()

# ==========================================================
# HISTORY LISTBOX
# ==========================================================

history_box = Listbox(
    root,
    width=55,
    height=8,
    font=("Segoe UI", 10),
    bg="#F5FFF7",
    relief="solid",
    bd=1
)

history_box.pack(pady=10)

# ==========================================================
# FOOTER
# ==========================================================

footer = Label(
    root,
    text="Developed using Python & Tkinter",
    font=("Segoe UI", 9, "italic"),
    fg="#6B7280",
    bg="#EAF4FF"
)

footer.pack(side=BOTTOM, pady=10)

# ==========================================================
# START APPLICATION
# ==========================================================

root.mainloop()