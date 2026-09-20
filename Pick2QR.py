from customtkinter import *
import os
from PIL import *
from PIL import Image 
from qrcode import *
import random
Set_Light = {"Light":["Dark","D"],"Dark":["Light","L"]}
hard = ["D", "E", "F", "G", "H", "I", "J", "K", "C"]
set_appearance_mode("dark")
set_default_color_theme("dark-blue")
class AppCreate(CTk):
    def __init__(self):
        super().__init__()
        for i in hard:
            if os.path.exists(f"{i}:/Pick2QR/"):
                self.hard = i
                break
            else:
                try:
                    os.mkdir(f"{i}:/Pick2QR/")
                    self.hard = i
                    break
                except:
                    pass
        self.buttonLight = CTkButton(self,text="D", width=11, height=20,command=self.SetBede)
        self.buttonLight.place(relx=0.95, y=10, anchor="ne")

        self.inputbox = CTkEntry(self,160,placeholder_text="Enter Text or Link")
        self.inputbox.pack(side="top",anchor="n",pady=30)
        self.buttonCreate = CTkButton(self, width=120, command=self.getBede)
        self.buttonCreate.pack(side="top", anchor="n")
        self.label = CTkLabel(self, text="", anchor="center")
        self.label.pack(side="bottom", anchor="n")

        self.loadImg = CTkLabel(self,text="",pady=200)
        self.loadImg.pack(side="bottom",anchor="n")

        self.geometry("300x400")
        self.title("Pick2QR")
        
    def getBede(self):
        if not self.inputbox.get() or len(self.inputbox.get()) < 1:
            return self.label.configure(text=f"Chizi Benevis")    
        rnt = random.randint(0,99999999999)
        self.bedebehesh = self.inputbox.get()
        self.final = str(self.bedebehesh[0:2]) + "_" + str(rnt)
        try:
            aks = make(self.inputbox.get())
            aks.save(f"{self.hard}:/Pick2QR/{self.final}.png")
        except:
            self.label.configure(text=f"error")
        self.label.configure(text=f"Files Saved At {self.hard}:/Pick2QR/{self.final}.png")    
        self.img = CTkImage(Image.open(f"{self.hard}:/Pick2QR/{self.final}.png"),Image.open(f"{self.hard}:/Pick2QR/{self.final}.png"),(179, 159))
        self.loadImg.configure(text="",image=self.img)
        self.label.after(5000, lambda: self.label.configure(text=""))
    def SetBede(self):
        set_appearance_mode(Set_Light[get_appearance_mode()][0])
        self.buttonLight.configure(text=Set_Light[get_appearance_mode()][1])

if __name__ == "__main__":
    bank = AppCreate()
    bank.mainloop()