from tkinter import *
from functools import partial

root = Tk()

root['bg']='#A4A4A4'
root.geometry("1000x600+10+10")
root.title('Crashtest')

def hello(piece, event):
	print("yousk2")

echiquier = Canvas(root, width=600, height=600, background='white')
echiquier.pack()

carre = echiquier.create_rectangle(200, 200, 300, 300, fill="black")
echiquier.tag_bind(carre, '<Button-1>', partial(hello, 1))

root.mainloop()
