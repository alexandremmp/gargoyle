from Tkinter import *
from tkFileDialog import *
import tkMessageBox
import sys

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
	f = asksaveasfile(mode='w', defaultextension='.txt',
		filetypes= [('Text','.txt'), ('HTML', '.html'), ('CSS', '.css'), ('JS', '.js'), ('PHP', '.php'), ('Python', '.py')])
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		tkMessageBox.showerror(title="ATTENTION!", message="Unable to save file, please try again.")

def openFile():
	f = askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

root = Tk()
root.title("Gargoyle")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(("%dx%d") % (width, height))

text = Text(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), font=('Ubuntu', 16), bg='#282C34', fg='#ABB2BF', highlightthickness=0, undo=True)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newFile, accelerator="Cmd+N")
filemenu.add_command(label="Open...", command=openFile, accelerator="Cmd+O")
filemenu.add_separator()
filemenu.add_command(label="Save", command=saveFile, accelerator="Cmd+S")
filemenu.add_command(label="Save as...", command=saveAs, accelerator="Cmd+Shift+S")
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit, accelerator="Cmd+Q")

filemenu = Menu(menubar)
menubar.add_cascade(label="Help", menu=filemenu)
filemenu.add_command(label="Gargoyle Help", command=help)

root.config(menu=menubar)
root.mainloop()
