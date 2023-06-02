import tkinter as tk
from tkinter import ttk


def start_translate():
	pass

window = tk.Tk()
window.geometry('505x300')

n = tk.StringVar()
srcchoosen = ttk.Combobox(window, width=30)
srcchoosen['values'] = (' January',
						' February',
						' March',
						' April',
						' May',
						' June',
						' July',
						' August',
						' September',
						' October',
						' November',
						' December')

srcchoosen.grid(row=0, column=0, padx=10, pady=5)
srcchoosen.current(0)

destchoosen = ttk.Combobox(window, width=30)
destchoosen['values'] = (' January',
						' February',
						' March',
						' April',
						' May',
						' June',
						' July',
						' August',
						' September',
						' October',
						' November',
						' December')

destchoosen.grid(row=0, column=1, padx=10, pady=5)

srcchoosen.bind("<<ComboboxSelected>>")
destchoosen.current(1)

src_text = tk.Text(window, height=10, width=30)
src_text.grid(row=1, column=0, columnspan=1, padx=5, pady=2)

dest_text = tk.Text(window, height=10, width=30)
dest_text.grid(row=1, column=1, columnspan=1, padx=1, pady=2)

translate_button = tk.Button(window, text='Translate', command=start_translate, width=10)
translate_button.grid(row=2, column=0, padx=5, pady=5, sticky='w')

window.mainloop()