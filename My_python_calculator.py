from tkinter import *
root = Tk()
root.geometry("400x500")
root.resizable(0,0)
root.title("its mine calculator")

myVariable =  StringVar()

first_frame = Frame(root, width=400 , height=100,bg = "green")
first_frame.pack(side = "top")


 
input_field = Entry(first_frame,width = 400,font=("arial 20 bold" ),textvariable= myVariable,justify= "right" )
input_field.grid(row=0, column=0)
input_field.pack(ipady=200)

second_frame =  Frame(root, width=400, height=400, bg ="white")
#second_frame.pack(side= BOTTOM)

clear = Button(second_frame,text ="clear" , fg = "black" ).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)


root.mainloop()
