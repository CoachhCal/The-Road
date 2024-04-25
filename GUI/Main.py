import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class player:
    def __init__(self, name, age, color, height, weight, sex, armor, max_health, health, stamina, max_stamina):
        self.name = name
        self.age = age
        self.color = color
        self.height = height
        self.weight = weight
        self.sex = sex
        self.armor = armor
        self.max_health = max_health
        self.health = health
        self.stamina = stamina
        self.max_stamina = max_stamina
    
    def total_health(self):
        return self.armor + self.max_health
    
class inventory:
    def __init__(self, gold, arrows, scaliber, lcaliber, grenades, health_potion, stamina_potion):
        self.gold = gold
        self.arrows = arrows
        self.scaliber = scaliber
        self.lcaliber = lcaliber
        self.grenades = grenades
        self.health_potion = health_potion
        self.stamina_potion = stamina_potion

class GameApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self, height=800, width=1100, bg="black")
        super().minsize(1100, 800) #super refers to the window
        # window.configure()
        window.pack(side="top", fill = "both", expand=True)

        self.frames = {}
        for F in (SplashPage, StartPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.place(height=800, width=1100)
        
        self.show_frame(SplashPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        
class SplashPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        initialPage = tk.Frame(self,width="1100", height="800")
        initialPage.pack()
        initialPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        titlePicture = ImageTk.PhotoImage(Image.open("pictures/title2.jpg"))
        lblTitlePicture = tk.Label(initialPage,height=800, width=1100,image=titlePicture)
        initialPage.image=titlePicture
        lblTitlePicture.place(x=0, y=0)

        lblGameName = tk.Label(initialPage, text="The Game", font="Arial 50", bg='#c5c5c5')
        lblGameName.place(relx=0.5, rely=0.1, anchor="center")

        lblCreatorName = tk.Label(initialPage, text="By: Calvin Murray", font="Arial 36", bg="grey")
        lblCreatorName.place(relx=0.01,rely= .95, anchor="w")

        lblDate = tk.Label(initialPage, text="2024", font="Arial 36", bg="grey")
        lblDate.place(relx = .96, rely= .95, anchor="e")

        btnBegin = tk.Button(initialPage, text="Click to Start", font="Arial 36", relief="solid", bg="grey", command=lambda: controller.show_frame(StartPage))
        btnBegin.place(relx=.5, rely=.6, anchor="center")


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        startPage = tk.Frame(self,width="1100", height="800", bg="black")
        startPage.pack()
        startPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        lblGameName = tk.Label(startPage, text="Enter your characters information", font="Arial 30", bg='black', fg="white")
        lblGameName.place(relx=0.5, rely=0.07, anchor="center")

        # self.lblCreatorName = ttk.Label(self.startPage, text="By: Calvin Murray", font="Arial 36", bg="grey")
        # self.lblCreatorName.place(relx=0.01,rely= .95, anchor="w")

        # self.lblDate = ttk.Label(self.startPage, text="2024", font="Arial 36", bg="grey")
        # self.lblDate.place(relx = .96, rely= .95, anchor="e")
        lblName = tk.Label(startPage, text="Name: ", font="Arial 20", fg="white", bg="black")
        lblName.place(relx=.075, rely=.15)
        entName = tk.Entry(startPage, bg="white", font="Arial 20", width=15)
        entName.place(relx=.22, rely=.15)

        lblSkinColor = tk.Label(startPage, text="Skin Color: ", font="Arial 20", fg="white", bg="black")
        lblSkinColor.place(relx=.075, rely=.25)
        entSkinColor = tk.Entry(startPage, bg="white", font="Arial 20", width=15)
        entSkinColor.place(relx=.22, rely=.25)

        rbValue = IntVar()
        lblSex = tk.Label(startPage, text="Sex: ", font="Arial 20", fg="white", bg="black")
        lblSex.place(relx=.075, rely=.35)
        rbMale = tk.Radiobutton(startPage, text="Male", variable=rbValue, value=1, font="Arial 20", bg="black", fg="white", )
        rbMale.place(relx=.22, rely=.345)
        rbFemale = tk.Radiobutton(startPage, text="Female", variable=rbValue, value=2, font="Arial 20", bg="black", fg="white", )
        rbFemale.place(relx=.22, rely=.405)


        btnStory = tk.Button(startPage, text="Story Mode", font="Arial 36", relief="solid", bg="grey", width=15)
        btnStory.place(relx=.27, rely=.75, anchor="center")
        btnTest = tk.Button(startPage, text="Quick Play", font="Arial 36", relief="solid", bg="grey", width=15)
        btnTest.place(relx=.73, rely=.75, anchor="center")




game = GameApp()


game.mainloop()