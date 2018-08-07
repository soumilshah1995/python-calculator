import tkinter

calculator= tkinter.Tk()
calculator.title('Calculator')
calculator.resizable(0, 0)


Entry=tkinter.Entry(calculator,font=("Arial", 22), borderwidth= 1 ,)
Entry.insert(0, "0")
Entry.grid(row=0,column=0,columnspan=4)



b_AC=tkinter.Button(calculator,text="AC",borderwidth=1,font=("Arial",20))
b_AC.grid(row=1,column=0,sticky="NWNESWSE")

b_C=tkinter.Button(calculator,text="C",borderwidth=1,font=("Arial",20))
b_C.grid(row=1,column=1,sticky="NWNESWSE")

b_X=tkinter.Button(calculator,text="X",borderwidth=1,font=("Arial",20))
b_X.grid(row=1,column=2,sticky="NWNESWSE")

b_divide=tkinter.Button(calculator,text="/",borderwidth=1,font=("Arial",20))
b_divide.grid(row=1,column=3,sticky="NWNESWSE")





b_7=tkinter.Button(calculator,text="7",borderwidth=1,font=("Arial",20))
b_7.grid(row=2,column=0,sticky="NWNESWSE")

b_8=tkinter.Button(calculator,text="8",borderwidth=1,font=("Arial",20))
b_8.grid(row=2,column=1,sticky="NWNESWSE")

b_9=tkinter.Button(calculator,text="9",borderwidth=1,font=("Arial",20))
b_9.grid(row=2,column=2,sticky="NWNESWSE")

b_mul=tkinter.Button(calculator,text="*",borderwidth=1,font=("Arial",20))
b_mul.grid(row=2,column=3,sticky="NWNESWSE")





calculator.mainloop()