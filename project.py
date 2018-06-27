from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

F1 = Frame(root,bg="grey60",width = 1400,height=45,relief=SUNKEN)
F1.pack(side=TOP)

F2 = Frame(root,width = 900,height=700,relief=SUNKEN)
F2.pack(side=LEFT)

F3 = Frame(root ,width = 400,height=700,relief=SUNKEN)
F3.pack(side=RIGHT)
localtime=time.asctime(time.localtime(time.time()))
l1 = Label(F1, font=( 'times' ,35, 'bold' ),text="Restaurant Management System",fg="saddle brown",bd=10,anchor='w')
l1.grid(row=0,column=0)
l2 = Label(F1, font=( 'roman' ,20, ),text=localtime,fg="brown",anchor=W)
l2.grid(row=1,column=0)
root.mainloop()
