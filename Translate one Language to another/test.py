import tkinter as tk
from tkinter import ttk

def submit():
	aaa = monthchoosen.get()
	print(aaa)
	#n.set('')


# Creating tkinter window
window = tk.Tk()
window.geometry('350x250')
window.title('icon lagao')
#path='pic_icon\VIRUS6.ico'
#window.iconbitmap(path)
# Label
ttk.Label(window, text = "Select the Month :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 15, padx = 10, pady = 25)

n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27,
							textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
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

monthchoosen.grid(column = 1, row = 15)
tk.Button(window,text='submit',command=submit).grid(column=0,row=16,padx=1,pady=3)


# Shows february as a default value
monthchoosen.current(1)
window.mainloop()
