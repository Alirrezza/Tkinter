from tkinter import *
from PIL import Image,ImageTk

def resizer(event,imgs,canvase):
    
    imgs[1]=imgs[0].resize((event.width,event.height),Image.Resampling.LANCZOS)
    imgs[2]=ImageTk.PhotoImage(imgs[1])
    canvase[0].create_image(0,0, image=imgs[2],anchor='nw')


root=Tk()
# root.geometry('800x500') #Optional


img=Image.open('RAM.jpg')  #You can write your image address insted of 'RAM.JPG'
img1=Image.open('RAM.jpg')  #You can write your image address insted of 'RAM.JPG'
img2=ImageTk.PhotoImage(img)
imgs=[img,img1,img2]

my_canvase=Canvas(root)
my_canvase.pack(fill='both',expand=True)
my_canvase.create_image(0,0,image=imgs[2],anchor='nw')
canvas=[my_canvase]


root.bind('<Configure>',lambda event:resizer(event,imgs,canvas))

root.mainloop()