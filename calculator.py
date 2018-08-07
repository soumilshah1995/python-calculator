import tkinter

calculator= tkinter.Tk()
calculator.title('Calculator')
calculator.resizable(0, 0)


Entry=tkinter.Entry(calculator,font=("Arial", 22), borderwidth= 1 ,)
Entry.insert(0, "0")
Entry.grid(row=0,column=0)

calculator.mainloop()
