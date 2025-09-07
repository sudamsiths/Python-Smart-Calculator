import tkinter as tk
from tkinter import messagebox

def calculate(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid Operator")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("350x250")
root.config(bg="#222")

# Input fields
tk.Label(root, text="Number 1:", fg="white", bg="#222").pack(pady=5)
entry1 = tk.Entry(root, width=20, font=("Arial", 14))
entry1.pack()

tk.Label(root, text="Number 2:", fg="white", bg="#222").pack(pady=5)
entry2 = tk.Entry(root, width=20, font=("Arial", 14))
entry2.pack()

# Buttons
button_frame = tk.Frame(root, bg="#222")
button_frame.pack(pady=10)

for operator in ["+", "-", "*", "/"]:
    btn = tk.Button(button_frame, text=operator, width=5, height=2,
                    bg="#00ADB5", fg="white", font=("Arial", 14, "bold"),
                    command=lambda op=operator: calculate(op))
    btn.pack(side="left", padx=5)

# Result
result_label = tk.Label(root, text="Result: ", fg="#FFD369", bg="#222", font=("Arial", 16, "bold"))
result_label.pack(pady=20)

root.mainloop()
