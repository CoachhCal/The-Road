import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import math
import operator

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

p1 = player("", 0, "", 0, 0, "", "none", 100, 100, 100, 100)
bag = inventory(100, 0, 0, 0, 0, 0, 0)

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

        titlePicture = ImageTk.PhotoImage(Image.open("GUI/pictures/title2.jpg"))
        lblTitlePicture = tk.Label(initialPage,height=800, width=1100,image=titlePicture)
        initialPage.image=titlePicture
        lblTitlePicture.place(x=0, y=0)

        #if image doesnt work:
        # lblTitlePicture = tk.Label(initialPage,height=800, width=1100,bg="black")
        # lblTitlePicture.pack()

        lblGameName = tk.Label(initialPage, text="The Game", font="Arial 50", bg='#c5c5c5')
        lblGameName.place(relx=0.5, rely=0.1, anchor="center")

        lblCreatorName = tk.Label(initialPage, text="By: Calvin Murray", font="Arial 36", bg="grey")
        lblCreatorName.place(relx=0.01,rely= .95, anchor="w")

        lblDate = tk.Label(initialPage, text="2024", font="Arial 36", bg="grey")
        lblDate.place(relx = .96, rely= .95, anchor="e")

        btnBegin = tk.Button(initialPage, text="Click to Start", font="Arial 36", relief="solid", bg="grey",cursor="hand2", command=lambda: controller.show_frame(StartPage))
        btnBegin.place(relx=.5, rely=.6, anchor="center")


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        startPage = tk.Frame(self,width="1100", height="800", bg="black")
        startPage.pack()
        startPage.pack_propagate(0) #prevents frame from shrinking to fit widgets
        textChecker = self.register(self.validInput) #used for max character length in entry widgets

        lblTitle1 = tk.Label(startPage, text="Enter your characters information", font="Arial 30", bg='black', fg="gold")
        lblTitle1.place(relx=0.5, rely=0.07, anchor="center")

        nameVar = StringVar()
        lblName = tk.Label(startPage, text="Name: ", font="Arial 20", fg="gold", bg="black")
        lblName.place(relx=.075, rely=.175)
        entName = tk.Entry(startPage, bg="white", font="Arial 20", width=20, textvariable=nameVar, validate="key", validatecommand=(textChecker,'%P', 15, "letter"))
        entName.place(relx=.22, rely=.175)
        self.validName = tk.Label(startPage, bg="black",fg="gold",text="1-15 letters. No whitespaces",font="Arial 10")
        self.validName.place(relx=.28, rely=.222)

        skinVar = StringVar()
        lblSkinColor = tk.Label(startPage, text="Skin Color: ", font="Arial 20", fg="gold", bg="black")
        lblSkinColor.place(relx=.075, rely=.325)
        entSkinColor = tk.Entry(startPage, bg="white", font="Arial 20", width=20, textvariable=skinVar,validate="key", validatecommand=(textChecker,'%P', 10, "letter"))
        entSkinColor.place(relx=.22, rely=.325)
        self.validSkin = tk.Label(startPage, bg="black",fg="gold",text="3-10 letters. No whitespaces",font="Arial 10")
        self.validSkin.place(relx=.28, rely=.372)

        rbValue = StringVar()
        lblSex = tk.Label(startPage, text="Sex: ", font="Arial 20", fg="gold", bg="black")
        lblSex.place(relx=.075, rely=.475)
        lblBtnMale = LabelFrame(startPage, bd=2, bg="gold")
        lblBtnMale.place(relx=.22, rely=.47)
        rbMale = tk.Radiobutton(lblBtnMale, text="Male", variable=rbValue, value=1, font="Arial 18", bg="black", fg="gold",indicatoron=0,width=21,activebackground="black",activeforeground="gold",selectcolor="#022678",cursor="hand2")
        
        rbMale.pack()
        lblBtnFemale = LabelFrame(startPage, bd=2, bg="gold")
        lblBtnFemale.place(relx=.22, rely=.54)
        rbFemale = tk.Radiobutton(lblBtnFemale, text="Female", variable=rbValue, value=2, font="Arial 18", bg="black", fg="gold", indicatoron=0, width=21,activebackground="black",activeforeground="gold",selectcolor="#61023e",cursor="hand2")
        rbFemale.pack()
        self.validSex = tk.Label(startPage, bg="black",fg="black",text="Select one",font="Arial 10")
        self.validSex.place(relx=.33, rely=.6)
        

        ageVar = StringVar()
        lblAge = tk.Label(startPage, text="Age: ", font="Arial 20", fg="gold", bg="black")
        lblAge.place(relx=.585, rely=.175)
        entAge = tk.Entry(startPage, bg="white", font="Arial 20", width=10, textvariable=ageVar,validate="key", validatecommand=(textChecker,'%P', 2, "number"))
        entAge.place(relx=.7, rely=.175)
        self.validAge = tk.Label(startPage, bg="black",fg="gold",text="18-99",font="Arial 10")
        self.validAge.place(relx=.75, rely=.222)
        lblAgeUnit = tk.Label(startPage, text="years", font="Arial 15", fg="gold", bg="black")
        lblAgeUnit.place(relx=.85, rely=.19)

        heightVar = StringVar()
        lblHeight = tk.Label(startPage, text="Height: ", font="Arial 20", fg="gold", bg="black")
        lblHeight.place(relx=.585, rely=.325)
        entHeight = tk.Entry(startPage, bg="white", font="Arial 20", width=10, textvariable=heightVar,validate="key", validatecommand=(textChecker,'%P', 3, "number"))
        entHeight.place(relx=.7, rely=.325)
        self.validHeight = tk.Label(startPage, bg="black",fg="gold",text="120-300",font="Arial 10")
        self.validHeight.place(relx=.745, rely=.372)
        lblHeightUnit = tk.Label(startPage, text="cm", font="Arial 15", fg="gold", bg="black")
        lblHeightUnit.place(relx=.85, rely=.34)

        weightVar = StringVar()
        lblWeight = tk.Label(startPage, text="Weight: ", font="Arial 20", fg="gold", bg="black")
        lblWeight.place(relx=.585, rely=.475)
        entWeight = tk.Entry(startPage, bg="white", font="Arial 20", width=10, textvariable=weightVar,validate="key", validatecommand=(textChecker,'%P', 3, "number"))
        entWeight.place(relx=.7, rely=.475)
        self.validWeight = tk.Label(startPage, bg="black",fg="gold",text="50-999",font="Arial 10")
        self.validWeight.place(relx=.75, rely=.522)
        lblWeightUnit = tk.Label(startPage, text="lbs", font="Arial 15", fg="gold", bg="black")
        lblWeightUnit.place(relx=.85, rely=.49)

        lblTitle2 = tk.Label(startPage, text="Choose your mode", font="Arial 30", bg='black', fg="gold")
        lblTitle2.place(relx=0.5, rely=0.7, anchor="center")

        lblBtnStory = LabelFrame(startPage, bd=5, bg="gold")
        lblBtnStory.place(relx=.1, rely=.8)
        btnStory = tk.Button(lblBtnStory, text="Story Mode", font="Arial 30", relief="solid", bg="black",fg="gold", width=15, activebackground="gold", cursor="hand2", command= lambda: self.storyModeValidation(nameVar.get(), skinVar.get(), rbValue.get(), ageVar.get(), heightVar.get(), weightVar.get()))
        # btnStory.place(relx=.27, rely=.75, anchor="center")
        btnStory.pack()
        lblBtnQuick = LabelFrame(startPage, bd=5, bg="gold")
        lblBtnQuick.place(relx=.565, rely=.8)
        btnQuick = tk.Button(lblBtnQuick, text="Quick Play", font="Arial 30", relief="solid", bg="black",fg="gold", width=15, activebackground="gold", cursor="hand2")
        # btnQuick.place(relx=.73, rely=.75, anchor="center")
        btnQuick.pack()

    def storyModeValidation(self, nameVar, skinVar, rbValue, ageVar, heightVar, weightVar):
        count = 0 #used to check how many entries are valid
        var = [self.validName, self.validSkin,self.validSex, self.validAge, self.validHeight, self.validWeight] # used for loop
        val = [nameVar, skinVar, rbValue, ageVar, heightVar, weightVar] #used for loop
        for x in range(len(var)):
            if val[x] == "": #If empty
                var[x].configure(fg="red")
            elif var[x] == self.validSkin and len(val[x]) < 3: #if Skin color entry is less than 3 characters
                var[x].configure(fg="red")
            elif var[x] == self.validSex and int(val[x]) == "": #if neither radio button (sex) was selected
                var[x].configure(fg="red")
            elif var[x] == self.validAge and int(val[x]) < 18: # if age is less than 18
                var[x].configure(fg="red")
            elif var[x] == self.validHeight and not 120 <= int(val[x]) <= 300 : # if height is below 120 or over 300
                var[x].configure(fg="red")
            elif var[x] == self.validWeight and 50 > int(val[x]): #if weight is less than 50
                var[x].configure(fg="red")
            else: #when entry is correct
                if var[x] == self.validSex: #if sex selected, remove error text (turn it black to disppear)
                    var[x].configure(fg="black")
                else:
                    var[x].configure(fg="green") #turn all other error text green
            if var[x].cget("fg") == "green": #if text is green (entry is correct)
                count+=1 #add to counter
            if count == 5 and rbValue != "": # if all entrys correct
                if rbValue == 1:
                    p1.sex = "man"
                elif rbValue == 2:
                    p1.sex == "woman"
                p1.name = nameVar
                p1.age = int(ageVar)
                p1.color = skinVar
                p1.height = int(heightVar)
                p1.weight = int(weightVar)
                print("done")
                
            
    def validInput(self, text, maxLength, type):
        if text:
            if type == "letter":
                return len(text) <= int(maxLength) and text.isalpha()
            elif type == "number":
                return len(text) <= int(maxLength) and text.isdigit()
        return True
            
            
        
        # print(nameVar)
        # print(skinVar)
        # print(rbValue)
        # print(ageVar)
        # print(heightVar)
        # print(weightVar)


game = GameApp()


game.mainloop()