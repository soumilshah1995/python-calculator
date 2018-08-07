import tkinter

calculator= tkinter.Tk()
calculator.title('Calculator')
calculator.resizable(0, 0)


Entry=tkinter.Entry(calculator,font=("Arial", 22), borderwidth= 1 ,)
Entry.insert(0, "0")
Entry.grid(row=0,column=0,columnspan=4)


# ROW 1 --------------------------------------------------------------

b_AC=tkinter.Button(calculator,text="AC",borderwidth=1,font=("Arial",20),)
b_AC.grid(row=1,column=0,sticky="NWNESWSE",)

b_C=tkinter.Button(calculator,text="C",borderwidth=1,font=("Arial",20))
b_C.grid(row=1,column=1,sticky="NWNESWSE")

b_X=tkinter.Button(calculator,text="X",borderwidth=1,font=("Arial",20))
b_X.grid(row=1,column=2,sticky="NWNESWSE")

b_divide=tkinter.Button(calculator,text="/",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("/"))
b_divide.grid(row=1,column=3,sticky="NWNESWSE")


# ROW 2 -------------------------------------------------------------------


b_7=tkinter.Button(calculator,text="7",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("7"))
b_7.grid(row=2,column=0,sticky="NWNESWSE")

b_8=tkinter.Button(calculator,text="8",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("8"))
b_8.grid(row=2,column=1,sticky="NWNESWSE")

b_9=tkinter.Button(calculator,text="9",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("9"))
b_9.grid(row=2,column=2,sticky="NWNESWSE")

b_mul=tkinter.Button(calculator,text="*",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("*"))
b_mul.grid(row=2,column=3,sticky="NWNESWSE")


# ROW 3----------------------------------------------------------------------


b_4=tkinter.Button(calculator,text="4",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("4"))
b_4.grid(row=3,column=0,sticky="NWNESWSE")

b_5=tkinter.Button(calculator,text="5",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("5"))
b_5.grid(row=3,column=1,sticky="NWNESWSE")

b_6=tkinter.Button(calculator,text="6",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("6"))
b_6.grid(row=3,column=2,sticky="NWNESWSE")

b_minus=tkinter.Button(calculator,text="-",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("-") )
b_minus.grid(row=3,column=3,sticky="NWNESWSE")

# ROW 4 ------------------------------------------------------------------------

b_1=tkinter.Button(calculator,text="1",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("1"))
b_1.grid(row=4,column=0,sticky="NWNESWSE")

b_2=tkinter.Button(calculator,text="2",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("2"))
b_2.grid(row=4,column=1,sticky="NWNESWSE")

b_3=tkinter.Button(calculator,text="3",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("3"))
b_3.grid(row=4,column=2,sticky="NWNESWSE")

b_plus=tkinter.Button(calculator,text="+",borderwidth=1,font=("Arial",20),command=lambda: appendToDisplay("+"))
b_plus.grid(row=4,column=3,sticky="NWNESWSE")


# last row
b_0=tkinter.Button(calculator,text="0",font=("Arial",20),borderwidth= 1,command=lambda: appendToDisplay("0"))
b_0.grid(row=5,column=0,columnspan=3,sticky="NWNESWSE")

b_equal=tkinter.Button(calculator,text="=",font=("Arial",20),borderwidth=1)
b_equal.grid(row=5,column=3,sticky="NSNESWSE")


b_label=tkinter.Label(calculator,text="Designed by Soumil Shah Version 1")
b_label.grid(row=6,column=0,columnspan=5)


def appendToDisplay(text):
    entryText=Entry.get()
    Text_l=len(entryText)
    if entryText == "0":
        replaceText(text)
    else:
        Entry.insert(Text_l,text)



def replaceText(text):
    Entry.delete(0)
    Entry.insert(0, text)


calculator.mainloop()