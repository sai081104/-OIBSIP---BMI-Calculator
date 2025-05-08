import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

user_data = {}

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        bmi = weight / (height ** 2)
        bmi_result = f"BMI: {bmi:.2f}"
        category = categorize_bmi(bmi)
        category_result = f"Category: {category}"
        result_label.config(text=f"{bmi_result}\n{category_result}")

        # Store data for visualization
        user_data["BMI"] = user_data.get("BMI", []) + [bmi]
        user_data["Category"] = user_data.get("Category", []) + [category]

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def visualize_data():
    if "BMI" in user_data:
        plt.figure(figsize=(10, 6))
        plt.plot(user_data["BMI"], marker="o", linestyle="-", color="blue", label="BMI")
        plt.title("BMI Trend Analysis")
        plt.xlabel("Attempts")
        plt.ylabel("BMI Value")
        plt.grid(alpha=0.3)
        plt.legend()
        plt.show()
    else:
        messagebox.showinfo("No Data", "No data to visualize.")

# GUI Setup
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("400x300")

tk.Label(app, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(app)
weight_entry.pack(pady=5)

tk.Label(app, text="Height (m):").pack(pady=5)
height_entry = tk.Entry(app)
height_entry.pack(pady=5)

result_label = tk.Label(app, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

tk.Button(app, text="Calculate BMI", command=calculate_bmi).pack(pady=5)
tk.Button(app, text="Visualize Data", command=visualize_data).pack(pady=5)

app.mainloop()
