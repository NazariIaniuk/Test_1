from tkinter import *
from tkinter import ttk

root = Tk()


nums = Listbox(root, height=5)
nums.grid(column=0, row=0, sticky=(N,W,E,S))
scroll = ttk.Scrollbar(root, orient=VERTICAL, command=nums.yview)
scroll.grid(column=1, row=0, sticky=(N,S))
nums['yscrollcommand'] = scroll.set
ttk.Label(root, text="Status message here", anchor=(W)).grid(column=0, columnspan=2, row=1, sticky=(W,E))
root.grid_columnconfigure(0, weight=1) # (index, weight)
root.grid_rowconfigure(0, weight=1)
for i in range(1,101):
    nums.insert('end', 'Line %d of 100' % i)
root.mainloop()
