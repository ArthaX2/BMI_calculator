import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}", foreground="red")
    except ValueError:
        result_label.config(text="Please enter valid numbers", foreground="red")

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")
window.configure(bg="#f8f9fa")

style = ttk.Style()
style.theme_use('clam')

style.configure("TFrame", background="#f8f9fa")
style.configure("TLabel", background="#f8f9fa", font=("Helvetica", 12))
style.configure("TButton", background="#007bff", foreground="white", font=("Helvetica", 12))
style.map("TButton", background=[("active", "#0056b3")])

title_label = ttk.Label(window, text="BMI Calculator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

frame = ttk.Frame(window, padding="20 20 20 20", borderwidth=2, relief="solid")
frame.pack(padx=10, pady=10, fill="both", expand=True)

height_label = ttk.Label(frame, text="Height (m):")
height_label.grid(row=0, column=0, pady=10, padx=5, sticky="e")
height_entry = ttk.Entry(frame, width=15, font=("Helvetica", 12))
height_entry.grid(row=0, column=1, pady=10, padx=5)

weight_label = ttk.Label(frame, text="Weight (kg):")
weight_label.grid(row=1, column=0, pady=10, padx=5, sticky="e")
weight_entry = ttk.Entry(frame, width=15, font=("Helvetica", 12))
weight_entry.grid(row=1, column=1, pady=10, padx=5)

calculate_button = ttk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, pady=20)

result_label = ttk.Label(frame, text="")
result_label.grid(row=3, columnspan=2, pady=10)

window.mainloop()
