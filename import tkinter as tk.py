import tkinter as tk

def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        si = (p * t * r) / 100

        ci = p * ((1 + r / 100) ** t) - p

        result_label.config(
            text=f"Simple Interest: ₹{si:.2f}\nCompound Interest: ₹{ci:.2f}"
        )
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")
root.configure(bg="#E0F8EC")

label_font = ("Arial", 12)

tk.Label(root, text="Principal (₹):", font=label_font, bg="#E0F8EC").grid(row=0, column=0, padx=10, pady=10, sticky="e")
principal_entry = tk.Entry(root, font=label_font, bg="#FFF5EE")
principal_entry.grid(row=0, column=1, padx=10)

tk.Label(root, text="Time (years):", font=label_font, bg="#E0F8EC").grid(row=1, column=0, padx=10, pady=10, sticky="e")
time_entry = tk.Entry(root, font=label_font, bg="#FFF5EE")
time_entry.grid(row=1, column=1, padx=10)

tk.Label(root, text="Rate (%):", font=label_font, bg="#E0F8EC").grid(row=2, column=0, padx=10, pady=10, sticky="e")
rate_entry = tk.Entry(root, font=label_font, bg="#FFF5EE")
rate_entry.grid(row=2, column=1, padx=10)

calc_button = tk.Button(root, text="Calculate Interest", font=("Arial", 13),
                        bg="#FF7F50", fg="white", command=calculate_interest)
calc_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#E0F8EC", fg="#4B0082")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
