from Tkinter import *
from tkFileDialog import *

filename = None

def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFile():
	global filename
	t = text.get(0.0, END)
	f = open(filename, 'w')
	f.write(t)
	f.close()

def saveAs():
	f = asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title="Sorry!", message="Unable to save file, please try again...")

def openFile():
	f = askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)


root = Tk()
root.title("Gargoyle")
root.minsize(width=600, height=600)
root.maxsize(width=700, height=700)

text = Text(root, width=700, height=700, font=("Helvetica",16))
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open...", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save as...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

filemenu = Menu(menubar)
menubar.add_cascade(label="Help", menu=filemenu)
filemenu.add_command(label="Gargoyle Help", command=help)

root.config(menu=menubar)
root.mainloop()
