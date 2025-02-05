from tkinter import * 
from tkinter import messagebox 
  
root = Tk() 
root.geometry("300x200") 
  
w = Label(root, text ='Messagebox examples', font = "50") 
w.place(x = 0, y = 0)
w.pack() 
  
one = messagebox.showinfo("showinfo", "Information") 
  
two = messagebox.showwarning("showwarning", "Warning") 
  
three = messagebox.showerror("showerror", "Error") 
  
four = messagebox.askquestion("askquestion", "Are you sure?") 
print (four)

while four == 'no':
    four = messagebox.askquestion("askquestion", "Are you sure?") 


five = messagebox.askokcancel("askokcancel", "Want to continue?") 
  
six = messagebox.askyesno("askyesno", "Find the value?") 
print (six)
if six == True:
    print ('pressed')
    lab1 = Label (root, text = 'you asked for it')
    lab1.place(x = 0, y = 90)
  
  
seven = messagebox.askretrycancel("askretrycancel", "Try again?")   
  
root.mainloop() 