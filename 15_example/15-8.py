from tkinter import *
root=Tk()
root.geometry('320x240')
mycanvas=Canvas(root)
mycanvas.pack()
photo=PhotoImage(file='1.png')
mycanvas.create_image(100,100,image=photo)
root.mainloop()
