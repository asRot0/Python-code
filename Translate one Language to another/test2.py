import tkinter as tk
from tkinter import ttk

def update_selection(event):
    combobox2.current(combobox1.current())

# Create the Tkinter window
window = tk.Tk()
window.title("Combobox Example")

# Create the Combobox widgets
combobox1 = ttk.Combobox(window, values=['Option 1', 'Option 2', 'Option 3'])
combobox1.pack()

combobox2 = ttk.Combobox(window, values=['Choice A', 'Choice B', 'Choice C'])
combobox2.pack()

# Bind the selection event of combobox1 to update combobox2's selection
combobox1.bind("<<ComboboxSelected>>", update_selection)

# Set the initial selection for combobox1 and combobox2
combobox1.current(1)
combobox2.current(1)

# Start the Tkinter event loop
window.mainloop()
