import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Electrical Table")

# Data from the image
data = [
    ["", "(kW)", "L-N (V)", "(A)", "L-L (V)"],
    ["L1", "19.5", "231.8", "28.0", "L1-L2", "401.5"],
    ["L2", "19.2", "232.1", "27.6", "L2-L3", "402.0"],
    ["L3", "19.4", "232.7", "27.8", "L3-L1", "403.1"],
    ["FRE.", "50.4", "A.LN", "232.4", "A.PF", "0.99"],
]

# Colors mapping
colors = {
    "L1": "red", "L2": "goldenrod", "L3": "blue",
    "L1-L2": "red", "L2-L3": "goldenrod", "L3-L1": "blue",
    "FRE.": "black", "A.LN": "black", "A.PF": "black"
}

# Create a grid layout
for i, row in enumerate(data):
    for j, value in enumerate(row):
        fg_color = colors.get(value, "black")  # Default text color
        font_style = ("Arial", 12, "bold") if value in colors else ("Arial", 12)
        label = tk.Label(root, text=value, font=font_style, fg=fg_color, borderwidth=1, relief="solid", width=10, height=2)
        label.grid(row=i, column=j, padx=0, pady=0)

root.mainloop()
