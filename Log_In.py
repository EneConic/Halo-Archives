"""
File created by Lieutent Vera - 08/11/2021 - 1100

This program is a database for all weapon and ship
information for the Halo universe.

WARNING: AUTHORIZED PERSONNEL ONLY. IF FOUND BY ANY ALIENS, DELETE
ANY AND ALL ACCESS IN ACCORDANCE WITH THE COLE PROTOCOL. FAILURE
TO FOLLOW THE COLE PROTOCOL WILL RESULT IN A COURT MARTIAL.
"""

import random as r
import string as s
from tkinter import *
from PIL import ImageTk, Image
import os.path

#Set Frame
DB = Tk()
DB.title("UNSC Database")
DB.geometry("728x410")

def LogIn_Check():
    #LogIn_Label = Label(DB, bg='gray', font=('HaloRegular', 15))

    if (os.path.isfile('.\\Halo-Archives\\UNSC_Username.txt') and os.path.isfile('.\\Halo-Archives\\UNSC_Password.txt') == True):

        with open('.\\Halo-Archives\\UNSC_Username.txt', 'r') as UN:
            with open('.\\Halo-Archives\\UNSC_Password.txt', 'r') as PW:
                UN_Text = UN.read()
                PW_Text = PW.read()

                if ID_Entry.get() == UN_Text and Password_Entry.get() == PW_Text:
                    def Main_Menu():
                        DB.iconify()
                        import MainMenu 

                    Main_Menu()

                elif ID_Entry.get() != open('.\\Halo-Archives\\UNSC_Username.txt', 'r') or Password_Entry.get() != open('.\\Halo-Archives\\UNSC_Password.txt', 'r'):
                    #Incorrect Message
                    Incorrect_Message = "One or more fields are incorrect.\nPlease resubmit your information."
                    Incorrect_Label = Label(DB, text=Incorrect_Message, bg='gray', font=('HaloRegular', 15))
                    DB.update()
                    Incorrect_Label.place(x=180, y=180)

    elif (os.path.isfile('.\\Halo-Archives\\UNSC_Username.txt') or os.path.isfile('.\\Halo-Archives\\UNSC_Password.txt') == False):
        #Error Message
        Error_Message = "No file on Record.\nCreating log in...."
        Error_Label = Label(DB, text=Error_Message, bg='gray', font=('HaloRegular', 15))
        #Error_Label = LogIn_Label.configure(text=Error_Message)
        DB.update()
        Error_Label.place(x=255, y=180)
        #Error_Label_Destroy = LogIn_Label.configure(text="")

        #ID Generator
        Number = 0
        ID_List = []
        while Number < 10:
            ID_List.append(r.randint(0, 9))
            Number += 1

        ID_String = ""
        ID_Number = ID_String.join([str(num) for num in ID_List])
        
        Save_Path = '.\\Halo-Archives'
        Username_File = 'UNSC_Username.txt'
        User_Join = os.path.join(Save_Path, Username_File)
        UNSC_Username = open(User_Join, 'w')
        UNSC_Username.write(ID_Number)
        UNSC_Username.close()

        #Password Generator
        Password = "".join(r.choices(s.ascii_letters + s.digits + s.punctuation, k=10))

        Save_Path = '.\\Halo-Archives'
        Password_File = 'UNSC_Password.txt'
        Pass_Join = os.path.join(Save_Path, Password_File)
        UNSC_Password = open(Pass_Join, 'w')
        UNSC_Password.write(Password)
        UNSC_Password.close()        

    elif ID_Entry.get() or Password_Entry.get() == "":
        #Invalid Entry
        Invalid_Text = "Please fill out all forms."
        Invalid_Label = Label(DB, text=Invalid_Text,bg='gray', font=('HaloRegular', 15))
        #Invalid_Label = LogIn_Label.configure(text=Invalid_Text)
        DB.update()
        Invalid_Label.place(x=220, y=180)
        #Invalid_Label_Destroy = LogIn_Label.configure(text="")
    
    #LogIn_Label.place(x=238, y=180)

#Logo Background
BG_Locate = os.path.relpath('Halo-Archives\BG.jpg')
BG = ImageTk.PhotoImage(Image.open(BG_Locate))
BG_Place = Label(DB, image=BG)
BG_Place.pack(fill=BOTH, expand=YES)

#Welcome Label
Welcome_Text = "UNSC MILTARY DATABASE\nAUTHORIZED PERSONNEL ONLY"
Welcome = Label(DB, text=Welcome_Text, font=('HaloRegular', 15), bg='gray')
Welcome.place(x=130, y=50)

#ID Label
ID_Text = "ID"
ID = Label(DB, text=ID_Text, bg='gray', font=('HaloRegular', 10))
ID.place(x=160, y=300)

#Username Entry
ID_Entry = Entry(DB, width='25')
ID_Entry.place(x=100, y=320)

#Password Label
Password_Text = "Password"
Password = Label(DB, text=Password_Text, bg='gray', font=('HaloRegular', 10))
Password.place(x=515, y=300)

#Password Entry
Password_Entry = Entry(DB, width='25')
Password_Entry.place(x=480, y=320)

#Log In
LogIn_Button = Button(DB, text="Log In", width='10', command=LogIn_Check)
LogIn_Button.place(x=330, y=315)

DB.mainloop()