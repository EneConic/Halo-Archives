from tkinter import *
from PIL import ImageTk, Image
import os.path

DB = Toplevel()
DB.title("UNSC Database")
DB.geometry("728x410")

#Logo Background
BG_Locate = os.path.relpath('Halo-Archives\BG.jpg')
BG = ImageTk.PhotoImage(Image.open(BG_Locate))
BG_Place = Label(DB, image=BG)
BG_Place.pack(fill=BOTH, expand=YES)

#Hello
Hello_Text = "HELLO"
Hello = Label(DB, text=Hello_Text, font=('HaloRegular', 15), bg='gray')
Hello.place(x=130, y=50)

DB.mainloop()