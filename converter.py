from tkinter import *
top = Tk()
top.config(bg = "#ff3d05")
# Code to add widgets will go here...
top.title("Currency Converter")
top.geometry("600x500")

frm1 = Frame(top,height = 20,bg = "#ff3d05")
frm1.pack()

frm2 = Frame(top,height = 30,bg = "#ff3d05")
frm2.pack()

frm3 = Frame(top,height = 20,bg = "#ff3d05")
frm3.pack()

frm4 = Frame(top,height = 30,bg = "#ff3d05")
frm4.pack()

frm5 = Frame(top,height = 20,bg = "#ff3d05")
frm5.pack()

frm6 = Frame(top,height = 20,bg = "#ff3d05")
frm6.pack()

frm7 = Frame(top,height = 20,bg = "#ff3d05")
frm7.pack()

frm8 = Frame(top,height = 50,bg = "#ff3d05")
frm8.pack()

frm9 = Frame(top,height = 20,bg = "#ff3d05")
frm9.pack()

frm10 = Frame(top,height = 40,bg = "#ff3d05")
frm10.pack()

frm11 = Frame(top,height = 20,bg = "#ff3d05")
frm11.pack()

frm12 = Frame(top,height = 30,bg = "#ff3d05")
frm12.pack()

frm13 = Frame(top,height = 20,bg = "#ff3d05")
frm13.pack()

frm14 = Frame(top,height = 30,bg = "#ff3d05")
frm14.pack()

frm15 = Frame(top,height = 20,bg = "#ff3d05")
frm15.pack()

def calu():
	g = int(ce.get())
	v = s.get()
	ve = ss.get()
	if (v == "Dollars" and ve == "Rupee"):
		res.config(text = g*82)

l1 = Label(frm2,text = "From :- ",bg = "red",font = ("helvetica",10,"bold"))
l1.pack(side = "left")

s = StringVar()
listc = ["Arabs","Dollars","Euros","Pounds","Pennys","Rupee"]
s.set("Select Currency")
drp = OptionMenu(frm2,s,*listc)
drp.pack()

l = Label(frm4,text = "Enter the value",font = ("helvetica",10,"bold"),bg = "red")
l.pack(side = "left")

ce = Entry(frm4,width = 10)
ce.pack()

l2 = Label(frm6,text = "To :- ",bg = "red",font = ("helvetica",10,"bold"))
l2.pack(side = "left")

ss = StringVar()
ss.set("Select Currency")
drps = OptionMenu(frm6,ss,*listc)
drps.pack()

cal = Button(frm8,text = "Calculate",bg = "magenta",command = calu)
cal.pack()

res = Button(frm10)
res.pack()

top.mainloop()