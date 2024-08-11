try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from PIL import ImageTk, Image
import math

import random


"""
IMPORTANT:

https://deckofcardsapi.com/

https://deckofcardsapi.com/static/img/AS.png

"""



class PlayerClass:
    def __init__(self, name, age, color, height, weight, sex, armor, maxHealth, health, stamina, maxStamina):
        self.name = name
        self.age = age
        self.color = color
        self.height = height
        self.weight = weight
        self.sex = sex
        self.armor = armor
        self.maxHealth = maxHealth
        self.health = health
        self.stamina = stamina
        self.maxStamina = maxStamina
    
    def totalHealth(self):
        return self.armor + 100
    
class GameClass:
    def __init__(self, mode, nextFunction, location, choice, enemies, damDealt, damTaken, arrows, sCal, mCal, grenades, special, hPotion, sPotion, goldSpent, goldEarned):
        self.mode = mode
        self.nextFunction = nextFunction
        self.location = location #Can either be road, or town
        self.choice = choice
        self.enemies = enemies
        self.damDealt = damDealt
        self.damTaken = damTaken
        self.arrows = arrows
        self.sCal = sCal
        self.mCal = mCal
        self.grenades = grenades
        self.special = special
        self.hPotion = hPotion
        self.sPotion = sPotion
        self.goldSpent = goldSpent
        self.goldEarned = goldEarned
    
class ArmorClass:
    name = "None"
    healthBonus = 0
    goldCost = 0
    image = "None"

class Inventory:
    def __init__(self, gold, arrows, scaliber, lcaliber, grenades, healthPotion, staminaPotion):
        self.gold = gold
        self.arrows = arrows
        self.scaliber = scaliber
        self.lcaliber = lcaliber
        self.grenades = grenades
        self.healthPotion = healthPotion
        self.staminaPotion = staminaPotion

class EnemyClass:
    level = 0
    name = "none"
    health = 0
    attack1 = ["name", 0,1]
    attack2 = ["name", 0,1]
    attack3 = ["name", 0,1]
    finalMove = "none"
    reward = 0
    picture = "none"

    def attack(attackList):
        return random.randint(attackList[1], attackList[2])

def list_from_csv(file, access_mode):
    import csv
    with open(file, access_mode) as current_file:
        list = []
        full_list = csv.reader(current_file)
        for row in full_list:
            list.append(row)
        del list[0]
        for x in range(len(list)):
            for y in range(len(list[x])):
                if list[x][y].replace(".","").replace("-","").isnumeric():
                    try:
                        list[x][y] = int(list[x][y])
                    except ValueError:
                        list[x][y] = float(list[x][y])
    return list

def random_monster(p_monster_list):
    """Chooses a random monster from a 2D list"""
    import random
    random_number = random.randint(1,len(p_monster_list)-1) #chooses a numbr between 1 and however many monsters there are in the list
    return p_monster_list[random_number] #return the monsters index value

def create_player_weapon_list():
    """Creates 6 empty weapon slots (2D list) """
    list = []
    for x in range(6):
        list.append([])
        for y in range(9):
            list[x].append("")
    return list

# try:
monsterList = list_from_csv("csvFiles/monster_list.csv", "r")
weapons_list = list_from_csv("csvFiles/weapons_list.csv", "r")
ammoList = list_from_csv("csvFiles/ammo_list.csv", "r")
armorList = list_from_csv("csvFiles/armor_list.csv", "r")
potionList = list_from_csv("csvFiles/potions_list.csv", "r")
cardsList = list_from_csv("csvFiles/cards_list.csv", "r")
# except:


playerWeapons = create_player_weapon_list()
playerWeapons[0] = weapons_list[4]
playerWeapons[1] = weapons_list[10]
playerWeapons[2] = weapons_list[11]
playerWeapons[3] = weapons_list[19]
playerWeapons[4] = weapons_list[21]
playerWeapons[5] = weapons_list[22]
GameInfo = GameClass(1, "none", "road", "none",0,0,0,0,0,0,0,0,0,0,0,0)
Enemy = EnemyClass
Armor = ArmorClass

Player = PlayerClass("Calvin", 26, "white", 70, 152, "man", "none", 500, 500, 100, 100)
Bag = Inventory(0, 0, 300, 400, 9, 50, 0)

class GameApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self, height=800, width=1100, bg="black")
        super().minsize(1100, 800) #super refers to the window
        # window.configure()
        window.pack(side="top", fill = "both", expand=True)

        self.frames = {}
        for F in (SplashPage, StartPage, MainPage, FightPage, TownPage, ArenaPage, ShopPage, AmmoPage, ArmorPage, PotionPage, WeaponPage, MeleePage, ArcheryPage, SidearmPage, RiflePage, SpecialPage, BlackPage, EndPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.place(height=800, width=1100)
        
        self.showFrame(SplashPage)

    def showFrame(self,cont):
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

        #if image doesnt work:
        # lblTitlePicture = tk.Label(initialPage,height=800, width=1100,bg="black")
        # lblTitlePicture.pack()

        lblGameName = tk.Label(initialPage, text="The Road", font="Arial 50", bg='#c5c5c5')
        lblGameName.place(relx=0.5, rely=0.1, anchor="center")

        lblCreatorName = tk.Label(initialPage, text="By: Calvin Murray", font="Arial 36", bg="grey")
        lblCreatorName.place(relx=0.01,rely= .95, anchor="w")

        lblDate = tk.Label(initialPage, text="2024", font="Arial 36", bg="grey")
        lblDate.place(relx = .96, rely= .95, anchor="e")

        btnBegin = tk.Button(initialPage, text="Click to Start", font="Arial 36", relief="solid", bg="grey",cursor="hand2", command=lambda: self.yup(controller))
        btnBegin.place(relx=.5, rely=.6, anchor="center")

    def yup(self, controller):
        # controller.showFrame(StartPage)
        # controller.showFrame(FightPage)
        # controller.frames[FightPage].updateWeapons()
        # controller.frames[FightPage].updateInfo()
        # controller.frames[FightPage].enemyBattle(1,4,"Dragon", 0)
        controller.showFrame(MainPage)
        controller.frames[MainPage].three8(controller)
        # controller.trial(MainPage)

        # controller.showFrame(TownPage)
        # controller.showFrame(BlackPage)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        startPage = tk.Frame(self,width="1100", height="800", bg="black")
        startPage.pack()
        startPage.pack_propagate(0) #prevents frame from shrinking to fit widgets
        textChecker = self.register(self.validInput) #used for max character length in entry widgets

        lblTitle1 = tk.Label(startPage, text="Build your character", font="Arial 30", bg='black', fg="white")
        lblTitle1.place(relx=0.5, rely=0.07, anchor="center")

        nameVar = tk.StringVar()
        lblName = tk.Label(startPage, text="Name: ", font="Arial 20", fg="white", bg="black")
        lblName.place(relx=.075, rely=.175)
        entName = tk.Entry(startPage, bg="white", font="Arial 20", width=20, textvariable=nameVar, validate="key", validatecommand=(textChecker,'%P', 15, "letter"))
        entName.place(relx=.22, rely=.175)
        self.validName = tk.Label(startPage, bg="black",fg="white",text="1-15 letters. No spaces",font="Arial 10")
        self.validName.place(relx=.28, rely=.222)

        skinVar = tk.StringVar()
        lblSkinColor = tk.Label(startPage, text="Skin Color: ", font="Arial 20", fg="white", bg="black")
        lblSkinColor.place(relx=.075, rely=.325)
        entSkinColor = tk.Entry(startPage, bg="white", font="Arial 20", width=20, textvariable=skinVar,validate="key", validatecommand=(textChecker,'%P', 10, "letter"))
        entSkinColor.place(relx=.22, rely=.325)
        self.validSkin = tk.Label(startPage, bg="black",fg="white",text="3-10 letters. No whitespaces",font="Arial 10")
        self.validSkin.place(relx=.28, rely=.372)

        rbValue = tk.StringVar()
        lblSex = tk.Label(startPage, text="Sex: ", font="Arial 20", fg="white", bg="black")
        lblSex.place(relx=.075, rely=.475)
        lblBtnMale = tk.LabelFrame(startPage, bd=2, bg="white")
        lblBtnMale.place(relx=.22, rely=.47)
        rbMale = tk.Radiobutton(lblBtnMale, text="Male", variable=rbValue, value=1, font="Arial 18", bg="black", fg="white",indicatoron=0,width=21,activebackground="black",activeforeground="white",selectcolor="#022678",cursor="hand2")
        rbMale.pack()

        lblBtnFemale = tk.LabelFrame(startPage, bd=2, bg="white")
        lblBtnFemale.place(relx=.22, rely=.54)
        rbFemale = tk.Radiobutton(lblBtnFemale, text="Female", variable=rbValue, value=2, font="Arial 18", bg="black", fg="white", indicatoron=0, width=21,activebackground="black",activeforeground="white",selectcolor="#61023e",cursor="hand2")
        rbFemale.pack()
        self.validSex = tk.Label(startPage, bg="black",fg="black",text="Select one",font="Arial 10")
        self.validSex.place(relx=.33, rely=.6)
        

        ageVar = tk.StringVar()
        lblAge = tk.Label(startPage, text="Age: ", font="Arial 20", fg="white", bg="black")
        lblAge.place(relx=.585, rely=.175)
        entAge = tk.Entry(startPage, bg="white", font="Arial 20", width=10, textvariable=ageVar,validate="key", validatecommand=(textChecker,'%P', 2, "number"))
        entAge.place(relx=.7, rely=.175)
        self.validAge = tk.Label(startPage, bg="black",fg="white",text="18-99",font="Arial 10")
        self.validAge.place(relx=.75, rely=.222)
        lblAgeUnit = tk.Label(startPage, text="years", font="Arial 15", fg="white", bg="black")
        lblAgeUnit.place(relx=.85, rely=.19)

        heightVarFt = tk.StringVar()
        heightVarIn = tk.StringVar()
        lblHeight = tk.Label(startPage, text="Height: ", font="Arial 20", fg="white", bg="black")
        lblHeight.place(relx=.585, rely=.325)

        entHeightFt = tk.Entry(startPage, bg="white", font="Arial 20", width=3, textvariable=heightVarFt,validate="key", validatecommand=(textChecker,'%P', 1, "number"))
        entHeightFt.place(relx=.7, rely=.325)
        self.validHeightFt = tk.Label(startPage, bg="black",fg="white",text="3-9",font="Arial 10")
        self.validHeightFt.place(relx=.712, rely=.372)
        lblHeightUnitFt = tk.Label(startPage, text="ft", font="Arial 15", fg="white", bg="black")
        lblHeightUnitFt.place(relx=.748, rely=.34)

        entHeightIn = tk.Entry(startPage, bg="white", font="Arial 20", width=4, textvariable=heightVarIn,validate="key", validatecommand=(textChecker,'%P', 2, "number"))
        entHeightIn.place(relx=.78, rely=.325)
        self.validHeightIn = tk.Label(startPage, bg="black",fg="white",text="0-12",font="Arial 10")
        self.validHeightIn.place(relx=.795, rely=.372)
        lblHeightUnitIn = tk.Label(startPage, text="in", font="Arial 15", fg="white", bg="black")
        lblHeightUnitIn.place(relx=.85, rely=.34)

        weightVar = tk.StringVar()
        lblWeight = tk.Label(startPage, text="Weight: ", font="Arial 20", fg="white", bg="black")
        lblWeight.place(relx=.585, rely=.475)
        entWeight = tk.Entry(startPage, bg="white", font="Arial 20", width=10, textvariable=weightVar,validate="key", validatecommand=(textChecker,'%P', 3, "number"))
        entWeight.place(relx=.7, rely=.475)
        self.validWeight = tk.Label(startPage, bg="black",fg="white",text="50-999",font="Arial 10")
        self.validWeight.place(relx=.75, rely=.522)
        lblWeightUnit = tk.Label(startPage, text="lbs", font="Arial 15", fg="white", bg="black")
        lblWeightUnit.place(relx=.85, rely=.49)

        lblTitle2 = tk.Label(startPage, text="Choose your mode", font="Arial 30", bg='black', fg="white")
        lblTitle2.place(relx=0.5, rely=0.7, anchor="center")

        lblBtnStory = tk.LabelFrame(startPage, bd=5, bg="gold")
        lblBtnStory.place(relx=.11, rely=.8)
        btnStory = tk.Button(lblBtnStory, text="Story Mode", font="Arial 30", relief="solid", bg="black",fg="gold", width=15, activebackground="gold", cursor="hand2", command= lambda: self.modeValidation(controller, nameVar.get(), skinVar.get(), rbValue.get(), ageVar.get(), heightVarFt.get(), heightVarIn.get(), weightVar.get(), 1))
        # btnStory.place(relx=.27, rely=.75, anchor="center")
        btnStory.pack()
        lblBtnQuick = tk.LabelFrame(startPage, bd=5, bg="gold")
        lblBtnQuick.place(relx=.565, rely=.8)
        btnQuick = tk.Button(lblBtnQuick, text="Quick Play", font="Arial 30", relief="solid", bg="black",fg="gold", width=15, activebackground="gold", cursor="hand2", command= lambda: self.modeValidation(controller, nameVar.get(), skinVar.get(), rbValue.get(), ageVar.get(), heightVarFt.get(), heightVarIn.get(), weightVar.get(), 2))
        # btnQuick.place(relx=.73, rely=.75, anchor="center")
        btnQuick.pack()

    def modeValidation(self, controller, nameVar, skinVar, rbValue, ageVar, heightVarFt, heightVarIn, weightVar, btnValue):
        count = 0 #used to check how many entries are valid
        var = [self.validName, self.validSkin,self.validSex, self.validAge, self.validHeightFt, self.validHeightIn, self.validWeight] # used for loop
        val = [nameVar, skinVar, rbValue, ageVar, heightVarFt, heightVarIn, weightVar] #used for loop
        for x in range(len(var)):
            if val[x] == "": #If empty
                var[x].configure(fg="red")
            elif var[x] == self.validSkin and len(val[x]) < 3: #if Skin color entry is less than 3 characters
                var[x].configure(fg="red")
            elif var[x] == self.validSex and int(val[x]) == "": #if neither radio button (sex) was selected
                var[x].configure(fg="red")
            elif var[x] == self.validAge and int(val[x]) < 18: # if age is less than 18
                var[x].configure(fg="red")
            elif var[x] == self.validHeightFt and not 3 <= int(val[x]) <= 9 : # if height entry in feet is between 3 and 9
                var[x].configure(fg="red")
            elif var[x] == self.validHeightIn and not 0 <= int(val[x]) <= 12 : # if inches entry is between 0 and 12
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
            if count == 6 and rbValue != "": # if all entrys correct
                Player = PlayerClass(nameVar, int(ageVar), skinVar, (int(heightVarFt) * 12) + int(heightVarIn), int(weightVar), "man", "none", 100, 100, 100, 100)
                if int(rbValue) == 1:
                    Player.sex = "man"
                elif int(rbValue) == 2:
                    Player.sex = "woman"
                # Player.name = nameVar
                # Player.age = int(ageVar)
                # Player.color = skinVar
                # Player.height = (int(heightVarFt) * 12) + int(heightVarIn)
                # Player.weight = int(weightVar)
                GameInfo = GameClass(btnValue, "none", "none", "none",0,0,0,0,0,0,0,0,0,0,0,0)
                if btnValue == 1:
                    GameInfo.location = "road"
                    controller.showFrame(MainPage)
                    controller.frames[MainPage].one1(controller)
                elif btnValue == 2:
                    GameInfo.location = "town"
                    controller.showFrame(TownPage)
                
    def validInput(self, text, maxLength, type):
        if text:
            if type == "letter":
                return len(text) <= int(maxLength) and text.isalpha()
            elif type == "number":
                return len(text) <= int(maxLength) and text.isdigit()
        return True
            
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.mainPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.mainPage.pack()
        self.mainPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        titlePicture = ImageTk.PhotoImage(Image.open("pictures/title2.jpg"))
        lblTitlePicture = tk.Label(self.mainPage,height=800, width=1100,image=titlePicture)
        self.mainPage.image=titlePicture
        lblTitlePicture.place(x=0, y=0)

        self.lblHealth = tk.Label(self.mainPage, height=2, width=30,highlightbackground="white", highlightthickness=2, bg="black",fg="white", font="Arial 15",anchor="w",padx=20, pady=20, text="Health : "+str(Player.health)+"/"+str(Player.maxHealth)+"\n\nHealth potions: "+str(Bag.healthPotion)+" (+"+str(potionList[0][1])+")")
        self.lblHealth.place(relx=.1045, rely=.63)

        self.btnHealth = tk.Button(self.mainPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="sunken", borderwidth=4, command=self.healthPotion)
        self.btnHealth.place(relx=.35, rely=.637)
        try:
            self.picHealth = ImageTk.PhotoImage(Image.open(potionList[0][3]))
            self.btnHealth.configure(width=70, height=70, image=self.picHealth)
        except:
            self.btnHealth.configure(width=11, height=4, text=potionList[0][0])

        self.lblStamina = tk.Label(self.mainPage, height=2, width=30,highlightbackground="white", highlightthickness=2, bg="black",fg="white", font="Arial 15",anchor="w",padx=20, pady=20, text="Stamina : "+str(Player.stamina)+"/"+str(Player.maxStamina)+"\n\nStamina potions: "+str(Bag.staminaPotion)+" (+"+str(potionList[1][1])+")")
        self.lblStamina.place(relx=.4465, rely=.63)

        self.btnStamina = tk.Button(self.mainPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="sunken", borderwidth=4, command=self.staminaPotion)
        self.btnStamina.place(relx=.692, rely=.637)
        try:
            self.picStamina = ImageTk.PhotoImage(Image.open(potionList[1][3]))
            self.btnStamina.configure(width=70, height=70, image=self.picStamina)
        except:
            self.btnStamina.configure(width=11, height=4, text=potionList[1][0])

        self.lblGold = tk.Label(self.mainPage, height=2, width=7,highlightbackground="white", highlightthickness=2, bg="black",fg="gold", font="Arial 15",padx=20, pady=20, text="Gold:\n\n"+str(Bag.gold))
        self.lblGold.place(relx=.783, rely=.63)

        self.mainText = tk.Text(self.mainPage, state="disabled", height=16, width=75, bg="black", highlightbackground="white", highlightthickness=2, fg="white", font="Arial 15", wrap="word", padx=20)
        self.mainText.place(relx=.5, rely=.397, anchor="center")

        self.lblChoice = tk.Label(self.mainPage, height=3, width=78, bg="black", highlightbackground="white", highlightthickness=2, fg="white", font="Arial 15", pady=10)
        self.lblChoice.place(relx=.5, rely=.9, anchor="center")

        self.btnYes = tk.Button(self.mainPage, height=2, width=20,bg="grey",fg="white",state="disabled", relief="sunken", cursor="x_cursor", font="Arial 19")
        self.btnYes.place(relx=.114, rely=.853)

        self.btnNo = tk.Button(self.mainPage, height=2, width=20,bg="grey",fg="white", state="disabled", relief="sunken", cursor="x_cursor", font="Arial 19")
        self.btnNo.place(relx=.604, rely=.853)

    def healthPotion(self):
        if Bag.healthPotion > 0 and Player.health < Player.maxHealth:
            Bag.healthPotion -= 1
            GameInfo.hPotion+=1
            Player.health += potionList[0][1]
            if Player.health > Player.maxHealth:
                Player.health = Player.maxHealth
            self.updateInfo()

    def staminaPotion(self):
        if Bag.staminaPotion > 0 and Player.stamina < Player.maxStamina:
            Bag.staminaPotion -= 1
            GameInfo.sPotion+=1
            Player.stamina += potionList[1][1]
            if Player.stamina > Player.maxStamina:
                Player.stamina = Player.maxStamina
            self.updateInfo()

    def updateInfo(self):
        self.lblGold.configure(text="Gold:\n\n"+str(Bag.gold))
        self.lblHealth.configure(text="Health : "+str(Player.health)+"/"+str(Player.maxHealth)+"\n\nHealth potions: "+str(Bag.healthPotion)+" (+"+str(potionList[0][1])+")")
        self.lblStamina.configure(text="Stamina : "+str(Player.stamina)+"/"+str(Player.maxStamina)+"\n\nStamina potions: "+str(Bag.staminaPotion)+" (+"+str(potionList[1][1])+")")

    def updateText(self, text): #displays the text in the text box
        self.mainText.configure(state="normal")
        self.mainText.insert(tk.END, text)
        self.mainText.configure(state="disabled")
 
    def snapBottom(self):
        self.mainText.see("end")
        self.after(1000, self.snapBottom)
    
    def clearBox(self):
        self.mainText.configure(state="normal")
        self.mainText.delete(0.0, "end")
        self.mainText.configure(state="disabled")

    def btnDisbaled(self):
        self.btnYes.configure(state = "disabled", text="", cursor="x_cursor")
        self.btnNo.configure(state = "disabled", text="", cursor="x_cursor")
        self.lblChoice.configure(text="")

    def newChoice(self, controller, btnOne, btnTwo, newText, cmdOne, cmdTwo):
        self.lblChoice.configure(text=newText)
        self.btnYes.configure(state = "normal", text=btnOne, cursor="hand2", command=lambda: cmdOne(controller))
        self.btnNo.configure(state = "normal", text=btnTwo, cursor="hand2", command=lambda: cmdTwo(controller))

#region Random Events

    def eventRandom(self, lowerBound, upperBound, ammoQuant, size):
        """Randomly chooses a good or bad event"""
        num = random.randint(1,3)
        if num == 1:
            self.eventGood(lowerBound, upperBound, ammoQuant)
        elif num == 2:
            self.eventBad(size)
        else:
            self.after(1000, lambda: self.updateText("\n\nYou don't find anything of value in there."))

    def eventGood(self, lowerBound, upperBound, ammoQuant):
        """Chooses a random good event"""
        eventType = random.randint(1,3)
        if eventType == 1:
            self.eventGold(lowerBound, upperBound)
        elif eventType == 2:
            self.eventPotion()
        else:
            self.eventAmmo(ammoQuant)

    def eventGold(self, lowerBound, upperBound):
        multiplier = 10
        ranNum1 = random.randint(1,50)
        ranNum2 = random.randint(1,50)
        goldAmt = random.randint(lowerBound, upperBound)
        if ranNum1 != ranNum2:
            Bag.gold += goldAmt
            GameInfo.goldEarned+=goldAmt
            self.after(1000, lambda: self.updateText("\n\nYou found "+str(goldAmt)+" gold!"))
        else:
            multiplierGold = goldAmt*multiplier
            Bag.gold += multiplierGold
            GameInfo.goldEarned+=multiplierGold
            self.after(1000, lambda: self.updateText("\n\nYou found a stash of gold! You're now "+str(multiplierGold)+" gold richer!"))
        self.after(1500, self.updateInfo)
        
    def eventPotion(self):
        potionType = random.randint(1,2)
        if potionType == 1:
            Bag.healthPotion += 1
            self.after(1000, lambda: self.updateText("\n\nYou found a health potion!"))
        else:
            Bag.staminaPotion += 1
            self.after(1000, lambda: self.updateText("\n\nYou found a stamina potion!"))
        self.after(1500, self.updateInfo)
    
    def eventAmmo(self, ammoQuant):
        """Random amount of ammo. ammoQuant is either 'small', 'medium', or 'large'"""
        ammoType = random.randint(1,20)
        ammoAmt = 1
        if ammoQuant == "medium":
            ammoAmt = 3
        elif ammoQuant == "large":
            ammoAmt = 5
        if 1 <= ammoType < 8:
            ranArrows = random.randint(1,3)
            arrowAmt = ranArrows*ammoAmt
            Bag.arrows += arrowAmt
            self.after(1000, lambda: self.updateText("\n\nYou found "+str(arrowAmt)+" arrows!"))
        elif 8 <= ammoType < 14:
            ranSCal = random.randint(1,10)
            sCalAmt = ranSCal*ammoAmt
            Bag.scaliber += sCalAmt
            self.after(1000, lambda: self.updateText("\n\nYou found "+str(sCalAmt)+"  9mm rounds!"))
        elif 14 <= ammoType < 19:
            ranMCal = random.randint(1,20)
            mCalAmt = ranMCal*ammoAmt
            Bag.lcaliber += mCalAmt
            self.after(1000, lambda: self.updateText("\n\nYou found "+str(mCalAmt)+"  7.62mm rounds!"))
        else:
            if ammoAmt == 1:
                Bag.grenades +=1
                self.after(1000, lambda: self.updateText("\n\nYou found a grenade!"))
            else:
                Bag.grenades +=ammoAmt
                self.after(1000, lambda: self.updateText("\n\nYou found "+str(ammoAmt)+" grenades!"))
        
    def eventGoblin(self):
        """A goblin steals a random amount of gold from the player"""
        theftNum = random.randint(25, 100) #How much the goblin could steal
        if 0 < Bag.gold < theftNum: #If goblin tries to steal more gold than the player has, this makes it so that the goblin steals the players exact amount of gold
            theftNum = Bag.gold
            Bag.gold -= theftNum
            self.after(1000, lambda: self.updateText("\n\nA goblin stole all of your gold!"))
        elif Bag.gold == 0: #If player has no gold, the goblin cant steal anything
            self.after(1000, lambda: self.updateText("\n\nA goblin tried to steal your gold, but you didnt have any for it to take."))
        else:
            Bag.gold -= theftNum
            self.after(1000, lambda: self.updateText(f"\n\nA goblin stole {str(theftNum)} gold from you!"))
        self.after(1500, self.updateInfo)

    def eventDamage(self, size):
        """Randomly chooses an animal (within specified size) to deal damage to the player"""
        damageAmt = random.randint(1, 12)
        Player.health -= damageAmt
        GameInfo.damTaken+=damageAmt
        if size == "small":
            list = ["spider", "snake", "mutant rat"]
            animalNum = random.randint(0,len(list)-1)
            if Player.health <= 0: #Added incase the small amount of damage kills the player
                Player.health = 0
                self.after(1000, lambda: self.updateText(f"\n\nA {list[animalNum]} bites you for {str(damageAmt)} damage!"))
                print("\n\nYou have no health remaining. This small yet fierece animal put an end to your journey. No one will sing songs about you.")
                print("Game over")
            else:
                self.after(1000, lambda: self.updateText(f"\n\nA {list[animalNum]} bit you for {str(damageAmt)} damage!")) #Says what hurt them and for how much damage
        else:
            list = ["racoon bites you and runs off", "rabid cat scratches you", "debris falls ontop of you"]
            sec_num = random.randint(0, len(list)-1)
            if Player.health <= 0:
                Player.health =0
                self.after(1000, lambda: self.updateText(f"\n\nA {list[sec_num]}, causing {str(damageAmt)} damage!\n"))
                print("\n\nYou have no health remaining...This is the worst way ones journey could end. You dishonor your family.\n")
                print("Game over")
            else:
                self.after(1000, lambda: self.updateText(f"\n\nA {list[sec_num]}, causing {str(damageAmt)} damage!"))
        self.after(1500, self.updateInfo)

    def eventBad(self, size): #Size is added in because if a player opens a small box, a big animal shouldn't be there
        """Randomly chooses a bad event"""
        num = random.randint(1,2)
        if num == 1:
            self.eventDamage(size)
        elif num == 2 and size != "small":
            self.eventGoblin()
        elif num == 2 and size == "small":
            self.eventDamage(size)

#endregion

#region Stage one

    def one1(self, controller):
        self.snapBottom()
        self.after(3000, lambda: self.updateText("\nYou wake up, laying face down in the dirt."))
        self.after(7000, lambda: self.updateText("\n\nFinding your footing, you see your flipped truck nearby, still radiating heat."))
        self.after(13000, lambda: self.updateText("\n\nThere are two mangled bodies inside."))
        self.after(18000, lambda: self.updateText("\n\nThe last member of your team is impaled on a tree a few feet from the crash."))
        self.after(25000, self.clearBox)
        self.after(26000, lambda: self.updateText("\nUnsure of your whereabouts, you hear something rustling in the brush."))
        self.after(32000, lambda: self.updateText("\n\nCautiously making your way over, you see a goose pecking at your bag."))
        self.after(38000, lambda: self.updateText("\n\nWithin seconds, the goose sees you, flaring out its wings."))
        self.after(43000, lambda: self.updateText("\n\nLooking around quickly, you pick up a stick to defend yourself."))
        playerWeapons[0] = weapons_list[0]
        self.after(49000, lambda: controller.showFrame(FightPage))
        self.after(49001,lambda: controller.frames[FightPage].enemyBattle(1,2,"Goose", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.one2
        self.after(50000, self.clearBox)

    def one2(self, controller):
        self.after(3000, lambda: self.updateText("\nYou toss the dead goose aside and look through the bag."))
        self.after(7000, lambda: self.updateText("\n\nMost of your supplies is missing."))
        self.after(10000, lambda: self.updateText("\n\nYou'll need to re-stock quickly if you want to survive."))
        self.after(15000, lambda: self.updateText("\n\nYou gather the remaining supplies scattered around your bag:"))
        self.after(21000, lambda: self.updateText("\n\nA few potions, a pouch of gold, a bow and arrows, along with a single grenade."))
        Bag.gold +=120
        Bag.healthPotion +=2
        Bag.staminaPotion +=1
        Bag.arrows +=6
        Bag.grenades +=1
        playerWeapons[4] = weapons_list[21]
        playerWeapons[1] = weapons_list[8]
        self.after(22000, self.updateInfo)
        self.after(28000, lambda: self.updateText("\n\nIt's not much, but it will have to do for now."))
        self.after(34000, lambda: self.updateText("\n\nYou head back to the main road and begin your journey."))
        self.after(38000, self.clearBox)
        self.after(39000, lambda: self.updateText("\n\n*A few miles later*"))
        self.after(41000, lambda: self.updateText("\n\nYou spot a carriage abandoned on the road ahead."))
        self.after(46000, lambda: self.updateText("\n\nAs you get closer, a man shouts from inside the carriage."))
        if Player.sex == "man":
            self.after(51000, lambda: self.updateText("\n\nMan: \"Hey Mister, could you please get this thing away from me!?\""))
        else:
            self.after(51000, lambda: self.updateText("\n\nMan: \"Hey Miss, could you please get this thing away from me!?\""))
        self.after(56000, lambda: self.updateText("\n\nA creature slowly crawls out from under the carriage."))
        self.after(60000,lambda: controller.frames[FightPage].enemyBattle(1,2,"Arthropleura", 0))
        self.after(61000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.one3
        self.after(62000, self.clearBox)

    def one3(self, controller):
        self.after(3000, lambda: self.updateText("\nThe man gets out of the carriage, looking at the pile of goo."))
        self.after(8000, lambda: self.updateText("\n\nMan: \"Thank you for the assistance! I'm far too old to be fighting these things.\""))
        self.after(15000, lambda: self.updateText("\n\nMan: \"You on the other hand look like a "+Player.sex+" who can take care of themselves.\""))
        self.after(22000, lambda: self.updateText("\n\nMan: \"Still, an out-of-towner like yourself could end up being food if you're not too careful.\""))
        self.after(29000, lambda: self.updateText("\n\nMan: \"A bit of advice, the only way to survive these lands is to stay stocked up on gear.\""))
        self.after(36000, lambda: self.updateText("\n\nMan: \"Be mindful of your ammunition and health before getting into any fights.\""))
        self.after(42000, self.clearBox)
        self.after(43000, lambda: self.updateText("\n\nMan: \"You know what, I was headed to the next town to sell supplies, but I can give you a quick look right now.\""))
        self.after(51000, lambda: self.updateText("\n\nMan: \"And remember, you can never have too many potions on hand!\""))
        self.after(56000, self.clearBox)
        self.after(56000, lambda: controller.showFrame(ShopPage))
        GameInfo.nextFunction = self.one4

    def one4(self, controller):
        self.after(3000, lambda: self.updateText("\nMan: \"Well, I hope that holds you over for now.\""))
        self.after(6000, lambda: self.updateText("\n\nMan: \"Anyways, that damned creature spooked my horses when it attacked. I should go look for them.\""))
        self.after(12000, lambda: self.updateText("\n\nMan: \"Safe journeys friend, and feel free to stop by my shop when you're in town!\""))
        self.after(17000, self.clearBox)
        self.after(18000, lambda: self.updateText("\n\nAs you continue down the road, the midday sun amplifies the smell of rotting flesh."))
        self.after(23000, lambda: self.updateText("\n\nHearing a low growling just off the road, you cautiously head toward the noise."))
        self.after(29000, lambda: self.updateText("\n\nFollowing a beaten down path, you discover a rundown campsite."))
        self.after(35000, lambda: self.updateText("\n\nThere lies a man half dragged out of his tent, with both legs chewed to the bone."))
        self.after(41000, lambda: self.updateText("\n\nA rabid dog is inside, starting to chew away at the mans arms, unbothered by your presence."))
        self.after(48000, lambda: self.updateText("\n\nLooking more closely, you notice an ammo case in the back of the tent."))
        self.after(53000, lambda: self.newChoice(controller, "Yes", "No", "Do you fight the dog?", self.one4StrayDog, self.one4Exit))

    def one4StrayDog(self, controller):
        self.btnDisbaled()
        self.after(500,lambda: controller.frames[FightPage].enemyBattle(1,3,"Stray Dog", 0))
        self.after(1000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.one4StrayDogEnd
        self.after(3000, self.clearBox)

    def one4StrayDogEnd(self, controller):
        self.after(3000, lambda: self.updateText("\nAfter cleaning the blood off yourself, you take a look inside the ammo case."))
        self.after(10000, lambda: self.eventAmmo("medium"))
        self.after(15000, lambda: self.updateText("\n\nYou don't see anything else of value around the campsite, and head back to the road."))
        self.after(22000, self.clearBox)
        self.after(22100, lambda: self.one5(controller))
        
    def one4Exit(self, controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\n\nYou leave the campsite and head back to the road."))
        self.after(9000, self.clearBox)
        self.after(9100, lambda: self.one5(controller))

    def one5(self, controller):
        self.after(3000, lambda: self.updateText("\nAfter a few hours of walking, you notice alot of movement up ahead."))
        self.after(9000, lambda: self.updateText("\n\nGetting closer, you can make out a pack of coyotes eating something on the road."))
        self.after(16000, lambda: self.updateText("\n\nThere's no way you can fight them. You'll have to go around."))
        self.after(21000, lambda: self.updateText("\n\nA path is close by that interescts the road."))
        self.after(26000, lambda: self.updateText("\n\nOn your left, you can take the path into the woods, or go right towards the river."))
        self.after(33000, lambda: self.newChoice(controller, "Woods", "River", "Which route\ndo you take?", self.oneForest1, self.oneRiver1))

#region Forest

    def oneForest1(self, controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\nYou leave the road and start following the path into the woods."))
        self.after(10000, lambda: self.updateText("\n\nAbout a kilometer in, you come across an old cabin."))
        self.after(15000, lambda: self.updateText("\n\nThe landscape is severly overgrown, yet the cabin looks intact."))
        self.after(20000, lambda: self.updateText("\n\nA rain collector sits adjacent to the cabin, filled to the brim."))
        self.after(26000, lambda: self.updateText("\n\nOther than a small shed, there isn't much else on the property."))
        self.after(32000, lambda: self.updateText("\n\nIt's completley silent, except the creeking of surrounding trees."))
        self.after(38000, lambda: self.newChoice(controller, "Yes", "No", "Do you enter the cabin?", self.oneForestEnterCabin, self.oneForestGoToShed))

    def oneForestEnterCabin(self, controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou gently push the door open, coughing as the musty smell hits."))
        self.after(10000, lambda: self.updateText("\n\nThe furniture looks well taken care of, but covered in light dust."))
        self.after(16000, lambda: self.updateText("\n\nThe kitchen table has a single bowl on it, with some kind of moldy food still inside."))
        self.after(23000, lambda: self.updateText("\n\nYou pack up some food stored in the pantry, and head to the cabinet."))
        self.after(30000, lambda: self.newChoice(controller, "Yes", "No", "Do you open the cabinet?", self.oneForestCabinCabinet, self.oneForestCabinGoToSpareRoom))

    def oneForestCabinCabinet(self, controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou open up the cabinet:"))
        self.after(6000, lambda: self.eventGood(5, 30, "medium"))
        self.after(13000, lambda: self.oneForestCabinGoToSpareRoom(controller))

    def oneForestCabinGoToSpareRoom(self, controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\n\nNext, you make your way to the corner bedroom."))
        self.after(10000, lambda: self.newChoice(controller, "Yes", "No", "Do you open the door?", self.oneForestCabinSpareRoom, self.oneForestCabinGoToMainRoom))

    def oneForestCabinSpareRoom(self, controller):
        self.btnDisbaled()
        self.after(1000, lambda: self.eventBad("large"))
        self.after(3000, self.updateInfo)
        self.after(8000, lambda: self.updateText("\n\nIt's just a small bathroom. The medicine cabinet is open, with a few empty pill bottles."))
        self.after(15000, lambda: self.oneForestCabinGoToMainRoom(controller))
    
    def oneForestCabinGoToMainRoom(self, controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nThere's one room left to check. A large hole is chewed out from the bottom of the door."))
        self.after(10000, lambda: self.updateText("\n\nThe door seems to be jammed. You'll need to kick it open."))
        self.after(10000, lambda: self.newChoice(controller, "Yes", "No", "Do you kick the door open?", self.oneForestCabinMainRoom1, self.oneForestCabinExitCabin))

    def oneForestCabinMainRoom1(self, controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou take a couple steps back and kick the door open, tearing it away from one of the hinges."))
        self.after(10000, lambda: self.updateText("\n\n An small animal charges you."))
        self.after(15000, lambda: controller.showFrame(FightPage))
        self.after(15001,lambda: controller.frames[FightPage].enemyBattle(1,3,"Tasmanian devil", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.oneForestCabinMainRoom2
        self.after(16000, self.clearBox)

    def oneForestCabinMainRoom2(self, controller):
        self.after(3000, lambda: self.updateText("\nThe bedroom is quite small, yet very organized and neat."))
        self.after(10000, lambda: self.updateText("\n\nYou find a health potion in the dresser, and a granola bar beside it."))
        Bag.healthPotion+=1
        self.after(15000, self.updateInfo)
        self.after(15000, lambda: self.updateText("\n\nOn top of the right bedside table you find a note."))
        self.after(21000, self.clearBox)
        self.after(22000, lambda: self.updateText("\nDear Matthew,\n\n\tI'm sorry to end it this way. The area is getting too dangerous and I cant stay here\n\tany longer.\n\n\tJohn is taking me south where it's safer...He's well equipt, and will take good care\n\tof me.\n\n\tYou'll always be my first love. I hope you can find peace without me.\n\n\t\tLove, Annie"))
        self.after(40000, self.clearBox)
        self.after(41000, lambda: self.updateText("\nYou set the note back down leave the room."))
        self.after(46000, lambda: self.oneForestCabinExitCabin(controller))
        
    def oneForestCabinExitCabin(self, controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\n\nYou make your way out of the cabin."))
        self.after(8000, lambda: self.oneForestGoToShed(controller))

    def oneForestGoToShed(self, controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\n\nAs you start to walk toward the shed, a wretched odour fills your nose."))
        self.after(10000, lambda: self.newChoice(controller, "Yes", "No", "Do you enter the shed?", self.oneForestShed1, self.oneForestLeaveCabinProperty))
        
    def oneForestShed1(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou open the shed door to reveal a man hanging from the ceiling."))
        self.after(9000, lambda: self.updateText("\n\nThe shed is filled with old gardening equipment. You move past the body to the workbench."))
        self.after(16000, lambda: self.updateText("\n\nThere is a small chest sitting on top."))
        self.after(22000, lambda: self.newChoice(controller, "Yes", "No", "Do you open the chest?", self.oneForestShed2, self.oneForestLeaveCabinProperty))
    
    def oneForestShed2(self, controller):
        self.btnDisbaled()
        self.after(1000, lambda: self.eventGold(50, 100))
        self.after(5000, lambda: self.oneForestLeaveCabinProperty(controller))

    def oneForestLeaveCabinProperty(self, controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\nYou leave the property and continue down the trail."))
        self.after(10000, lambda: self.updateText("\n\nOnly a few minutes later, you hear a whirring sound, rapidly growing louder."))
        self.after(17000, lambda: self.updateText("\n\nYou look up to see a helicopteer spinning out of control, passing over you."))
        self.after(24000, lambda: self.updateText("\n\nIt looks like one of yours, but this area's a no-fly zone."))
        self.after(31000, lambda: self.updateText("\n\nThings must be getting really bad if they'd take that risk again."))
        self.after(37000, lambda: self.updateText("\n\nThere's a thick smoke trail leading to the crash."))
        self.after(41000, lambda: self.newChoice(controller, "Yes", "No", "Do you follow the smoke?", self.oneForestGoToCrash, self.oneForestSkipCrash))

    def oneForestGoToCrash(self, controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\nYou managed to get to the crash site after about 10 minutes"))
        self.after(9000, lambda: self.updateText("\nThe surrounding area is littered with debris and small fires."))
        self.after(15000, lambda: self.updateText("\nLucky enough, the helicopter is mostly intact."))
        self.after(20000, lambda: self.updateText("\nOne of the pilots is hanging through the front window, the other dead in his seat."))
        self.after(26000, lambda: self.updateText("\nFuel is pouring out of the fuselage. The whole thing will catch fire soon."))
        self.after(33000, lambda: self.updateText("\nQuickly working on the side door, you managed to get it open a few feet."))
        self.after(39000, lambda: self.updateText("\nImmediately, a Buzzdroid crawls out towards you."))
        self.after(44000, lambda: controller.showFrame(FightPage))
        self.after(44001,lambda: controller.frames[FightPage].enemyBattle(1,3,"Dimorphodon", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.oneForestInsideHeli
        self.after(45000, self.clearBox)

    def oneForestInsideHeli(self, controller):
        self.after(3000, lambda: self.updateText("\nSqueezing through the door, you see alot of broken gear thrown about."))
        self.after(10000, lambda: self.updateText("\n\nTheres a couple small crates still intact, but you can only carry one out."))
        self.after(41000, lambda: self.newChoice(controller, "Ammo", "Potion", "Which crate do you take?", self.oneForestAmmoHeli, self.oneForestPotionHeli))

    def oneForestAmmoHeli(self, controller):
        self.after(3000, lambda: self.updateText("\n\nYou grab the ammo crate and leave just before the Helicopter catches fire."))
        GameInfo.choice = "ammo"
        self.after(10000, lambda: self.updateText("\n\nAfter getting to a safe area, you open the crate and find 200 7.62mm rounds."))
        Bag.lcaliber +=200
        self.after(16000, lambda: self.oneForestLeaveHeli(controller))


    def oneForestPotionHeli(self, controller):
        self.after(3000, lambda: self.updateText("\n\nYou grab the potion crate and leave just before the Helicopter catches fire."))
        GameInfo.choice = "potion"
        self.after(10000, lambda: self.updateText("\n\nAfter getting to a safe area, you open the crate and find 4 health and 2 stamina potions."))
        Bag.healthPotion +=4
        Bag.staminaPotion +=2
        self.after(11000, self.updateInfo)
        self.after(16000, lambda: self.oneForestLeaveHeli(controller))

    def oneForestLeaveHeli(self, controller):
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nOn your way back to the trail, a man approaches with his gun drawn."))
        self.after(8000, lambda: self.updateText("\n\nThug: \"Whatever you took from there, drop it, and I'll let you go.\""))
        self.after(15000, lambda: self.newChoice(controller, "Yes", "No", "Do you give him the "+GameInfo.choice+" you found?", self.oneForestFightThug, self.oneForestGiveCrate))

    def oneForestFightThug(self, controller):
        self.after(3000, lambda: self.updateText("\n\nThug: \"You gonna learn today...\""))
        self.after(8000, lambda: controller.showFrame(FightPage))
        self.after(8001,lambda: controller.frames[FightPage].enemyBattle(1,2,"Thug", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.oneForestLeaveForest
        self.after(9000, self.clearBox)

    def oneForestGiveCrate(self, controller):
        self.after(3000, lambda: self.updateText("\n\nThug: \"That's what I thought. And this is what you get for being a lil' bitch..\""))
        self.after(10000, lambda: self.updateText("\n\nThe thug punches you in the face, knocking you to the ground."))
        if GameInfo.choice == "ammo":
            self.after(16000, lambda: self.updateText("\n\nHe takes 200 7.62mm off your pathetic body."))
            Bag.lcaliber -= 200
        elif GameInfo.choice == "potion":
            self.after(16000, lambda: self.updateText("\n\nHe takes 4 health and 2 stamina potions off your pathetic body."))
            Bag.healthPotion -=4
            Bag.staminaPotion -=2
        self.after(16100, lambda: self.updateInfo)
        self.after(23000, lambda: self.oneForestLeaveForest(controller))

    def oneForestLeaveForest(self, controller):
        self.after(3000, lambda: self.updateText("\n\nYou find your back to the trail, continuing your hike back to the main road."))
        self.after(10000, lambda: self.updateText("\n\nAfter an hour, you see the road up ahead. You suddenly hear a noise behind you and quickly turn around."))
        self.after(17000, lambda: controller.showFrame(FightPage))
        self.after(17001,lambda: controller.frames[FightPage].enemyBattle(1,2,"random", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.one6
        self.after(18000, self.clearBox)
    
    def oneForestSkipCrash(self, controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\nContinuing along the trail, you come across a large sea container. Something is inside..."))
        self.after(11000, lambda: controller.showFrame(FightPage))
        self.after(11001,lambda: controller.frames[FightPage].enemyBattle(1,2,"random", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.oneForestSeaCan
        self.after(12000, self.clearBox)

    def oneForestSeaCan(self, controller):
        self.after(3000, lambda: self.updateText("\nIt looks like someone used to live in this container."))
        self.after(9000, lambda: self.updateText("\n\nThere's some ragged clothes left about, empty food cans, and a dirty sleeping bag."))
        self.after(16000, lambda: self.updateText("\n\nThis would be a good place to rest, but you dont want to be stuck out here at night."))
        self.after(23000, lambda: self.updateText("\n\nYou leave the container and get back on the trail."))
        self.after(28000, self.clearBox)
        self.after(29000, lambda: self.updateText("\nAfter an hour, you see the road up ahead. You suddenly hear a noise from behind."))
        self.after(36000, lambda: controller.showFrame(FightPage))
        self.after(36001,lambda: controller.frames[FightPage].enemyBattle(1,2,"random", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.one6
        self.after(37000, self.clearBox)

#endregion

#region River

    def oneRiver1(self, controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\nYou make your way along a small path to the river."))
        self.after(9000, lambda: self.updateText("\n\nThere's a parked camper and some containers scattered around."))
        self.after(15000, lambda: self.newChoice(controller, "Yes", "No", "Do you search\nthe containers?", self.oneRiverContainer, self.oneRiverAfterContainer))

    def oneRiverContainer(self, controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.eventRandom(10, 50, "small", "small"))
        self.after(9000, lambda: self.oneRiverAfterContainer(controller))
        
    def oneRiverAfterContainer(self, controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\n\nThe camper looks to be in good shape."))
        self.after(7000, lambda: self.newChoice(controller, "Yes", "No", "Do you enter\nthe camper?", self.oneRiverEnterRV, self.oneRiverAfterRV))

    def oneRiverEnterRV(self, controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.eventRandom(30, 80, "medium", "large"))
        self.after(9000, lambda: self.oneRiverAfterRV(controller))

    def oneRiverAfterRV(self, controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nAround back of the camper, you find a flipped over canoe."))
        self.after(9000, lambda: self.updateText("\n\nThe green paint has been scratched up, but the rest is in good shape."))
        self.after(17000, lambda: self.updateText("\n\nYou pick up an oar and drag the canoe into the water."))
        self.after(23000, lambda: self.updateText("\n\nTravelling downstream, you hear 5 distant gun shots, too far to care about though."))
        self.after(31000, lambda: self.updateText("\n\nThere's quite a bit of debris washed up on the riverbank, along with the bodies of animals."))
        self.after(40000, lambda: self.updateText("\n\nYou decide to lay back and get some rest."))
        self.after(47000, lambda: self.oneRiverWakeUp(controller))

    def oneRiverWakeUp(self, controller):
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nA repetitive banging noise wakes you up."))
        self.after(9000, lambda: self.updateText("\n\nYou sit up to see your canoe washed up on the bank, hitting off another boat."))
        self.after(16000, lambda: self.updateText("\n\nThe boat looks familiar. A previous team left with it few weeks ago..."))
        self.after(24000, lambda: self.updateText("\n\nThere's a fishing shack close by, maybe that holds some clues about the teams whereabouts."))
        self.after(30000, lambda: self.updateText("\n\nYou approach the front door of the shack."))
        self.after(36000, lambda: self.newChoice(controller, "Yes", "No", "Do you explore the\nfishing shack?", self.oneRiverEnterShack, self.oneRiverLeaveShack))

    def oneRiverEnterShack(self, controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nAs you open the door, you see a small figure scurry across the floor."))
        self.after(10000, lambda: self.updateText("\n\nThe dark room makes it hard to see the creature..."))
        self.after(16000, lambda: self.updateText("\n\nAs you step closer, it scampers to the back corner of the room."))
        self.after(23000, lambda: self.updateText("\n\nYour eyes begin to adjust. You see a small child, in ragged clothes."))
        self.after(29000, lambda: self.updateText("\n\nIt's standing over a floor hatch, almost as if it's guarding it."))
        self.after(36000, lambda: self.newChoice(controller, "Fight", "Leave", "What do you do?", self.oneRiverFightChild, self.oneRiverLeaveChild))

    def oneRiverLeaveChild(self, controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou slowly back away and exit through the front door."))
        self.after(10000, lambda: self.newChoice(controller, "Yes", "No", "Do you explore\nthe back of the\nproperty?", self.oneRiverBackYard, self.oneRiverLeaveShack))

    def oneRiverFightChild(self, controller):
        self.btnDisbaled()
        self.after(1000, lambda: controller.showFrame(FightPage))
        self.after(1001,lambda: controller.frames[FightPage].enemyBattle(1,2,"Orphaned Child", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.oneRiverEnterBasement
        self.after(3000, self.clearBox)

    def oneRiverEnterBasement(self, controller):
        self.after(3000, lambda: self.updateText("\nYou drag the childs body away from the floor hatch."))
        self.after(9000, lambda: self.updateText("\n\nThere is ladder to get down."))
        self.after(17000, lambda: self.updateText("\n\nOnce you get into the cellar, you see a dining table in the center of the room."))
        self.after(25000, lambda: self.updateText("\n\nThere are several chairs around it, three of which have rotting corpses seated in them."))
        self.after(33000, lambda: self.updateText("\n\nThe candles have done well with masking the smell."))
        self.after(40000, lambda: self.updateText("\n\nThe clothes on the bodies look clean, as if they were put on after their deaths..."))
        self.after(48000, self.clearBox)
        self.after(49000, lambda: self.updateText("\nThe table is set with a mix of plastic and moldy food."))
        self.after(54000, lambda: self.updateText("\n\nThe bodies all have pins stuck into their chests."))
        self.after(62000, lambda: self.updateText("\n\nThey read \"Best Dad\", \"Best Mom\", and \"Best Brother\"."))
        self.after(68000, lambda: self.updateText("\n\nIt could be that childs family, but you see black tactical gear piled in the corner."))
        self.after(76000, lambda: self.updateText("\n\nThat must be the team from the boat..."))
        self.after(82000, lambda: self.updateText("\n\nThankfully, there's still useful gear scattered around the room."))
        self.after(90000, lambda: self.updateText("\n\nYou grab a couple health potions, a few arrows, and a pouch of gold."))
        Bag.healthPotion+=2
        Bag.arrows +=4
        Bag.gold +=74
        self.after(92000, self.updateInfo)
        self.after(98000, self.clearBox)
        self.after(105000, lambda: self.updateText("\nYou head back up to the main floor."))
        self.after(110000, lambda: self.newChoice(controller, "Yes", "No", "Do you explore\nthe back of the\nproperty?", self.oneRiverBackYard, self.oneRiverLeaveShack))

    def oneRiverBackYard(self, controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\n\nYou walk to the back of the property and start looking around."))
        self.after(10000, lambda: self.updateText("\n\nOn your way towards the river, light reflects off of something in the mud."))
        self.after(17000, lambda: self.updateText("\n\nAs you get closer a giant crab emerges from the ground."))
        self.after(23000, lambda: controller.showFrame(FightPage))
        self.after(23001,lambda: controller.frames[FightPage].enemyBattle(1,2,"Mudcrab", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.oneRiverLeaveBackYard
        self.after(24000, self.clearBox)

    def oneRiverLeaveBackYard(self, controller):
        self.after(3000, lambda: self.updateText("\nYou bag up some crab meat before checking your map."))
        self.after(9000, lambda: self.updateText("\n\nThe main road should be close. You might be able to get there before nightfall."))
        self.after(17000, lambda: self.one6(controller))

    def oneRiverLeaveShack(self, controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\n\nYou leave the shack and continue towards the main road on foot."))
        self.after(9000, lambda: self.updateText("\n\nIt's getting dark, but you should be able to make it there before nightfall."))
        self.after(17000, lambda: self.one6(controller))

#endregion

    def one6(self, controller):
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou finally get back to the road, just as the sun sets."))
        self.after(9000, lambda: self.updateText("\n\nThe town isn't much further, you'll rest once you get there."))
        self.after(16000, lambda: self.updateText("\n\nA few minutes later, you see distant lights on the road ahead."))
        self.after(22000, lambda: self.updateText("\n\nYou soon realize it's a group of men. You get off the road and wait for them to pass."))
        self.after(30000, self.clearBox)
        self.after(31000, lambda: self.updateText("\nMan 1: \"The cabin is a couple hours from here, we'll sleep once we get there.\""))
        self.after(39000, lambda: self.updateText("\n\nMan 2: \"It's late, I'm sure we'll be fine to hold up here for the night.\""))
        self.after(45000, lambda: self.updateText("\n\nMan 1: \"If getting your limbs chewed off by boars is considered fine, then yes, we'll be fine....\""))
        self.after(53000, lambda: self.updateText("\n\nMan 3: \"I wouldn't worry about that. I'm sure they're well fed with all the soldiers getting sent up here.\""))
        self.after(61000, lambda: self.updateText("\n\nMan 2: \"And the Republic will keep sending more. Anything to get what they want.\""))
        self.after(67000, lambda: self.updateText("\n\nMan 3: \"What's in that facility will get society back on track though.\""))
        self.after(75000, lambda: self.updateText("\n\nMan 1: \"No, it will just give the Republic more power. People like us will still have to fight to survive.\""))
        self.after(83000, self.clearBox)
        self.after(85000, lambda: self.updateText("\nThe men are too far away to listen any longer."))
        self.after(89000, lambda: self.updateText("\n\nYou start to think about what the men were saying, but they dont know how bad it is in the city."))
        self.after(97000, lambda: self.updateText("\n\nFood is running out. People are starved on the streets."))
        self.after(103000, lambda: self.updateText("\n\nThat's why they've sent so many soldiers here recently, including yourself."))
        self.after(109000, lambda: self.updateText("\n\nYour thoughts get interupted by something..."))
        self.after(117000, lambda: controller.showFrame(FightPage))
        self.after(117001,lambda: controller.frames[FightPage].enemyBattle(1,2,"random", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.one7
        self.after(118000, self.clearBox)

    def one7(self, controller):
        self.after(3000, lambda: self.updateText("\nYou finally see the town ahead."))
        self.after(8000, lambda: self.updateText("\n\nAs you get close, a man opens the gate for you."))
        if Player.sex == "man":
            self.after(14000, lambda: self.updateText("\n\nGatekeeper: \"Hello there mister... You look to be in rough shape.\""))
        else: 
            self.after(14000, lambda: self.updateText("\n\nGatekeeper: \"Hello there miss... You look to be in rough shape.\""))

        self.after(21000, lambda: self.updateText("\n\nGatekeeper: \"You better come on in and get situated. There's lots to do in here!\""))
        self.after(29000, self.clearBox)
        GameInfo.location == "town"
        self.after(29000, lambda: controller.showFrame(TownPage))
        GameInfo.nextFunction = self.two1

#endregion

#region Stage two
    def two1(self, controller):
        GameInfo.location == "road"
        self.after(3000, lambda: self.updateText("\nYou leave the town at dawn, continuing north."))
        self.after(9000, lambda: self.updateText("\n\nThe road is quite clear, with dense forest on either side."))
        self.after(15000, lambda: self.updateText("\n\nHowever, there's still garbage littered about, among a mix of animal and human bodies."))
        self.after(21000, lambda: self.updateText("\n\nEventually you come across a man seated beside the road."))
        if Player.sex == "man":
            self.after(28000, lambda: self.updateText("\n\nHomeless Man: \"Hey brotha, you able to help me out?\""))
        else:
            self.after(28000, lambda: self.updateText("\n\nHomeless Man: \"Hey shawty, you able to help me out?\""))
        self.after(34000, lambda: self.updateText("\n\nThe man sticks out his hand, waiting for something."))
        self.after(39000, lambda: self.newChoice(controller, "Give a granola bar", "Spit on him", "What do you do?", self.twoBeggerYes, self.twoBeggerNo))

    def twoBeggerYes(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\nThe man slaps the granola bar out of your hand."))
        self.after(8000, lambda: self.updateText("\n\nHomeless Man: \"Aye I don't want that shit, give me some gold.\""))
        self.after(14000, lambda: self.newChoice(controller, "Give 50 Gold", "Tell him to get a job", "What do you do?", self.twoBeggerGold, self.twoBeggerJob))

    def twoBeggerNo(self,controller):
        self.btnDisbaled()
        self.after(3000, lambda: controller.showFrame(FightPage))
        self.after(3001,lambda: controller.frames[FightPage].enemyBattle(1,2,"Homeless Man", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.two2

    def twoBeggerGold(self, controller):
        self.btnDisbaled()
        if Bag.gold >= 50:
            self.after(3000, lambda: self.updateText("\n\nYou give the man 50 gold and carry on your way."))
            Bag.gold-=50
            self.after(3500, self.updateInfo)
            self.after(9000, lambda: self.two2(controller))

        else:
            self.after(3000, lambda: self.updateText("\n\nKnowing you don't have the gold, you pretend to check your pockets."))
            self.after(10000, lambda: self.updateText("\n\nThe man gets inpatient and takes a swing at you."))
            self.after(15000, lambda: controller.showFrame(FightPage))
            self.after(15001,lambda: controller.frames[FightPage].enemyBattle(1,2,"Homeless Man", 0))
            controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.two2

    def twoBeggerJob(self,controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\n\nThe man gets visibly angry."))
        self.after(9000, lambda: self.updateText("\n\nHomeless Man: \"Shit's hard out here ya know. Ain't nobody wanna give me a chance!\""))
        self.after(17000, lambda: self.updateText("\n\nHomeless Man: \"...Fuck you anyways. You gone be dead soon enough.\""))
        self.after(23000, lambda: self.updateText("\n\nThe man gets up and hobbles away."))
        self.after(31000, lambda: self.two2(controller))

    def two2(self, controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nAs you continue down the road, you come across an old gas station."))
        self.after(9000, lambda: self.updateText("\n\nYou hesistate about entering due to how clean it looks."))
        self.after(15000, lambda: self.updateText("\n\nYou're a few meters from the door when a woman speaks."))
        self.after(21000, self.clearBox)
        self.after(22000, lambda: self.updateText("\nWoman: \"Stop right there.\""))
        self.after(27000, lambda: self.updateText("\n\nYou look up to see a woman on the roof, before noticing some men inside the gas station."))
        self.after(35000, lambda: self.updateText("\n\nWoman: \"I saw your nasty "+Player.color.lower()+" skin from a mile away.\""))
        self.after(42000, lambda: self.updateText("\n\nWoman: \"You people just cause problems around here. We oughta be rid of you folks for good.\""))
        self.after(50000, lambda: self.updateText("\n\nThe woman raises her gun, but pauses when she looks up."))
        self.after(57000, lambda: self.updateText("\n\nWoman: \"On second thought, it looks like we gonna be getting a free show.\""))
        self.after(64000, self.clearBox)
        self.after(65000, lambda: self.updateText("\nAfter seeing what's behind you, you look around for an escape, but there's no where to go."))
        self.after(72001,lambda: controller.frames[FightPage].enemyBattle(3,4,"Mountain Lion", 0))
        self.after(73000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.two3

    def two3(self,controller):
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou immediately run into the woods behind the gas station."))
        self.after(9000, lambda: self.updateText("\n\nThe racists take a couple shots at you while they yell slurs."))
        self.after(15000, lambda: self.updateText("\n\nYou make it away safe, and decide to travel into the woods a bit further just incase."))
        self.after(22000, lambda: self.updateText("\n\nSoon after, you come across an overgrown field."))
        self.after(26000, lambda: self.updateText("\n\nThere's a barn off in the distance."))
        self.after(30000, lambda: self.newChoice(controller, "Yes", "No", "Do you go to the barn?", self.twoBarn, self.twoLeaveFarm))

    def twoBarn(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nThe barn door is open. It looks like it used to house cattle."))
        self.after(10000, lambda: self.updateText("\n\nNear the entrance, you see an opened firearm safe."))
        self.after(16000, lambda: self.updateText("\n\nThere's nothing left inside, but you notice a footprint in the mud infront of it."))
        self.after(24000, lambda: self.updateText("\n\nSomeone must have just looted this place."))
        self.after(28000, lambda: self.updateText("\n\nSuddenly, you hear a loud banging noise."))
        self.after(33000, lambda: self.updateText("\n\nYou exit the barn and head towards the noise. It's coming from the farm house."))
        self.after(40000, lambda: self.newChoice(controller, "Yes", "No", "Do you go to the house?", self.twoFarmHouse, self.twoLeaveFarm))
        
    def twoFarmHouse(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou see a deformed human-like creature smashing on the front door."))
        self.after(9000, lambda: self.newChoice(controller, "Yes", "No", "Do you Fight?", self.twoFarmHouseFight, self.twoLeaveFarm))

    def twoFarmHouseFight(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(2000, lambda: controller.showFrame(FightPage))
        self.after(2001,lambda: controller.frames[FightPage].enemyBattle(3,4,"Falmer", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.twoEnterFarmHouse

    def twoEnterFarmHouse(self,controller):
        self.after(3000, lambda: self.updateText("\nA man slowly opens the front door, looking at the dead falmer, and then you."))
        self.after(10000, lambda: self.updateText("\n\nHe is very skinny, with mismatched gear on."))
        if Player.height >= 72:
            self.after(16000, lambda: self.updateText("\n\nMan: \"Oh wow, you're a tall "+Player.sex+"! Thanks for killing this thing.\""))
        elif 65<= Player.height<72:
            self.after(16000, lambda: self.updateText("\n\nMan: \"Oh wow, thanks for killing this thing!\""))
        else:
            self.after(16000, lambda: self.updateText("\n\nMan: \"Oh wow, you're quite short...Thanks for killing this thing though!\""))
        self.after(23000, lambda: self.updateText("\n\nThere's a small safe in here that I can't get open. If you help, I'll give you some gold."))
        self.after(30000, lambda: self.newChoice(controller, "Yes", "No", "Do you help?", self.twoHelpWithSafe, self.twoLeaveFarm))

    def twoHelpWithSafe(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou follow the man to the master bedroom."))
        self.after(9000, lambda: self.updateText("\n\nThe small safe is bolted into the wall within the walk-in closet."))
        self.after(15000, lambda: self.updateText("\n\nYou help the man pull on the pry bar that's lodged in the safe door."))
        self.after(22000, lambda: self.updateText("\n\nThe safe door comes flying open, suprisingly easy."))
        self.after(28000, lambda: self.updateText("\n\nThe man quickly blocks the view to what's inside."))
        self.after(33000, lambda: self.updateText("\n\nMan: \"Thanks alot for your help! Here's 50 gold, as promised!\""))
        Bag.gold+=50
        self.after(34000, self.updateInfo)
        self.after(39000, lambda: self.newChoice(controller, "Demand to see\nwhat's inside", "Leave the property", "What do you do?", self.twoDemandSafe, self.twoLeaveHouse))

    def twoDemandSafe(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nMan: \"That wasn't part of the deal friend... Please, I don't want any trouble.\""))
        self.after(9000, lambda: self.updateText("\n\nThe man nervously holds up the pry bar."))
        self.after(14000, lambda: self.newChoice(controller, "Attack", "Leave the property", "What do you do?", self.twoAttackSafe, self.twoLeaveHouse))
        
    def twoAttackSafe(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou lunge at the man, knocking the pry bar away and tackling him to the ground."))
        self.after(9000, lambda: self.newChoice(controller, "Gouge out his eyes", "Reach for the pry bar", "What do you do?", self.twoAttackEyes, self.twoReachPryBar))

    def twoAttackEyes(self,controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\n\nYou body weight pins the man to the ground."))
        self.after(9000, lambda: self.updateText("\n\nHe's frantically trying to push you off."))
        self.after(15000, lambda: self.updateText("\n\nYou plant your hands on either side of his face, pushing your thumbs into his eye sockets."))
        self.after(23000, lambda: self.updateText("\n\nHe starts screaming, flailing his arms around trying to hit you."))
        self.after(30000, lambda: self.updateText("\n\nYou transfer your body weight to your hands, driving your thumbs deeper, feeling inside his skull."))
        self.after(38000, lambda: self.updateText("\n\nHis cries fade and body goes limp, only to twitch a few times afterwards."))
        self.after(45000, lambda: self.twoTakeMansLoot(controller))

    def twoReachPryBar(self,controller):
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\n\nYou shift your body to the right, trying to reach for the pry bar."))
        self.after(9000, lambda: self.updateText("\n\nThe man takes the opportunity to push you off."))
        self.after(15000, lambda: self.updateText("\n\nHe then scrambles on the ground towards his bag."))
        self.after(21000, lambda: self.updateText("\n\nYou quickly stand up with the pry bar and hit it against the back of his skull."))
        self.after(29000, lambda: self.updateText("\n\nThe man slowly rolls over, with blood pooling on the floor underneath of him."))
        self.after(36000, lambda: self.updateText("\n\nMan: \"Please please! Take everything, take my bag, please don't do this.\""))
        self.after(43000, lambda: self.newChoice(controller, "Kill him", "Let him live", "What do you do?", self.twoKillPryBar, self.twoTakeMansLoot))

    def twoKillPryBar(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nYou raise the pry bar above your head and smash it into his skull several times."))
        self.after(10000, lambda: self.updateText("\n\nAfter the sixth hit, his arms fall to the side as his body twitches."))
        self.after(18000, lambda: self.twoTakeMansLoot(controller))
        
    def twoTakeMansLoot(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(3000, lambda: self.updateText("\nYou make your way over to the safe."))
        self.after(9000, lambda: self.eventGold(200, 500))
        self.after(15000, lambda: self.updateText("\n\nAfter taking the gold, you move to the mans bag and look inside."))
        self.after(22000, lambda: self.eventAmmo("large"))
        self.after(28000, lambda: self.twoLeaveHouse(controller))

    def twoLeaveHouse(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nMoving quickly, you leave the house."))
        self.after(9000, lambda: self.twoLeaveFarm(controller))

    def twoLeaveFarm(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nThe farms driveway must lead back to the main road."))
        self.after(9000, lambda: self.updateText("\n\nYou make your way towards it, being mindful of your surroundings."))
        self.after(15000, lambda: self.updateText("\n\nNot long after, a young girl, about 6 years old comes around the corner."))
        self.after(22000, lambda: self.updateText("\n\nShe freezes when she sees you."))
        self.after(26000, lambda: self.updateText("\n\nA woman appears soon after, putting herself in front of the girl."))
        self.after(32000, lambda: self.updateText("\n\nWoman: \"We dont want any trouble, just on our way back to my husband.\""))
        self.after(40000, self.clearBox)
        self.after(41000, lambda: self.updateText("\nThe woman and child walk by you, towards the farm."))
        self.after(47000, lambda: self.updateText("\n\nYou continue walking, seeing the main road once you get around the corner."))
        self.after(53000, lambda: self.updateText("\n\nThere's a creature just off the road, it must've been stocking the woman."))
        self.after(61000, lambda: controller.showFrame(FightPage))
        self.after(2001,lambda: controller.frames[FightPage].enemyBattle(3,4,"Dilophosaurus", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.two4

    def two4(self,controller):
        self.clearBox()
        self.after(3000, lambda: self.updateText("\nThe noise seemed to have attracted something else..."))
        self.after(9000, lambda: controller.showFrame(FightPage))
        self.after(9001,lambda: controller.frames[FightPage].enemyBattle(3,4,"random", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.two5

    def two5(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nAs you continue heading down the main road, you notice the change in environment."))
        self.after(10000, lambda: self.updateText("\n\nLarge areas of forest are burnt to ash, and vehicles aren't just abandoned, but destroyed."))
        self.after(18000, lambda: self.updateText("\n\nThe calming sounds of wildlife are replaced with eerie groans."))
        self.after(24000, lambda: self.updateText("\n\nYour thoughts are interrupted by the sound of a vehicle from behind."))
        self.after(31000, lambda: self.updateText("\n\nYou start to head off the road, but stop once the vehicle comes into view."))
        self.after(37000, lambda: self.updateText("\n\nYou see a black Jeep, with a circular emblem on the hood."))
        self.after(43000, self.clearBox)
        self.after(44000, lambda: self.updateText("\nIt's more soldiers from the Republic..."))
        self.after(50000, lambda: self.updateText("\n\nThe vehicle comes to a stop a few feet in front of you."))
        self.after(56000, lambda: self.updateText("\n\nTwo men get out, dressed in black tactical gear."))
        self.after(62000, lambda: self.updateText("\n\nYou recognize them. They were new recruits when you left."))
        self.after(68000, self.clearBox)
        self.after(69000, lambda: self.updateText("\nMcNeil: \""+Player.name+", I never thought I'd see you again!\""))
        self.after(75000, lambda: self.updateText("\n\nMcNeil: \"We saw your truck off the road a while back. There were some bodies and assumed you were all gone...\""))
        self.after(83000, lambda: self.updateText("\n\nGodfrey: \"I'm glad we were wrong though... We could use an extra gun right now.\""))
        self.after(90000, lambda: self.updateText("\n\nGodfrey: \"We got a distress call from another team. They're held up a few clicks from here.\""))
        self.after(98000, lambda: self.updateText("\n\nGodfrey: \""+Player.name+" you got shotgun. Let's get going.\""))
        self.after(104000, self.clearBox)
        self.after(105000, lambda: self.updateText("\nAfter 15 minutes, you pull into a parking lot of a small warehouse."))
        self.after(111000, lambda: self.updateText("\n\nThe building has a picture of a smiling pig on it wearing an apron."))
        self.after(117000, lambda: self.updateText("\n\nAs Godfrey and McNeil start unloading their gear from the vehicle, you hear a hissing noise from the woods..."))
        self.after(12400,lambda: controller.frames[FightPage].enemyBattle(3,4,"Velociraptor", 0))
        self.after(125000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.two6

    def two6(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nYou turn around to see Godfrey and McNeil had made quick work of the other Raptor."))
        self.after(10000, lambda: self.updateText("\n\nGodfrey: \"Remember, the distress call only provided the location, we're going in blind.\""))
        self.after(16000, lambda: self.updateText("\n\nMcNeil: \"You two take the front, I'll circle around the back.\""))
        self.after(23000, lambda: self.updateText("\n\nMcNeil heads around the building while you and Godfrey get to the front door."))
        self.after(30000, lambda: self.updateText("\n\nYou open the door quickly as Godfrey moves in with his gun raised."))
        self.after(37000, lambda: self.updateText("\n\nHe immediately gets swatted across the room."))
        self.after(43000,lambda: controller.frames[FightPage].enemyBattle(3,4,"Frost Troll", 0))
        self.after(44000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.two7

    def two7(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nYou rush over to Godfrey, kneeling down to check for a pulse."))
        self.after(9000, lambda: self.updateText("\n\nYou look up to check your surroundings as something hits your head. Everything goes dark."))
        self.after(16000, self.clearBox)
        self.after(18000, lambda: self.updateText("\nWhile dazed, you open your eyes to see McNeil and Godfreys tied up bodies being thrown into a truck."))
        self.after(26000, lambda: self.updateText("\n\nYour legs and arms are tied aswell, with tape over your mouth."))
        self.after(32000, lambda: self.updateText("\n\nThe woman next to the truck smiles as she sees you."))
        self.after(39000, lambda: self.updateText("\n\nWoman: \"Well look who it is! I should've guessed as soon as the odour of shit filled my nose.\""))
        self.after(47000, lambda: self.updateText("\n\nYou recognize her. She's the woman from the gas station."))
        self.after(52000, self.clearBox)
        self.after(53000, lambda: self.updateText("\n\nWoman: \"We were just out here rounding up some more entertainment.\""))
        self.after(60000, lambda: self.updateText("\n\nWoman: \"You wouldn't believe how many of you do-good soldiers fall for the ol' \'distress call\'.\""))
        self.after(68000, lambda: self.updateText("\n\nThe woman walks towards you and squats down as to be face-to-face."))
        self.after(73000, lambda: self.updateText("\n\nWoman: \"But I guess you stupid "+Player.color+"s fall for anything."))
        self.after(81000, lambda: self.updateText("\n\nYour eyes then get heavy and you fall out of consciousness."))
        self.after(86000, self.clearBox)
        self.after(87000, lambda: self.updateText("\nSome time later, you wake up to the sounds of cheering and applause."))
        self.after(92000, lambda: self.updateText("\n\nYou're seated in the dirt, held up by the wall behind you."))
        self.after(98000, lambda: self.updateText("\n\nThere are a few men and women near you, none of which you recognize."))
        self.after(104000, lambda: self.updateText("\n\nYou seem to be in some kind of large cage."))
        self.after(111000, lambda: self.updateText("\n\nYou stand up to look through the metal bars and see an old bull-riding stadium."))
        self.after(119000, lambda: self.updateText("\n\nThe walls are built up high, with dozens of people cheering in the bleachers above."))
        self.after(126000, self.clearBox)
        self.after(127000, lambda: self.updateText("\nAs your vision gets better, you look to the center of the stadium to see Godfrey fighting a large cyclops."))
        self.after(135000, lambda: self.updateText("\n\nGodfrey only has a spear, which he used to stab at the cyclops."))
        self.after(141000, lambda: self.updateText("\n\nIn an instant, the cyclops grabs the spear, throwing Godfrey to the ground."))
        self.after(149000, lambda: self.updateText("\n\nIt picks up Godfrey's frantic body, grabbing his torso in one hand, and legs in the other."))
        self.after(157000, lambda: self.updateText("\n\nThe cyclops rips Godfrey in half, throwing his seperated body into the crowd."))
        self.after(164000, lambda: self.updateText("\n\nThe roar of the crowd gets louder."))
        self.after(169000, self.clearBox)
        self.after(170000, lambda: self.updateText("\nAn older man comes up beside you, looking into the stadium."))
        self.after(174000, lambda: self.updateText("\n\nMan: \"I'm sorry about your friend. I saw you both get brought in together.\""))
        self.after(180000, lambda: self.updateText("\n\nThe man looks malnourished, with ragged clothes and an unkept beard."))
        self.after(185000, lambda: self.newChoice(controller, "Where's McNeil?", "What is this place?", "What do you ask?", self.twoPitMcNeil, self.twoPitInfo))

    def twoPitMcNeil(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nMan: \"I take it that was your other friend...\""))
        self.after(8000, lambda: self.updateText("\n\nMan: \"He and a few others got put up against a Xenomorph... It was a quick death.\""))
        self.after(15000, lambda: self.updateText("\n\nMan: \"They like capturing soldiers here, it makes for a more exciting fight.\""))
        self.after(23000, lambda: self.two8(controller))
        
    def twoPitInfo(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nMan: \"In a world of chaos, you will always have those that benefit from the absence of laws.\""))
        self.after(9000, lambda: self.updateText("\n\nMan: \"This place is a haven for those who aren't welcome in the more civilized towns.\""))
        self.after(16000, lambda: self.updateText("\n\nMan: \"And in your case, they will pay a high price for new fighters\""))
        self.after(22000, lambda: self.two8(controller))

    def two8(self, controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nMan: \"Thankfully I'm too frail to put on a good show for them. They keep me around for other reasons though.\""))
        self.after(10000, lambda: self.updateText("\n\nYou look back into the stadium to see the Cyclops get shot with tranquilizing darts."))
        self.after(16000, lambda: self.updateText("\n\nMan: \"I've been here a long time, and have talked to many soldiers like yourself...\""))
        self.after(23000, lambda: self.updateText("\n\nMan: \"That facility you're supposed to secure, AgriTech, that's where I used to work.\""))
        self.after(31000, lambda: self.updateText("\n\nMan: \"I know the Republic doesn't tell you much about it. So ask away, what do you want to know?\""))
        self.after(40000, lambda: self.newChoice(controller, "What is AgriTech?", "Why are you here?", "What do you ask?", self.twoPitTech, self.twoPitOther))

    def twoPitTech(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nMan: \"Our population was growing out of control, resulting in food shortages around the world.\""))
        self.after(10000, lambda: self.updateText("\n\nMan: \"AgriTech was the leading company in agricultural innovation, and worked towards solving this problem.\""))
        self.after(18000, lambda: self.updateText("\n\nMan: \"They created a machine that could generate a fully mature crop simply from it's DNA.\""))
        self.after(25000, lambda: self.updateText("\n\nMan: \"They improved this process, being able to generate whole yields of crop within seconds.\""))
        self.after(31000, lambda: self.newChoice(controller, "Where did it go wrong?", "What else did they do?", "What do you ask?", self.twoPitWrong, self.twoPitElse))

    def twoPitWrong(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nMan: \"The problem was with what they did afterwards, the experiments.\""))
        self.after(9000, lambda: self.updateText("\n\nMan: \"If they can grow a vegetable instantaneously from its DNA, why not an animal?\""))
        self.after(15000, lambda: self.updateText("\n\nMan: \"They started small, and then progressed to larger ones like cattle.\""))
        self.after(21000, lambda: self.updateText("\n\nMan: \"Unfortunately, they decided to expand their scope by using the DNA of extinct animals.\""))
        self.after(30000, lambda: self.updateText("\n\nMan: \"After a few months, they successfully created a Dilophosaurus.\""))
        self.after(36000, lambda: self.updateText("\n\nMan: \"It wasn't long until they were creating creatures from mythology and fiction, which brings us to now.\""))
        self.after(44000, lambda: self.two9(controller))

    def twoPitElse(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nMan: \"They did the same but with a variety of animals.\""))
        self.after(8000, lambda: self.updateText("\n\nMan: \"Unfortunately, they decided to expand their scope by using the DNA of extinct animals too.\""))
        self.after(21000, lambda: self.updateText("\n\nMan: \"It wasn't long until they were creating creatures from mythology and fiction, which brings us to now.\""))
        self.after(30000, lambda: self.two9(controller))
        
    def twoPitOther(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nMan: \"AgriTech's machines are a bit complicated to operate.\""))
        self.after(9000, lambda: self.updateText("\n\nMan: \"The inbreds that run this place wouldn't have a clue on how to use them, which is why they keep me here.\""))
        self.after(18000, lambda: self.two9(controller))

    def two9(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nThe man gets interrupted by people yelling."))
        self.after(8000, lambda: self.updateText("\n\nYou look into the stadium to see a gundark break loose, tearing through the crowd."))
        self.after(15000, lambda: self.updateText("\n\nWith the guard distracted, several prisoners rush the door, eventually getting it open."))
        self.after(22000, lambda: self.updateText("\n\nMan: \"I guess it's time to leave! Follow me, I know where your gear is.\""))
        self.after(29000, lambda: self.updateText("\n\nThe man leads you out of the stadium to a cattle trailer."))
        self.after(35000, lambda: self.updateText("\n\nYou locate your gear and start towards the woods."))
        self.after(43000, self.clearBox)
        self.after(44000, lambda: self.updateText("\nMan: \"Wait, they usually leave the keys in the vehicles.\""))
        self.after(48000, lambda: self.newChoice(controller, "Godfreys Black Jeep", "Large Truck", "What do you take?", self.twoJeep, self.twoTruck))

    def twoJeep(self,controller):
        self.btnDisbaled()
        GameInfo.choice = "jeep"
        self.two10(controller)

    def twoTruck(self,controller):
        self.btnDisbaled()
        GameInfo.choice = "truck"
        self.two10(controller)

    def two10(self,controller):
        self.after(2000, lambda: self.updateText("\n\nThe man gets in the drivers seat of the "+GameInfo.choice+" while you throw your gear in the back."))
        self.after(10000, lambda: self.updateText("\n\nOnce you're in, the man slams on the gas, avoiding the escaped prisoners as you exit the parking lot."))
        self.after(18000, lambda: self.updateText("\n\nThe "+GameInfo.choice+"'s clock reads 2:13am."))
        self.after(23000, lambda: self.updateText("\n\nMan: \"The next town is only a few hours from here. We should have enough gas to make it.\""))
        self.after(31000, lambda: self.updateText("\n\nYou decide to lean your seat back and rest."))
        self.after(37000, lambda: self.two11(controller))

    def two11(self, controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\n\nThe mans voice wakes you up."))
        self.after(7000, lambda: self.updateText("\n\nThe town is a few hundred meters ahead. It's smaller than the last one, but heavily fortified."))
        self.after(15000, lambda: self.updateText("\n\nThere's a sizable encampment outside the gate. You pull over just before it."))
        self.after(22000, lambda: self.updateText("\n\nMan: \"Well, it was a pleasure getting to know you. I'm going to catch up on some sleep.\""))
        self.after(30000, lambda: self.updateText("\n\nMan: \"I wish you the best of luck getting to AgriTech!\""))
        self.after(35000, self.clearBox)
        self.after(36000, lambda: self.updateText("\nThe man heads towards the town as you get your gear from the back."))
        self.after(41000, lambda: self.updateText("\n\nSomeone in a loose fitting suit approaches you moments after."))
        self.after(46000, lambda: self.updateText("\n\nBusinessman: \"I know a Republic soldier when I see one, and that means I know where you're going!\""))
        self.after(54000, lambda: self.updateText("\n\nBusinessman: \"There ain't too much of a road past here, so there's no need for those wheels.\""))
        self.after(62000, lambda: self.updateText("\n\nBusinessman: \"I'll give you 1500 gold for it right now\""))
        self.after(66000, lambda: self.newChoice(controller, "Deal", "It's worth more", "What do you say?", self.twoDeal, self.twoMore))

    def twoMore(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\n\nBusinessman: \"Don't get too greedy now, you dont have much of a choice ya know.\""))
        self.after(8000, lambda: self.updateText("\n\nBusinessman: \"Tell you what, we'll flip a coin for it...\""))
        self.after(14000, lambda: self.updateText("\n\nBusinessman: \"If you call it right, I'll give you 3000. If you're wrong, it's free.\""))
        self.after(18000, lambda: self.newChoice(controller, "Deal", "I'll take the $1500", "What do you say?", self.twoFlip, self.twoDeal))

    def twoDeal(self, controller):
        self.btnDisbaled()
        self.clearBox()
        Bag.gold+=1500
        self.after(2000, self.updateInfo)
        self.after(2000, lambda: self.updateText("\nYou hand over the keys as the man gives you a bag of gold."))
        self.after(8000, lambda: self.updateText("\n\nBusinessman: \"Pleasure doing buisness with you my friend, and incase you didn't know - \""))
        self.after(15000, lambda: self.updateText("\n\nBusinessman: \"There are no more stops after this town, so make sure you stock up on gear.\""))
        self.after(23000, lambda: self.updateText("\n\nYou make your way into the town."))
        GameInfo.location == "town"
        self.after(27000, lambda: controller.showFrame(TownPage))
        self.after(27001, self.clearBox)
        GameInfo.nextFunction = self.three1
        
    def twoFlip(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nBusinessman: \"Ah a gambler! I like it.\""))
        self.after(7000, lambda: self.updateText("\n\nThe man takes a peice of gold out of his pocket and flicks it in the air."))
        self.after(13000, lambda: self.newChoice(controller, "Heads", "Tails", "What do you call?", self.twoHeads, self.twoTails))

    def twoHeads(self,controller):
        self.clearBox()
        self.btnDisbaled()
        GameInfo.choice = "heads"
        num = random.randint(1,2)
        if num == 1:
            self.after(2000, lambda: self.updateText("\nThe coin falls to the ground, bouncing several times before landing."))
            self.after(8000, lambda: self.updateText("\n\nIt's on heads!"))
            Bag.gold+=1500
            self.after(14000, lambda: self.twoDeal(controller))
        else:
            self.after(2000, lambda: self.updateText("\nThe coin falls to the ground, bouncing several times before landing."))
            self.after(9000, lambda: self.updateText("\n\nIt's on tails..."))
            self.after(13000, lambda: self.updateText("\n\nYou hand over the keys to the man."))
            self.after(18000, lambda: self.updateText("\n\nBusinessman: \"Pleasure doing buisness with you my friend, and incase you didn't know - \""))
            self.after(24000, lambda: self.updateText("\n\nBusinessman: \"There are no more stops after this town, so make sure you stock up on gear.\""))
            self.after(32000, lambda: self.updateText("\n\nYou make your way into the town."))
            GameInfo.location == "town"
            self.after(36000, lambda: controller.showFrame(TownPage))
            self.after(36001, self.clearBox)
            GameInfo.nextFunction = self.three1

    def twoTails(self,controller):
        self.clearBox()
        self.btnDisbaled()
        GameInfo.choice = "tails"
        num = random.randint(1,2)
        if num == 1:
            self.after(2000, lambda: self.updateText("\nThe coin falls to the ground, bouncing several times before landing."))
            self.after(8000, lambda: self.updateText("\n\nIt's on tails!"))
            Bag.gold+=1500
            self.after(14000, lambda: self.twoDeal(controller))
        else:
            self.after(2000, lambda: self.updateText("\nThe coin falls to the ground, bouncing several times before landing."))
            self.after(9000, lambda: self.updateText("\n\nIt's on heads..."))
            self.after(13000, lambda: self.updateText("\n\nYou hand over the keys to the man."))
            self.after(18000, lambda: self.updateText("\n\nBusinessman: \"Pleasure doing buisness with you my friend, and incase you didn't know - \""))
            self.after(24000, lambda: self.updateText("\n\nBusinessman: \"There are no more stops after this town, so make sure you stock up on gear.\""))
            self.after(32000, lambda: self.updateText("\n\nYou make your way into the town."))
            GameInfo.location == "town"
            self.after(36000, lambda: controller.showFrame(TownPage))
            self.after(36001, self.clearBox)
            GameInfo.nextFunction = self.three1

#endregion

#region Stage Three
    def three1(self,controller):
        GameInfo.location == "road"
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nYou leave the town at sunrise."))
        self.after(7000, lambda: self.updateText("\n\nThe road is overgrown, and littered with rubble and potholes."))
        self.after(15000, lambda: self.updateText("\n\nNonetheless, the outline of the road is still clear."))
        self.after(21000, lambda: self.updateText("\n\nAs you start walking, you think about what's to come."))
        self.after(27000, lambda: self.updateText("\n\nThe creatures past this point are more dangerous than anything you've seen before."))
        self.after(34000, lambda: self.updateText("\n\nWithout your team, do you even stand a chance?"))
        self.after(40000, self.clearBox)
        self.after(41000, lambda: self.updateText("\nYour thoughts are interrupted by the distant sound of rushing water"))
        self.after(47000, lambda: self.updateText("\n\nAs you get closer to the sound, you see the road has been washed out."))
        self.after(53000, lambda: self.updateText("\n\nA strong river has cut through the road, with only a small wood bridge connecting either side."))
        self.after(61000, lambda: self.updateText("\n\nA raspy voice startles you."))
        self.after(65000, lambda: self.updateText("\n\nScavenger: \"I made that bridge myself. Beauty ain't she?\""))
        self.after(72000, lambda: self.updateText("\n\nThe man is small in stature, but loaded with gear."))
        self.after(78000, self.clearBox)
        self.after(79000, lambda: self.updateText("\nScavenger: \"I'm glad to see you're stocked up on supplies!\""))
        self.after(85000, lambda: self.updateText("\n\nScavenger: \"Just means there will be another valuable corpse to loot.\""))
        self.after(91000, lambda: self.updateText("\n\nThe man pauses when he hears a distant scream."))
        self.after(96000, lambda: self.updateText("\n\nScavenger: \"Ou, sounds like my next paycheque.\""))
        self.after(101000, lambda: self.updateText("\n\nThe man scurries across the bridge towards the screams."))
        self.after(106000, lambda: self.updateText("\n\nThe wood almost breaks under his weight. Him and his gear must weigh no more 150lbs."))
        self.after(113000, lambda: self.newChoice(controller, "Yes", "No", "Do you cross\nthe bridge?", self.threeCross, self.threeNoCross))

    def threeCross(self,controller):
        self.btnDisbaled()
        if Player.weight <=150:
            self.threeCrossedBridge(controller)
        else: 
            self.threeBridgeBroke(controller)
    
    def threeBridgeBroke(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nThe wood creaks under your feet as you step onto the bridge."))
        self.after(8000, lambda: self.updateText("\n\nAs your halfway across, the bridge collapses, dropping you into the water."))
        self.after(15000, lambda: self.updateText("\n\nYou are hurled down the river, looking for something to grab onto."))
        self.after(23000, lambda: self.updateText("\n\nAfter a slow 30 seconds, you manage to grab ahold of some roots from a nearby tree."))
        self.after(30000, lambda: self.updateText("\n\nYou carefully pull yourself to the other side of the river, up onto the bank."))
        if Bag.lcaliber >= 150:
            self.after(37000, lambda: self.updateText("\n\nAfter checking your gear, you realize you've lost 150 rounds of 7.62mm."))
            Bag.lcaliber-=150
        elif Bag.scaliber >= 150:
            self.after(37000, lambda: self.updateText("\n\nAfter checking your gear, you realize you've lost 150 rounds of 9mm."))
            Bag.scaliber-=150
        elif Bag.arrows >= 50:
            self.after(38000, lambda: self.updateText("\n\nAfter checking your gear, you realize you've lost 50 arrows."))
            Bag.arrows-=50
        else: 
            self.after(37000, lambda: self.updateText("\n\nThankfully, you didn't lose any gear in the river."))
        self.after(45000, lambda: self.threeExitRiver(controller))

    def threeNoCross(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nYou head downstream along the bank, looking for an area to cross."))
        self.after(9000, lambda: self.updateText("\n\nOnly moments later something charges out of the thick brush."))
        self.after(14000,lambda: controller.frames[FightPage].enemyBattle(3,4,"Saber-Toothed Tiger", 0))
        self.after(15000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.threeNoCrossAfter
    
    def threeNoCrossAfter(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nAs you kill the tiger, you lose balance and fall backwards into the river."))
        self.after(9000, lambda: self.updateText("\n\nAfter 15 seconds of being thrown about, you manage to grab onto roots from a nearby tree."))
        self.after(17000, lambda: self.updateText("\n\nYou carefully pull yourself to the other side of the river, up onto the bank."))
        self.after(23000, lambda: self.updateText("\n\nThankfully, you didn't lose any gear."))
        self.after(29000, lambda: self.threeExitRiver(controller))
        
    def threeExitRiver(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nAs you make your way back towards the road, the ground crunches beneath you."))
        self.after(9000, lambda: self.updateText("\n\nLooking down, you realize you're walking over dozens of small bones, mostly picked clean."))
        self.after(18000, lambda: self.updateText("\n\nThe sound of high-pitched yips and howls soon fill your ears..."))
        self.after(24000,lambda: controller.frames[FightPage].enemyBattle(3,4,"Pack of Coyotes", 0))
        self.after(25000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.threeAfterCoyotes

    def threeAfterCoyotes(self,controller):
        self.after(2000, lambda: self.updateText("\n\nAmongst the bones and animal corpses, you see a pile of dead soldiers."))
        self.after(9000, lambda: self.newChoice(controller, "Yes", "No", "Do you loot them?", self.threeLoot, self.threeSoldierAlive))

    def threeLoot(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nYou begin searching the bodies..."))
        self.after(6000, lambda: self.eventAmmo("small"))
        self.after(10000, lambda: self.eventAmmo("large"))
        self.after(14000, lambda: self.eventAmmo("medium"))
        self.after(18000, self.eventPotion)
        self.after(22000, self.eventPotion)
        self.after(28000, lambda: self.threeSoldierAlive(controller))

    def threeSoldierAlive(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nAs you begin walking away, you hear a groan."))
        self.after(7000, lambda: self.updateText("\n\nYou look back to see that one of the soldiers is still alive."))
        self.after(14000, lambda: self.updateText("\n\nHer right arm is chewed through to the bone, and chunks of her thighs taken out."))
        self.after(21000, lambda: self.updateText("\n\nWith her left hand, she painfully pulls a gun from her waist and hands it to you."))
        self.after(28000, lambda: self.newChoice(controller, "Yes", "No", "Do you put her\nout of her misery?", self.threeKillSoldier, self.threeLetSoldierLive))

    def threeKillSoldier(self,controller):
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\n\nYou take the pistol, confirming there's a round chambered."))
        self.after(9000, lambda: self.updateText("\n\nAs she closes her eyes, you aim at her head and squeeze the trigger."))
        self.after(17000, lambda: self.threeLeaveRiver(controller))

    def threeLetSoldierLive(self,controller):
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\n\nYou turn your back, walking away as you hear her muffled groans and cries."))
        self.after(11000, lambda: self.threeLeaveRiver(controller))

    def threeLeaveRiver(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nAfter leaving the area, you make it back to the main road with haste."))
        self.after(10000, lambda: self.three2(controller))
        
    def threeCrossedBridge(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nYou safely make it across the bridge."))
        self.after(8000, lambda: self.three2(controller))

    def three2(self,controller):
        self.after(2000, lambda: self.updateText("\n\nThe next couple kilometers passed without issue."))
        self.after(8000, lambda: self.updateText("\n\nYou often heard screeching and growls from the woods, but none were close enough to cause concern."))
        self.after(17000, lambda: self.updateText("\n\nFurther down the road, you see a group of people wearing robes and odd masks."))
        self.after(24000, lambda: self.updateText("\n\nAs you creep closer, you see a man being dragged behind them."))
        self.after(31000, lambda: self.updateText("\n\nIt looks like the scavenger you talked to earlier..."))
        self.after(30000, lambda: self.newChoice(controller, "Yes", "No", "Do you save him?", self.threeTuskens, self.threeNoTuskens))

    def threeTuskens(self,controller):
        self.btnDisbaled()
        self.after(500,lambda: controller.frames[FightPage].enemyBattle(3,4,"Tusken Raiders", 0))
        self.after(1000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.threeKilledTuskens
    
    def threeKilledTuskens(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nAfter killing the last raider, you untie the scavenger and remove the gag from his mouth."))
        self.after(10000, lambda: self.updateText("\n\nScavenger: \"Oh jesus thank you! I swear those sand people come from the depths of hell.\""))
        self.after(18000, lambda: self.updateText("\n\nScavenger: \"I gotta go back and grab my gear before something takes it.\""))
        self.after(24000, lambda: self.updateText("\n\nAs the man heads off towards the woods, he yells out."))
        self.after(30000, lambda: self.updateText("\n\nScavenger: \"Thanks again. I owe you one!\""))
        self.after(35000, lambda: self.updateText("\n\nYou watch him disappear into the woods before continuing down the road."))
        GameInfo.choice = "scavenger"
        self.after(42000, lambda: self.three3(controller))

    def threeNoTuskens(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nRemaining out of site, you watch as the man gets dragged into the woods."))
        self.after(9000, lambda: self.updateText("\n\nAfter a few minutes you get back on the road and continue your journey."))
        self.after(16000, lambda: self.three3(controller))

    def three3(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nNot long after, you come across what seems to be an old general store."))
        self.after(9000, lambda: self.updateText("\n\nThis is the first place you've come across since the town that's still intact."))
        self.after(15000, lambda: self.newChoice(controller, "Yes", "No", "Do you enter?", self.threeStore, self.three4))

    def threeStore(self,controller):
        self.after(2000, lambda: self.updateText("\nThe front doors have been ripped off, and all windows smashed in."))
        self.after(9000, lambda: self.updateText("\n\nInside doesn't look any better. The shelves are all knocked over onto the floor."))
        self.after(15000, lambda: self.updateText("\n\nBehind the front desk, you see a locked door."))
        self.after(20000, lambda: self.newChoice(controller, "Yes", "No", "Do you kick it in?", self.threeStoreDoor, self.threeStoreDoor))

    def threeStoreDoor(self,controller):
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\n\nIn an instant, something barges through the front entrance of the store."))
        self.after(7000,lambda: controller.frames[FightPage].enemyBattle(3,4,"Reek", 0))
        self.after(8000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.threeLeaveStore

    def threeLeaveStore(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nThe creature casued alot of structural damage, the building is starting to collapse."))
        self.after(10000, lambda: self.updateText("\n\nYou make it out just as the building crumbles, then get back on the road."))
        self.after(17000, lambda: self.three4(controller))

    def three4(self,controller):
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nOver the next few kilometers, the sun quickly sets."))
        self.after(7000, lambda: self.updateText("\n\nAs the darkness makes it harder to see the road ahead, you decide to set up camp."))
        self.after(14000, self.clearBox)
        self.after(15000, lambda: self.updateText("\nOnce you get into the woods, you start to unpack your gear."))
        self.after(21000, lambda: self.updateText("\n\nYou turn around at the sound of a twig snapping to see an outline of a large beast."))
        self.after(27000, lambda: self.updateText("\n\nThe last thing you hear is its roar."))
        self.after(36000, lambda: self.updateText("\n\nYou slowly gain consciousness. Your head throbs as you slowly open your eyes."))
        self.after(44000, lambda: self.updateText("\n\nYou're hanging upside down is some cave. Your feet are glued to the ceiling."))
        self.after(51000, self.clearBox)
        self.after(52000, lambda: self.updateText("\nThe cave is dark, but bright enough to see whats around you."))
        self.after(58000, lambda: self.updateText("\n\nIt's not very large, but is filled with bones and carcasses, along with alot of supplies from past kills."))
        self.after(68000, lambda: self.updateText("\n\nGathering your thoughts, you look around to figure out a way to escape."))
        self.after(75000, lambda: self.updateText("\n\nUsing a fractured bone from the ground, you start chipping away at the glue holding your feet."))
        self.after(84000, lambda: self.updateText("\n\nThe sound draws the attention of the beast, just as you get free and fall to the ground."))
        self.after(91000,lambda: controller.frames[FightPage].enemyBattle(3,4,"Wampa", 0))
        self.after(92000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.three5
    
    def three5(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nAfter killing it, you spend time looking through supplies in the cave."))
        self.after(9000, lambda: self.eventAmmo("large"))
        self.after(13000, lambda: self.eventAmmo("large"))
        self.after(17000, self.eventPotion)
        self.after(21000, lambda: self.eventAmmo("medium"))
        self.after(25000, self.eventPotion)
        self.after(29000, self.clearBox)
        self.after(30000, lambda: self.updateText("\nWhile looking through the cave, you uncover a sign that reads \"Property of AgriTech\"."))
        self.after(37000, lambda: self.updateText("\n\nMoving debris out of the area, you then discover a sewer entrance."))
        self.after(43000, lambda: self.updateText("\n\nYou crawl inside, eventually getting to a larger tunnel that's big enough for you to stand in."))
        self.after(51000, lambda: self.updateText("\n\nThe tunnel is dimly lit by red emergency lights, making the journey much easier."))
        self.after(59000, lambda: self.updateText("\n\nAfter a good 30 minutes, you finally get to a large open area that has an exit door."))
        self.after(67000, self.clearBox)
        self.after(68000, lambda: self.updateText("\nAs you approach the door, you feel something hit your shoulder."))
        self.after(74000, lambda: self.updateText("\n\nIt's a clear slimy substance that dripped from the ceiling."))
        self.after(79000,lambda: controller.frames[FightPage].enemyBattle(3,4,"Xenomorph", 0))
        self.after(80000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.three6

    def three6(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nThrough the door, there is a large room filled with furniture and equipment."))
        self.after(10000, lambda: self.updateText("\n\nFurther into the room there's a corpse just outside a locked metal door."))
        self.after(16000, lambda: self.updateText("\n\nYou try the door, but it's far too strong to be forced open."))
        if Bag.grenades >=1:
            self.after(22000, lambda: self.updateText("\n\nA grenade should blow the door open. You have "+Bag.grenades+" grenades."))
            self.after(28000, lambda: self.newChoice(controller, "Yes", "No", "Use a grenade?", self.threeBlowDoor, self.three7))
        else:
            self.after(22000, lambda: self.updateText("\n\nA grenade would've worked if you had one."))
            self.after(27000, lambda: self.three7(controller))

    def threeBlowDoor(self,controller):
        self.btnDisbaled()
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nOnce behind cover, you roll a live grenade towards the door."))
        self.after(8000, lambda: self.updateText("\n\nThe blast was enough to open it up."))
        self.after(14000, lambda: self.updateText("\n\nInside, you see several more corpses in lab coats, with a stockpile of supplies."))
        self.after(22000, lambda: self.updateText("\n\nThey must've tried to escape when things went south here."))
        self.after(28000, lambda: self.updateText("\n\nYou find a box with 4 grenades, as well as a crate full of health potions."))
        Bag.grenades+=4
        Bag.healthPotion+=15
        self.after(29000, self.updateInfo)
        self.after(35000, lambda: self.three7(controller))
        
    def three7(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nYou make your way over to the elevator doors on the other side of the room."))
        self.after(9000, lambda: self.updateText("\n\nThe inside of the elevetor is stained red, with paper scattered around the floor."))
        self.after(17000, lambda: self.updateText("\n\nThis should take you up to the main level of the facility."))
        self.after(23000, lambda: self.updateText("\n\nOnce you're up there, you'll need to locate the power generators and shut them off."))
        self.after(29000, lambda: self.updateText("\n\nAfter getting to the main level, the doors open to reveal a destroyed lobby."))
        self.after(35000, lambda: self.updateText("\n\nThe front of the building has falllen apart, with very little wall left seperating the inside from the out."))
        self.after(43000, self.clearBox)
        self.after(44000, lambda: self.updateText("\nAs you exit the elevator, a chimp swings from the ceiling towards you."))
        self.after(49000,lambda: controller.frames[FightPage].enemyBattle(3,4,"Chimpanzee", 0))
        self.after(50000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.three8

    def three8(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nOn one of the walls in the lobby, you find a map of the property."))
        self.after(8000, lambda: self.updateText("\n\nThere's a building out back that is marked with a lightning bolt."))
        self.after(14000, lambda: self.updateText("\n\nThat must be where the generators are."))
        self.after(19000, lambda: self.updateText("\n\nTo avoid what's outside, you navigate your way through the facililty towards the back exit."))
        self.after(26000, lambda: self.updateText("\n\nNearly to the door, you feel a slight pinch on your leg."))
        self.after(32000,lambda: controller.frames[FightPage].enemyBattle(3,4,"Squirrel", 0))
        self.after(33000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.three9

    def three9(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nLooking through the window in the back door, you see the electrical building only 50 meters away."))
        self.after(10000, lambda: self.updateText("\n\nYou're entire mission, everything you've been through, was to get to this point."))
        self.after(16000, lambda: self.updateText("\n\nAs you open the door, a high-pitched screech rings throughout your ears, followed by intense gusts of wind."))
        self.after(24000, lambda: self.updateText("\n\nA large creature lands just outside the building, blocking your path."))
        self.after(30000,lambda: controller.frames[FightPage].enemyBattle(3,4,"Dragon", 0))
        self.after(31000, lambda: controller.showFrame(FightPage))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.three10

    def three10(self,controller):
        self.clearBox()
        self.after(2000, lambda: self.updateText("\nYou quickly make it into the electrical building and shut the door behind you."))
        self.after(9000, lambda: self.updateText("\n\nLooking at the various panels around the room, you locate the one powering the labs."))
        self.after(17000, lambda: self.updateText("\n\nYou turn it off, being sure to keep all other power on in the facility."))
        self.after(23000, lambda: self.updateText("\n\nAs you begin to head back into the main building to look for a radio, you stop in your tracks."))
        self.after(32000, self.clearBox)
        self.after(33000, lambda: self.updateText("\nYou are supposed to radio in to the Republic, reporting on your success."))
        self.after(39000, lambda: self.updateText("\n\nWith no more creatures being generated, the Republic can make it here in a few days."))
        self.after(47000, lambda: self.updateText("\n\nOnce arrived, they'll take control of the facility, and send you back to the city."))
        self.after(53000, lambda: self.updateText("\n\nYour mind goes to the conversation you overheard on the road a while back."))
        self.after(59000, lambda: self.updateText("\n\nThe group of men at night speaking about the the Republic."))
        self.after(65000, lambda: self.updateText("\n\nHow controlling this facility will just make them more powerful. How the people will still have to fight to survive."))
        self.after(73000, self.clearBox)
        self.after(74000, lambda: self.updateText("\nYou're hopeful the Republic will do the right thing, but can't know for sure."))
        self.after(80000, lambda: self.updateText("\n\nWhat if you didn't radio them, but rather created your own community here?"))
        self.after(86000, lambda: self.updateText("\n\nYou could recruit people from the surrounding towns to help rebuild."))
        self.after(91000, lambda: self.updateText("\n\nThe agricultural machines in the facility will provide unlimited food."))
        self.after(97000, lambda: self.updateText("\n\nUnfortunately, the Republic would surely attack when they found out..."))
        self.after(103000, lambda: self.updateText("\n\nThere's no right answer. You'll just have to go with your gut feeling."))
        self.after(109000, lambda: self.newChoice(controller, "Radio the Republic", "Build your own\ncommunity", "How will your\nstory end?", self.threeRepublic, self.threeCommunity))

    def threeRepublic(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nThe Republic thanks you for your service."))
        self.after(8000, lambda: self.updateText("\n\nAs they take control of the facility in the coming days, you are relieved of your duty."))
        self.after(16000, lambda: self.updateText("\n\nYou're driven back to the city, rewarded with a sizeable payment in gold."))
        self.after(22000, lambda: self.updateText("\n\nWhat happens next is out of your control..."))
        self.after(30000, lambda: self.three11(controller))

    def threeCommunity(self,controller):
        self.clearBox()
        self.btnDisbaled()
        self.after(2000, lambda: self.updateText("\nYou make you way to the previous town, recruiting the ex-AgriTech employee you met before."))
        self.after(10000, lambda: self.updateText("\n\nSeveral others join and help rid the area of any and all straggling creatures."))
        self.after(17000, lambda: self.updateText("\n\nMore people trickle in everyday as the word spreads throughout the area."))
        self.after(24000, lambda: self.updateText("\n\nBut it's only a matter of time until it reaches the Republic..."))
        self.after(32000, lambda: self.three11(controller))

    def three11(self,controller):
        controller.frames[EndPage].updateInfo()
        controller.showFrame(EndPage)
#endregion

class FightPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.fightPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.fightPage.pack()
        self.fightPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.lblEnemyPic = tk.Label(self.fightPage, height=18, width=40, bg="black")
        self.lblEnemyPic.place(relx=.05, rely=.085)

        self.lblEnemyHealth = tk.Label(self.fightPage, height=1, width=25, bg="#751515", fg="white", font="Arial 15")
        self.lblEnemyHealth.place(relx=.05, rely=.359)

        self.lblAddEH = tk.Label(self.fightPage, height=1, width=2, bg="#751515", font="Arial 15")
        self.lblAddEH.place(relx=.2845, rely=.359)

        self.lblEnemyName = tk.Label(self.fightPage, height=1, width=20, bg="black", fg="white", font="Arial 18")
        self.lblEnemyName.place(relx=.05, rely=.05)

        self.lblAddEN = tk.Label(self.fightPage, height=1, width=2, bg="black", font="Arial 15")
        self.lblAddEN.place(relx=.2845, rely=.05)

        self.lblInventory = tk.Label(self.fightPage, height=18, width=75, bg="black")
        self.lblInventory.place(relx=.45, rely=.05)

        self.lblInvTitle = tk.Label(self.fightPage, height=1, width=32, bg="black", fg="white", font="Arial 20", text="  "+Player.name + "'s Inventory", anchor='center')
        self.lblInvTitle.place(relx=.45, rely=.05)

        self.lblArrow = tk.Label(self.fightPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Arrows: "+str(Bag.arrows), anchor='w')
        self.lblArrow.place(relx=.48, rely=.12)

        self.lblSCal = tk.Label(self.fightPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="9mm Rounds: "+str(Bag.scaliber), anchor='w',)
        self.lblSCal.place(relx=.48, rely=.18)

        self.lblMCal = tk.Label(self.fightPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="7.62mm Rounds: "+str(Bag.lcaliber), anchor='w')
        self.lblMCal.place(relx=.48, rely=.24)

        self.lblGrenade = tk.Label(self.fightPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Grenades: "+str(Bag.grenades), anchor='w')
        self.lblGrenade.place(relx=.48, rely=.30)

        self.lblSpecialWord = tk.Label(self.fightPage, height=1, width = 20, bg="black", fg="white", font="Arial 15", text="Special: ", justify="left", anchor='nw')
        self.lblSpecialWord.place(relx=.7, rely=.12)

        self.lblSpecial = tk.Label(self.fightPage, height=2, width=20, bg="black", fg="white", font="Arial 15", text=str(playerWeapons[5][1]), anchor='nw', justify="left", wraplength=220, )
        self.lblSpecial.place(relx=.72, rely=.17)

        self.lblHealthPot = tk.Label(self.fightPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Health Potions: "+str(Bag.healthPotion), anchor='w')
        self.lblHealthPot.place(relx=.70, rely=.24)

        self.lblStaminaPot = tk.Label(self.fightPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Stamina Potions: "+str(Bag.staminaPotion), anchor='w')
        self.lblStaminaPot.place(relx=.70, rely=.30)

        self.lblPHealth = tk.Label(self.fightPage, height=1, width=24, bg="#751515", fg="white", font="Arial 15", text="Health: "+str(Player.health)+"/"+str(Player.maxHealth))
        self.lblPHealth.place(relx=.45, rely=.359)

        self.lblPStamina = tk.Label(self.fightPage, height=1, width=24, bg="#157528", fg="white", font="Arial 15", text="Stamina: "+str(Player.stamina)+"/"+str(Player.maxStamina))
        self.lblPStamina.place(relx=.687, rely=.359)

        self.fightText = tk.Text(self.fightPage, height=9, width=60, state="disabled", bg="black", fg="white", font="Arial 18", padx=25, wrap="word")
        self.fightText.tag_configure("center", justify='center', spacing1=5)
        self.fightText.tag_add("center", 1.0, "end")
        self.fightText.place(relx=.05, rely=.42)
       
        
        self.btnMelee = tk.Button(self.fightPage, bg="#909090",text="Melee", cursor="hand2", command=lambda: self.playerAttack(0, False, controller))
        self.btnMelee.place(relx=.05, rely=.76)
        self.lblMelee = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblMelee.place(relx=.037, rely=.88)

        self.btnBow = tk.Button(self.fightPage, bg="#909090",text="Bow",cursor="hand2", command=lambda: self.playerAttack(1, False, controller))
        self.btnBow.place(relx=.188, rely=.76)
        self.lblBow = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblBow.place(relx=.179, rely=.8925)

        self.btnSmallCal = tk.Button(self.fightPage, bg="#909090",text= "Sidearm",cursor="hand2", command=lambda: self.playerAttack(2, False, controller))
        self.btnSmallCal.place(relx=.318, rely=.76)
        self.lblSmallCal = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblSmallCal.place(relx=.309, rely=.88)

        self.btnMedCal = tk.Button(self.fightPage, bg="#909090",text="Rifle",cursor="hand2", command=lambda: self.playerAttack(3, False, controller))
        self.btnMedCal.place(relx=.448, rely=.76)
        self.lblMedCal = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblMedCal.place(relx=.439, rely=.88)

        self.btnGrenade = tk.Button(self.fightPage, bg="#909090",text="Grenade",cursor="hand2", command=lambda: self.playerAttack(4, False, controller))
        self.btnGrenade.place(relx=.578, rely=.76)
        self.lblGren = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblGren.place(relx=.569, rely=.88)

        self.btnSpecial = tk.Button(self.fightPage, bg="#909090",text="Special",cursor="hand2", command=lambda: self.playerAttack(5, False, controller))
        self.btnSpecial.place(relx=.712, rely=.76)
        self.lblSpec = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblSpec.place(relx=.703, rely=.88)

        self.btnSkip = tk.Button(self.fightPage, width=8, height=3,cursor="hand2",text="Skip\nAttack",font="Arial 15", bg="grey",fg="white", command=lambda: self.playerAttack(6, True, controller))
        self.btnSkip.place(relx=.845, rely=.765)

        self.btnHealth = tk.Button(self.fightPage, width=13, height=5,cursor="hand2", bg="#909090", command= self.healthPotion)
        try:
            self.picHealth = ImageTk.PhotoImage(Image.open(potionList[0][3]))
            self.btnHealth.configure(width=95, height=80, image=self.picHealth)
        except:
            self.btnHealth.configure(width=13, height=5, text="Health\nPotion")
        self.btnHealth.place(relx=.845, rely=.42)
        self.lblAddHealth = tk.Label(self.fightPage, width = 10, height=1, bg="#1a1a1a", fg="white",font="Arial 12", text="+"+str(potionList[0][1])+" Health")
        self.lblAddHealth.place(relx=.846, rely=.53)

        self.btnStamina = tk.Button(self.fightPage, width=13, height=5,cursor="hand2", bg="#909090", command = self.staminaPotion)
        try:
            self.picStamina = ImageTk.PhotoImage(Image.open(potionList[1][3]))
            self.btnStamina.configure(width=95, height=80, image=self.picStamina)
        except:
            self.btnStamina.configure(width=13, height=5, text="Stamina\nPotion")
        self.btnStamina.place(relx=.845, rely=.58)
        self.lblAddStamina = tk.Label(self.fightPage, width = 10, height=1, bg="#1a1a1a", fg="white",font="Arial 12", text="+"+str(potionList[1][1])+" Stamina")
        self.lblAddStamina.place(relx=.846, rely=.69)

    def enemyBattle(self, minEnemyLvl, maxEnemyLvl, nameOrRandom, zeroOrGoldAmt):
        self.enemySelector(minEnemyLvl, maxEnemyLvl, nameOrRandom, zeroOrGoldAmt)
        
        self.lblEnemyName.configure(text = Enemy.name)
        self.picEnemy = ImageTk.PhotoImage(Image.open(Enemy.picture))
        self.lblEnemyPic.configure(bg="black", width=282, height = 215, image=self.picEnemy)
        self.updateInfo()
        self.buttonState("normal", "hand2")
        
    def enemySelector(self,minEnemyLvl, maxEnemyLvl, nameOrRandom, zeroOrGoldAmt):
        """Chooses a monster from a 2D list"""
        if nameOrRandom != "random":
            for x in range(len(monsterList)): #Goes through the list looking for the correct monsters name. Once found, the details of the monster is assigned to the monster_index variable
                if monsterList[x][1] == nameOrRandom: #If the correct enemy is found
                    selectedEnemy = monsterList[x]
                    self.updateEnemyObject(selectedEnemy, zeroOrGoldAmt)
        else:
            x = 0
            while x < 100:
                selectedEnemy = monsterList[random.randint(0, len(monsterList)-1)] #Chooses a random monster from the list
                if minEnemyLvl <= selectedEnemy[0] <= maxEnemyLvl: #Checks to see of the chosen monster is the right level
                    self.updateEnemyObject(selectedEnemy, zeroOrGoldAmt)
                else:
                    x += 1

    def updateEnemyObject(self, enemy, goldAmt):
        Enemy.level = enemy[0]
        Enemy.name = enemy[1]
        Enemy.health = enemy[2]
        Enemy.attack1 = [enemy[3], enemy[4], enemy[5]]
        Enemy.attack2 = [enemy[6], enemy[7], enemy[8]]
        Enemy.attack3 = [enemy[9], enemy[10], enemy[11]]
        Enemy.finalMove = enemy[12]
        Enemy.reward = goldAmt
        Enemy.picture = enemy[13]

    def playerAttack(self,index,skip,controller):
        self.buttonState("disabled", "x_cursor")
        successfulAttack = False
        if skip == False:
            if playerWeapons[index][1] == "":
                self.clearText()
                self.updateText("\nEmpty weapon slot")
            elif index == 0: #if weapon is melee
                if Player.stamina < playerWeapons[index][5]:
                    self.clearText()
                    self.updateText("\nInsufficient stamina\n\nYou have: "+str(Player.stamina)+"\nRequired amount: "+str(playerWeapons[1][5]))
                else:
                    successfulAttack = True
                    damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                    GameInfo.damDealt+=damage
                    Player.stamina -= playerWeapons[index][5]
                    self.displayAttack(index, damage)
            elif index == 1:
                if Player.stamina < playerWeapons[index][5]:
                    self.clearText()
                    self.updateText("\nInsufficient stamina\n\nYou have: "+str(Player.stamina)+"\nRequired amount: "+str(playerWeapons[1][5]))
                elif Bag.arrows < playerWeapons[index][7]:
                    self.clearText()
                    self.updateText("\nInsufficient arrows\n\nYou have: "+str(Bag.arrows)+"\nRequired amount: "+str(playerWeapons[1][7]))
                else:
                    successfulAttack = True
                    damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                    GameInfo.damDealt+=damage
                    Player.stamina -= playerWeapons[index][5]
                    Bag.arrows -= playerWeapons[index][7]
                    GameInfo.arrows+=playerWeapons[index][7]
                    self.displayAttack(index, damage)
            elif index == 2:
                if Bag.scaliber < playerWeapons[index][7]:
                    self.clearText()
                    self.updateText("\nInsufficient 9mm rounds\n\nYou have: "+str(Bag.scaliber)+"\nRequired amount: "+str(playerWeapons[2][7]))
                else:
                    successfulAttack = True
                    damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                    GameInfo.damDealt+=damage
                    Bag.scaliber -= playerWeapons[index][7]
                    GameInfo.sCal+=playerWeapons[index][7]
                    self.displayAttack(index, damage)
            elif index == 3:
                if Bag.lcaliber < playerWeapons[index][7]:
                    self.clearText()
                    self.updateText("\nInsufficient 7.62mm rounds\n\nYou have: "+str(Bag.lcaliber)+"\nRequired amount: "+str(playerWeapons[3][7]))
                else:
                    successfulAttack = True
                    damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                    GameInfo.damDealt+=damage
                    Bag.lcaliber -= playerWeapons[index][7]
                    GameInfo.mCal+=playerWeapons[index][7]
                    self.displayAttack(index, damage)
            elif index == 4:
                if Bag.grenades < 1:
                    self.clearText()
                    self.updateText("\nInsufficient grenades\n\nYou have: "+str(Bag.grenades)+"\nRequired amount: "+str(playerWeapons[4][7]))
                else:
                    successfulAttack = True
                    damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                    GameInfo.damDealt+=damage
                    Bag.grenades -= playerWeapons[index][7]
                    GameInfo.grenades+=playerWeapons[index][7]
                    self.displayAttack(index, damage)
            elif index == 5:
                if playerWeapons[5][1] == "": #does the player have a speical attack in their inventory?
                    self.clearText()
                    self.updateText("\n\nYou do not own a special attack")
                else:
                    successfulAttack = True
                    damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                    GameInfo.damDealt+=damage
                    GameInfo.special+=1
                    self.displayAttack(index, damage)
                    playerWeapons[5] = ["", "", "", "", "", "", "", "", "", ""] #If the player does have a special attack, this will remove it after they use it - to ensure the player cant stack multiple special attacks
        else:
            successfulAttack = True
            self.clearText()
            self.updateText("\nYou miss your opportunity to attack")

        self.updateInfo()

        if successfulAttack == False:
            self.buttonState("normal", "hand2")

        if Enemy.health > 0 and successfulAttack == True:
            num = random.randint(1,3)
            if num == 1:
                eDamage = Enemy.attack(Enemy.attack1)
                eAttack = Enemy.attack1[0]
            elif num == 2:
                eDamage = Enemy.attack(Enemy.attack2)
                eAttack = Enemy.attack2[0]
            elif num == 3:
                eDamage = Enemy.attack(Enemy.attack3)
                eAttack = Enemy.attack3[0]
            
            Player.health -= eDamage
            GameInfo.damTaken+=eDamage

            if Player.health < 1:
                Player.health = 0

            self.fightText.after(5000, lambda: self.enemyAttack(eAttack, eDamage))

            if Player.health > 0:
                self.fightPage.after(8000, lambda: self.buttonState("normal", "hand2"))
            else: 
                self.fightText.after(9000, self.clearText)
                self.fightText.after(10000, lambda: self.updateText("\n\nThe "+Enemy.name+" "+Enemy.finalMove))

        elif Enemy.health < 1:
            if GameInfo.mode == 1: #If playing story mode
                if GameInfo.location == "road":
                    gold = self.enemyGold(Enemy.level)
                    Bag.gold += gold
                    GameInfo.goldEarned+=gold
                    GameInfo.enemies+=1
                    self.fightText.after(3000, lambda: self.updateText("\n\nYou've killed the "+Enemy.name+" and found "+str(gold)+" gold!"))
                    self.fightPage.after(5000, lambda: self.updateText("\n\nExiting..."))
                    self.fightPage.after(6999, self.clearText)
                    self.fightPage.after(7000, lambda: controller.showFrame(MainPage))
                    self.fightPage.after(7000, controller.frames[MainPage].updateInfo)
                    self.fightPage.after(7000, lambda: GameInfo.nextFunction(controller))
                elif GameInfo.location == "town":
                    gold = Enemy.reward
                    Bag.gold += gold
                    GameInfo.goldEarned+=gold
                    GameInfo.enemies+=1
                    self.fightText.after(3000, lambda: self.updateText("\n\nYou've killed the "+Enemy.name+" and earned "+str(gold)+" gold!"))
                    self.fightPage.after(5000, lambda: self.updateText("\n\nExiting..."))
                    self.fightPage.after(6999, self.clearText)
                    controller.frames[ArenaPage].updateInfo()
                    self.fightPage.after(7000, lambda: controller.showFrame(ArenaPage)) 
            elif GameInfo.mode == 2: #if playing quick play
                gold = Enemy.reward
                Bag.gold += gold
                GameInfo.goldEarned+=gold
                GameInfo.enemies+=1
                self.fightText.after(3000, lambda: self.updateText("\n\nYou've killed the "+Enemy.name+" and earned "+str(gold)+" gold!"))
                self.fightPage.after(5000, lambda: self.updateText("\n\nExiting..."))
                self.fightPage.after(6999, self.clearText)
                controller.frames[ArenaPage].updateInfo()
                self.fightPage.after(7000, lambda: controller.showFrame(ArenaPage))     

    def displayAttack(self, index, damage):
        Enemy.health -= damage
        if Enemy.health < 1:
            Enemy.health = 0
        self.clearText()
        self.updateText("\nYou dealt "+str(damage)+" damage with your "+playerWeapons[index][1]+"\nThe "+Enemy.name+" has "+str(Enemy.health)+" health remaining")
        
    def enemyAttack(self, att, dmg):
          
        self.updateText("\n\nThe "+Enemy.name+" "+att+" for "+str(dmg)+" damage\nYou have "+str(Player.health)+" health remaining")
        self.updateInfo()

    def healthPotion(self):
        if Bag.healthPotion == 0:
            self.clearText()
            self.updateText("\nInsufficient health potions\n\nYou have: "+str(Bag.healthPotion)+"\nRequired amount: 1")
        elif Player.health == Player.maxHealth:
            self.clearText()
            self.updateText("\n\nAlready at max health")
        else:
            Bag.healthPotion -= 1
            GameInfo.hPotion+=1
            Player.health += potionList[0][1]
            if Player.health > Player.maxHealth:
                Player.health = Player.maxHealth
            self.updateInfo()
    
    def staminaPotion(self):
        if Bag.staminaPotion == 0:
            self.clearText()
            self.updateText("\nInsufficient stamina potions\n\nYou have: "+str(Bag.staminaPotion)+"\nRequired amount: 1")
        elif Player.stamina == Player.maxStamina:
            self.clearText()
            self.updateText("\n\nAlready at max stamina")
        else:
            Player.stamina += potionList[1][1]
            Bag.staminaPotion -= 1
            GameInfo.sPotion+=1
            if Player.stamina > Player.maxStamina:
                Player.stamina = Player.maxStamina
            self.updateInfo()

    def enemyGold(self, enemyLevel):
        """Choses a random amount of gold to give the player after the monsters is defeated"""
        ranNum = random.randint(10, 60)
        goldRecovered = ranNum*enemyLevel #Amount of gold received based on enemies level
        return goldRecovered

    def buttonState(self, text, curs):
        self.btnBow.configure(state=text, cursor=curs)
        self.btnMelee.configure(state=text, cursor=curs)
        self.btnSmallCal.configure(state=text, cursor=curs)
        self.btnMedCal.configure(state=text, cursor=curs)
        self.btnGrenade.configure(state=text, cursor=curs)
        self.btnSpecial.configure(state=text, cursor=curs)
        self.btnSkip.configure(state=text, cursor=curs)
        self.btnHealth.configure(state=text, cursor=curs)
        self.btnStamina.configure(state=text, cursor=curs)
        
    def updateInfo(self):
        self.lblEnemyHealth.configure(text="Health: "+str(Enemy.health))
        self.lblArrow.configure(text="Arrows: "+str(Bag.arrows))
        self.lblSCal.configure(text="9mm Rounds: "+str(Bag.scaliber))
        self.lblMCal.configure(text="7.62mm Rounds: "+str(Bag.lcaliber))
        self.lblGrenade.configure(text="Grenades: "+str(Bag.grenades))
        self.lblSpecial.configure(text=str(playerWeapons[5][1]))
        self.lblHealthPot.configure(text="Health Potions: "+str(Bag.healthPotion))
        self.lblStaminaPot.configure(text="Stamina Potions: "+str(Bag.staminaPotion))
        self.lblPHealth.configure(text="Health: "+str(Player.health)+"/"+str(Player.maxHealth))
        self.lblPStamina.configure(text="Stamina: "+str(Player.stamina)+"/"+str(Player.maxStamina))
        
    def updateWeapons(self):
        try:
            self.picMelee = ImageTk.PhotoImage(Image.open(playerWeapons[0][9]))
            self.btnMelee.configure(width=100, height=90, image=self.picMelee)
        except:
            self.btnMelee.configure(width=13, height=6, text=playerWeapons[0][1])
        
        try:
            self.picBow = ImageTk.PhotoImage(Image.open(playerWeapons[1][9]))
            self.btnBow.configure(width=100, height=90, image=self.picBow)
        except:
            self.btnBow.configure(width=13, height=6, text=playerWeapons[1][1])

        try:
            self.picSmallCal = ImageTk.PhotoImage(Image.open(playerWeapons[2][9]))
            self.btnSmallCal.configure(width=100, height=90, image=self.picSmallCal)
        except:
            self.btnSmallCal.configure(width=13, height=6, text=playerWeapons[2][1])

        try:
            self.picMedCal = ImageTk.PhotoImage(Image.open(playerWeapons[3][9]))
            self.btnMedCal.configure(width=100, height=90, image=self.picMedCal)
        except:
            self.btnMedCal.configure(width=13, height=6, text=playerWeapons[3][1])

        try:
            self.picGrenade = ImageTk.PhotoImage(Image.open(playerWeapons[4][9]))
            self.btnGrenade.configure(width=100, height=90, image=self.picGrenade)
        except:
            self.btnGrenade.configure(width=13, height=6, text=playerWeapons[4][1])

        try:
            self.picSpecial = ImageTk.PhotoImage(Image.open(playerWeapons[5][9]))
            self.btnSpecial.configure(width=100, height=90, image=self.picSpecial)
        except:
            self.btnSpecial.configure(width=13, height=6, text=playerWeapons[5][1])
        
        if playerWeapons[0][1] != "":
            self.lblMelee.configure(text=str(playerWeapons[0][2])+" - "+str(playerWeapons[0][3])+"\n\n"+playerWeapons[0][4]+": "+str(playerWeapons[0][5]))
        if playerWeapons[1][1] != "":
            self.lblBow.configure(text=str(playerWeapons[1][2])+" - "+str(playerWeapons[1][3])+"\n\n"+playerWeapons[1][4]+": "+str(playerWeapons[1][5])+"\n"+playerWeapons[1][6]+": "+str(playerWeapons[1][7]))
        if playerWeapons[2][1] != "":    
            self.lblSmallCal.configure(text=str(playerWeapons[2][2])+" - "+str(playerWeapons[2][3])+"\n\n"+playerWeapons[2][6]+": "+str(playerWeapons[2][7]))
        if playerWeapons[3][1] != "":
            self.lblMedCal.configure(text=str(playerWeapons[3][2])+" - "+str(playerWeapons[3][3])+"\n\n"+playerWeapons[3][6]+": "+str(playerWeapons[3][7]))
        if playerWeapons[4][1] != "":
            self.lblGren.configure(text=str(playerWeapons[4][2])+" - "+str(playerWeapons[4][3])+"\n\nCost: "+str(playerWeapons[4][7]))
        if playerWeapons[5][1] != "":
            self.lblSpec.configure(text=str(playerWeapons[5][2])+" - "+str(playerWeapons[5][3])+"\n\nCost: "+str(playerWeapons[5][7]))
        else:
            self.lblSpec.configure(text="")
            self.btnSpecial.configure(image="")

    def updateText(self, text):
        self.fightText.configure(state="normal")
        self.fightText.insert(tk.END, text, "center")
        self.fightText.configure(state="disabled")

    def clearText(self):
        self.fightText.configure(state="normal")
        self.fightText.delete(0.0, "end")
        self.fightText.configure(state="disabled")

class TownPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.townPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.townPage.pack()
        self.townPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.townPage, width=10, height=1, text="Exit", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: self.exit(controller))
        self.btnBack.place(relx=.03, rely=.03)

        # self.lblTownPerson = tk.Label(self.townPage, height=5, width=12, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 25")
        # self.lblTownPerson.place(relx=.075, rely=.05)

        self.lblWelcome = tk.Label(self.townPage, height=1, width=25, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 25", text='"Welcome to the Town!"')
        self.lblWelcome.place(relx=.5, rely=.1, anchor="center")

        # self.lblExit = tk.Label(self.townPage, height=1, width=30, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 10", text="Exiting will return to main menu")
        # self.lblExit.place(relx=.38, rely=.15)

        btnArena = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="Arena", cursor="hand2", font="Arial 25", command=lambda: self.arenaFunction(controller))
        btnArena.place(relx=.5, rely=.3, anchor="center")
        lblArena = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Fight against enemies for gold")
        lblArena.place(relx=.5, rely=.36, anchor="center")

        btnCasino = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="Casino", cursor="hand2", font="Arial 25",command=lambda: controller.showFrame(BlackPage)) #add reset() function for blackPage
        btnCasino.place(relx=.5, rely=.47, anchor="center")
        lblCasino = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Gamble your gold")
        lblCasino.place(relx=.5, rely=.53, anchor="center")

        btnShop = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="Item Shop", cursor="hand2", font="Arial 25", command=lambda: controller.showFrame(ShopPage))
        btnShop.place(relx=.5, rely=.64, anchor="center")
        lblShop = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Shop weapons, armour, ammo, and potions")
        lblShop.place(relx=.5, rely=.7, anchor="center")

        btnSchool = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="School", cursor="hand2", font="Arial 25")
        btnSchool.place(relx=.5, rely=.81, anchor="center")
        lblSchool = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Answer math questions for gold")
        lblSchool.place(relx=.5, rely=.87, anchor="center")
    
    def arenaFunction(self, controller):
        controller.frames[ArenaPage].updateInfo()
        controller.showFrame(ArenaPage)

    def exit(self, controller):
        if GameInfo.mode == 1:
            print("main")
            controller.showFrame(MainPage)
            controller.frames[MainPage].updateInfo()
            GameInfo.nextFunction(controller)
        else:
            controller.showFrame(SplashPage)

class ArenaPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.arenaPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.arenaPage.pack()
        self.arenaPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.arenaPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(TownPage))
        self.btnBack.place(relx=.03, rely=.03)

        lblWelcome = tk.Label(self.arenaPage, height=1, width=25, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 25", text='"Welcome to the Town!"')
        lblWelcome.place(relx=.5, rely=.1, anchor="center")

        self.lblInventory = tk.Label(self.arenaPage, height=18, width=75, bg="black")
        self.lblInventory.place(relx=.05, rely=.5)

        self.lblInvTitle = tk.Label(self.arenaPage, height=1, width=32, bg="black", fg="white", font="Arial 20", text="  "+Player.name + "'s Inventory", anchor='center')
        self.lblInvTitle.place(relx=.05, rely=.525)

        self.lblArrow = tk.Label(self.arenaPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Arrows: "+str(Bag.arrows), anchor='w')
        self.lblArrow.place(relx=.08, rely=.6)

        self.lblSCal = tk.Label(self.arenaPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="9mm Rounds: "+str(Bag.scaliber), anchor='w',)
        self.lblSCal.place(relx=.08, rely=.66)

        self.lblMCal = tk.Label(self.arenaPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="7.62mm Rounds: "+str(Bag.lcaliber), anchor='w')
        self.lblMCal.place(relx=.08, rely=.72)

        self.lblGrenade = tk.Label(self.arenaPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Grenades: "+str(Bag.grenades), anchor='w')
        self.lblGrenade.place(relx=.08, rely=.78)

        self.lblGold = tk.Label(self.arenaPage, height=1, width=12, bg="#6e6c01", fg="white", font="Arial 15", text="Gold: "+str(Bag.gold))
        self.lblGold.place(relx=.05, rely=.84)

        self.lblPHealth = tk.Label(self.arenaPage, height=1, width=18, bg="#751515", fg="white", font="Arial 15", text="Health: "+str(Player.health)+"/"+str(Player.maxHealth))
        self.lblPHealth.place(relx=.175, rely=.84)

        self.lblPStamina = tk.Label(self.arenaPage, height=1, width=17, bg="#157528", fg="white", font="Arial 15", text="Stamina: "+str(Player.stamina)+"/"+str(Player.maxStamina))
        self.lblPStamina.place(relx=.3568, rely=.84)

        self.lblSpecial = tk.Label(self.arenaPage, height=3, width=20, bg="black", fg="white", font="Arial 15", text="Special:\n"+str(playerWeapons[5][1]), anchor='nw', justify="left", wraplength=250, )
        self.lblSpecial.place(relx=.30, rely=.6)

        self.lblHealthPot = tk.Label(self.arenaPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Health Potions: "+str(Bag.healthPotion), anchor='w')
        self.lblHealthPot.place(relx=.30, rely=.72)

        self.lblStaminaPot = tk.Label(self.arenaPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Stamina Potions: "+str(Bag.staminaPotion), anchor='w')
        self.lblStaminaPot.place(relx=.30, rely=.78)

        btnEasy = tk.Button(self.arenaPage, bg="grey", fg="white", height=1, width=20, text="Easy", font="Arial 25", cursor="hand2", command=lambda: self.beginBattle(controller, 1, 2, 50))
        btnEasy.place(relx=.6, rely=.5, anchor="w")
        # lblCasino = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Gamble your gold")
        # lblCasino.place(relx=.5, rely=.53, anchor="center")

        btnMedium = tk.Button(self.arenaPage, bg="grey", fg="white", height=1, width=20, text="Medium", font="Arial 25", cursor="hand2", command=lambda: self.beginBattle(controller, 3, 5, 250))
        btnMedium.place(relx=.6, rely=.65, anchor="w")
        # lblShop = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Shop weapons, armour, ammo, and potions")
        # lblShop.place(relx=.5, rely=.7, anchor="center")

        btnHard = tk.Button(self.arenaPage, bg="grey", fg="white", height=1, width=20, text="Hard", font="Arial 25", cursor="hand2")
        btnHard.place(relx=.6, rely=.8, anchor="w")
        # lblSchool = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Answer math questions for gold")
        # lblSchool.place(relx=.5, rely=.87, anchor="center")

    def beginBattle(self, controller, minLevel, maxLevel, gold):

        controller.showFrame(FightPage)
        controller.frames[FightPage].updateWeapons()
        controller.frames[FightPage].enemyBattle(minLevel, maxLevel, "random", gold)

    def updateInfo(self):
        self.lblArrow.configure(text="Arrows: "+str(Bag.arrows))
        self.lblSCal.configure(text="9mm Rounds: "+str(Bag.scaliber))
        self.lblMCal.configure(text="7.62mm Rounds: "+str(Bag.lcaliber))
        self.lblGrenade.configure(text="Grenades: "+str(Bag.grenades))
        self.lblSpecial.configure(text="Special:\n"+str(playerWeapons[5][1]))
        self.lblHealthPot.configure(text="Health Potions: "+str(Bag.healthPotion))
        self.lblStaminaPot.configure(text="Stamina Potions: "+str(Bag.staminaPotion))
        self.lblGold.configure(text="Gold: "+str(Bag.gold))
        self.lblPHealth.configure(text="Health: "+str(Player.health)+"/"+str(Player.maxHealth))
        self.lblPStamina.configure(text="Stamina: "+str(Player.stamina)+"/"+str(Player.maxStamina))

class ShopPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.shopPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.shopPage.pack()
        self.shopPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        # self.lblTownPerson = tk.Label(self.townPage, height=5, width=12, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 25")
        # self.lblTownPerson.place(relx=.075, rely=.05)

        self.btnBack = tk.Button(self.shopPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: self.backFunction(controller))
        self.btnBack.place(relx=.03, rely=.03)

        self.lblWelcome = tk.Label(self.shopPage, height=1, width=25, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 25", text='"Welcome to the Town!"')
        self.lblWelcome.place(relx=.5, rely=.1, anchor="center")

        # self.lblExit = tk.Label(self.townPage, height=1, width=30, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 10", text="Exiting will return to main menu")
        # self.lblExit.place(relx=.38, rely=.15)

        btnAmmo = tk.Button(self.shopPage, bg="grey", fg="white", height=1, width=20, text="Ammo", font="Arial 25", command=lambda: self.ammoFunction(controller))
        btnAmmo.place(relx=.5, rely=.3, anchor="center")
        lblAmmo = tk.Label(self.shopPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Fight against enemies for gold")
        lblAmmo.place(relx=.5, rely=.36, anchor="center")

        btnArmor = tk.Button(self.shopPage, bg="grey", fg="white", height=1, width=20, text="Armor", font="Arial 25", command=lambda: self.armorFunction(controller))
        btnArmor.place(relx=.5, rely=.47, anchor="center")
        lblArmor = tk.Label(self.shopPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Gamble your gold")
        lblArmor.place(relx=.5, rely=.53, anchor="center")

        btnPotions = tk.Button(self.shopPage, bg="grey", fg="white", height=1, width=20, text="Potions", font="Arial 25", command=lambda: self.potionFunction(controller))
        btnPotions.place(relx=.5, rely=.64, anchor="center")
        lblPotions = tk.Label(self.shopPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Shop weapons, armour, ammo, and potions")
        lblPotions.place(relx=.5, rely=.7, anchor="center")

        btnWeapons = tk.Button(self.shopPage, bg="grey", fg="white", height=1, width=20, text="Weapons", font="Arial 25", command=lambda: self.weaponFunction(controller))
        btnWeapons.place(relx=.5, rely=.81, anchor="center")
        lblWeapons = tk.Label(self.shopPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Answer math questions for gold")
        lblWeapons.place(relx=.5, rely=.87, anchor="center")
    
    def ammoFunction(self, controller):
        controller.frames[AmmoPage].updateInfo()
        controller.showFrame(AmmoPage)

    def armorFunction(self, controller):
        controller.frames[ArmorPage].updateInfo()
        controller.showFrame(ArmorPage)
    
    def potionFunction(self, controller):
        controller.frames[PotionPage].updateInfo()
        controller.showFrame(PotionPage)
    
    def weaponFunction(self, controller):
        controller.showFrame(WeaponPage)

    def backFunction(self, controller):
        if GameInfo.mode == 1 and GameInfo.location == "road":
            controller.showFrame(MainPage)
            controller.frames[MainPage].updateInfo()
            GameInfo.nextFunction(controller)
        else:
            controller.showFrame(TownPage)

class AmmoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.ammoPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.ammoPage.pack()
        self.ammoPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.ammoPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(ShopPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.shopTitle = tk.Label(self.ammoPage, width=15, height=1, font="Arial 25", fg="white", bg="#1a1a1a", text="Ammo Shop")
        self.shopTitle.place(relx=.5, rely=.05, anchor="center")

        self.goldTitle = tk.Label(self.ammoPage, width = 32,height=1, bg="#1a1a1a", fg="gold", font="Arial 20",highlightbackground="black",highlightthickness=3, text="Gold: "+str(Bag.gold))
        self.goldTitle.place(relx=.03, rely=.12)

        self.shopBorder = tk.Label(self.ammoPage, width = 32,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.shopBorder.place(relx=.03, rely=.17)

        self.btnArrow = tk.Button(self.ammoPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseAmmo(0))
        self.btnArrow.place(relx=.11, rely=.2)
        try:
            self.picArrow = ImageTk.PhotoImage(Image.open(ammoList[0][3]))
            self.btnArrow.configure(width=100, height=90, image=self.picArrow)
        except:
            self.btnArrow.configure(width=13, height=6, text=ammoList[0][0])

        self.lblArrowQuant = tk.Label(self.ammoPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Quantity: "+str(ammoList[0][1]))
        self.lblArrowQuant.place(relx=.24, rely=.218)
        self.lblArrowCost = tk.Label(self.ammoPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(ammoList[0][2])+" gold")
        self.lblArrowCost.place(relx=.24, rely=.268)
        self.lblArrowName = tk.Label(self.ammoPage, width = 9, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text="Arrows")
        self.lblArrowName.place(relx=.113, rely=.33)


        self.btnSCal = tk.Button(self.ammoPage, bg="#909090",text="9mm Rounds", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseAmmo(1))
        self.btnSCal.place(relx=.11, rely=.4)
        try:
            self.picSCal = ImageTk.PhotoImage(Image.open(ammoList[1][3]))
            self.btnSCal.configure(width=100, height=90, image=self.picSCal)
        except:
            self.btnSCal.configure(width=13, height=6, text=ammoList[1][0])
        self.lblSCalQuant = tk.Label(self.ammoPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Quantity: "+str(ammoList[1][1]))
        self.lblSCalQuant.place(relx=.24, rely=.418)
        self.lblSCalCost = tk.Label(self.ammoPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(ammoList[1][2])+" gold")
        self.lblSCalCost.place(relx=.24, rely=.468)

        self.lblSCalName = tk.Label(self.ammoPage, width = 9, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text="9mm")
        self.lblSCalName.place(relx=.113, rely=.53)

        self.btnMCal = tk.Button(self.ammoPage, bg="#909090",text="7.62 Rounds", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseAmmo(2))
        self.btnMCal.place(relx=.11, rely=.6)

        try:
            self.picMCal = ImageTk.PhotoImage(Image.open(ammoList[2][3]))
            self.btnMCal.configure(width=100, height=90, image=self.picMCal)
        except:
            self.btnMCal.configure(width=13, height=6, text=ammoList[2][0])

        self.lblMCalQuant = tk.Label(self.ammoPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Quantity: "+str(ammoList[2][1]))
        self.lblMCalQuant.place(relx=.24, rely=.618)
        self.lblMCalCost = tk.Label(self.ammoPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(ammoList[2][2])+" gold")
        self.lblMCalCost.place(relx=.24, rely=.668)
        self.lblMCalName = tk.Label(self.ammoPage, width = 9, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text="7.62mm")
        self.lblMCalName.place(relx=.113, rely=.73)

        self.btnGrenades = tk.Button(self.ammoPage, bg="#909090",text="Grenades", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseAmmo(3))
        self.btnGrenades.place(relx=.11, rely=.8)

        try:
            self.picGrenades = ImageTk.PhotoImage(Image.open(ammoList[3][3]))
            self.btnGrenades.configure(width=100, height=90, image=self.picGrenades)
        except:
            self.btnGrenades.configure(width=13, height=6, text=ammoList[3][0])

        self.lblGrenadesQuant = tk.Label(self.ammoPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Quantity: "+str(ammoList[3][1]))
        self.lblGrenadesQuant.place(relx=.24, rely=.818)
        self.lblGrenadesCost = tk.Label(self.ammoPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(ammoList[3][2])+" gold")
        self.lblGrenadesCost.place(relx=.24, rely=.868)
        self.lblGrenadesName = tk.Label(self.ammoPage, width = 9, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text="Grenades")
        self.lblGrenadesName.place(relx=.113, rely=.93)

        self.inventoryTitle = tk.Label(self.ammoPage, width = 32,height=1, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Inventory")
        self.inventoryTitle.place(relx=.49, rely=.12)

        self.inventory = tk.Label(self.ammoPage, width = 32,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.inventory.place(relx=.49, rely=.17)

        self.lblBowPic = tk.Label(self.ammoPage, bg="#909090", highlightthickness=5, highlightbackground="black")
        self.lblBowPic.place(relx=.57, rely=.2)
        self.lblBowAmt = tk.Label(self.ammoPage, width = 25, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Arrow Count: "+str(Bag.arrows))
        self.lblBowAmt.place(relx=.70, rely=.243)
        self.lblBowName = tk.Label(self.ammoPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=playerWeapons[1][1])
        self.lblBowName.place(relx=.554, rely=.335)

        self.lblSCalPic = tk.Label(self.ammoPage, bg="#909090", highlightthickness=5, highlightbackground="black")
        self.lblSCalPic.place(relx=.57, rely=.4)
        self.lblSCalAmt = tk.Label(self.ammoPage, width = 25, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",anchor="w", text="9mm Rounds: "+str(Bag.scaliber))
        self.lblSCalAmt.place(relx=.70, rely=.443)
        self.lblSCalGunName = tk.Label(self.ammoPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=playerWeapons[2][1])
        self.lblSCalGunName.place(relx=.554, rely=.535)

        self.lblMCalPic = tk.Label(self.ammoPage, bg="#909090", highlightthickness=5, highlightbackground="black")
        self.lblMCalPic.place(relx=.57, rely=.6)
        self.lblMCalAmt = tk.Label(self.ammoPage, width = 25, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",anchor="w", text="7.62mm Rounds: "+str(Bag.lcaliber))
        self.lblMCalAmt.place(relx=.70, rely=.643)
        self.lblMCalGunName = tk.Label(self.ammoPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=playerWeapons[3][1])
        self.lblMCalGunName.place(relx=.554, rely=.735)

        self.lblGrenadesPic = tk.Label(self.ammoPage, bg="#909090", highlightthickness=5, highlightbackground="black", text=playerWeapons[4][1])
        self.lblGrenadesPic.place(relx=.57, rely=.8)
        self.lblGrenadesAmt = tk.Label(self.ammoPage, width = 25, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Grenades: "+str(Bag.grenades))
        self.lblGrenadesAmt.place(relx=.70, rely=.843)
        self.lblGrenadesGunName = tk.Label(self.ammoPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text="Grenade")
        self.lblGrenadesGunName.place(relx=.554, rely=.935)

    def purchaseAmmo(self, index):
        self.updateClearColor()
        if Bag.gold < ammoList[index][2]:
            if index == 0:
                self.lblArrowCost.configure(fg="#fa6c61")
            elif index == 1:
                self.lblSCalCost.configure(fg="#fa6c61")
            elif index == 2:
                self.lblMCalCost.configure(fg="#fa6c61")
            elif index == 3:
                self.lblGrenadesCost.configure(fg="#fa6c61")
        else:
            Bag.gold -= ammoList[index][2]
            GameInfo.goldSpent+=ammoList[index][2]
            if index == 0:
                Bag.arrows += ammoList[index][1]
            elif index == 1:
                Bag.scaliber += ammoList[index][1]
            elif index == 2:
                Bag.lcaliber += ammoList[index][1]
            elif index == 3:
                Bag.grenades += ammoList[index][1]
            self.goldTitle.configure(text="Gold: "+str(Bag.gold))
            self.updateAmmoCount()
        
    def updateClearColor(self):
        self.lblArrowCost.configure(fg="white")
        self.lblSCalCost.configure(fg="white")
        self.lblMCalCost.configure(fg="white")
        self.lblGrenadesCost.configure(fg="white")
    
    def updateAmmoCount(self):
        self.lblBowAmt.configure(text="Arrow Count: "+str(Bag.arrows))
        self.lblSCalAmt.configure(text="9mm Rounds: "+str(Bag.scaliber))
        self.lblMCalAmt.configure(text="7.62mm Rounds: "+str(Bag.lcaliber))
        self.lblGrenadesAmt.configure(text="Grenades: "+str(Bag.grenades))

    def updateInfo(self):
        self.goldTitle.configure(text="Gold: "+str(Bag.gold))
        self.updateAmmoCount()
        self.updateClearColor()
        try:
            self.picBow = ImageTk.PhotoImage(Image.open(playerWeapons[1][9]))
            self.lblBowPic.configure(width=100, height=90, image=self.picBow)
        except:
            if playerWeapons[1][1] == "":
                self.lblBowPic.configure(width=14, height=6, text="Empty Slot", image="")
            else:
                self.lblBowPic.configure(width=14, height=6, text="Image",image="")
        self.lblBowName.configure(text=playerWeapons[1][1])

        try:
            self.picSCalGun = ImageTk.PhotoImage(Image.open(playerWeapons[2][9]))
            self.lblSCalPic.configure(width=100, height=90, image=self.picSCalGun)
        except:
            if playerWeapons[2][1] == "":
                self.lblSCalPic.configure(width=14, height=6, text="Empty Slot",image="")
            else:
                self.lblSCalPic.configure(width=14, height=6, text="Image",image="")
        self.lblSCalGunName.configure(text=playerWeapons[2][1])

        try:
            self.picMCalGun = ImageTk.PhotoImage(Image.open(playerWeapons[3][9]))
            self.lblMCalPic.configure(width=100, height=90, image=self.picMCalGun)
        except:
            if playerWeapons[3][1] == "":
                self.lblMCalPic.configure(width=14, height=6, text="Empty Slot",image="")
            else:
                self.lblMCalPic.configure(width=14, height=6, text="Image",image="")
        self.lblMCalGunName.configure(text=playerWeapons[3][1])

        try:
            self.picGrenadesGun = ImageTk.PhotoImage(Image.open(playerWeapons[4][9]))
            self.lblGrenadesPic.configure(width=100, height=90, image=self.picGrenadesGun)
        except:
            self.lblGrenadesPic.configure(width=14, height=6, text="Image")

class ArmorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.armorPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.armorPage.pack()
        self.armorPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.armorPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(ShopPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.shopTitle = tk.Label(self.armorPage, width=15, height=1, font="Arial 25", fg="white", bg="#1a1a1a", text="Armor Shop")
        self.shopTitle.place(relx=.5, rely=.05, anchor="center")

        self.goldTitle = tk.Label(self.armorPage, width = 46,height=1, bg="#1a1a1a", fg="gold", font="Arial 20",highlightbackground="black",highlightthickness=3, text="Gold: "+str(Bag.gold))
        self.goldTitle.place(relx=.03, rely=.12)

        self.shopBorder = tk.Label(self.armorPage, width = 46,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.shopBorder.place(relx=.03, rely=.17)

        self.inventoryTitle = tk.Label(self.armorPage, width = 18,height=1, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Inventory")
        self.inventoryTitle.place(relx=.695, rely=.12)

        self.inventoryBorder = tk.Label(self.armorPage, width = 18,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.inventoryBorder.place(relx=.695, rely=.17)

        self.btnHide = tk.Button(self.armorPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.buyArmor(0))
        self.btnHide.place(relx=.075, rely=.25)

        try:
            self.picHide = ImageTk.PhotoImage(Image.open(armorList[0][3]))
            self.btnHide.configure(width=150, height=160, image=self.picHide)
        except:
            self.btnHide.configure(width=13, height=6, font="Arial 15", text="Image")

        self.lblHideName = tk.Label(self.armorPage, width = 12, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Hide")
        self.lblHideName.place(relx=.074, rely=.2)
        self.lblHideHealth = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="+"+str(armorList[0][1])+" Health")
        self.lblHideHealth.place(relx=.0675, rely=.47)
        self.lblHideCost = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="Cost: "+str(armorList[0][2])+" gold")
        self.lblHideCost.place(relx=.0675, rely=.51)
        


        self.btnLeather = tk.Button(self.armorPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.buyArmor(1))
        self.btnLeather.place(relx=.2855, rely=.25)

        try:
            self.picLeather = ImageTk.PhotoImage(Image.open(armorList[1][3]))
            self.btnLeather.configure(width=150, height=160, image=self.picLeather)
        except:
            self.btnLeather.configure(width=13, height=6, font="Arial 15", text="Image")
        self.lblLeatherName = tk.Label(self.armorPage, width = 12, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Leather")
        self.lblLeatherName.place(relx=.282, rely=.2)
        self.lblLeatherHealth = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="+"+str(armorList[1][1])+" Health")
        self.lblLeatherHealth.place(relx=.278, rely=.47)
        self.lblLeatherCost = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="Cost: "+str(armorList[1][2])+" gold")
        self.lblLeatherCost.place(relx=.278, rely=.51)

        self.btnChain = tk.Button(self.armorPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.buyArmor(2))
        self.btnChain.place(relx=.495, rely=.25)

        try:
            self.picChain = ImageTk.PhotoImage(Image.open(armorList[2][3]))
            self.btnChain.configure(width=150, height=160, image=self.picChain)
        except:
            self.btnChain.configure(width=13, height=6,font="Arial 15", text="Image")
        self.lblChainName = tk.Label(self.armorPage, width = 12, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Chainmail")
        self.lblChainName.place(relx=.492, rely=.2)
        self.lblChainHealth = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="+"+str(armorList[2][1])+" Health")
        self.lblChainHealth.place(relx=.488, rely=.47)
        self.lblChainCost = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="Cost: "+str(armorList[2][2])+" gold")
        self.lblChainCost.place(relx=.488, rely=.51)


        self.btnSteel = tk.Button(self.armorPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.buyArmor(3))
        self.btnSteel.place(relx=.075, rely=.66)
        try:
            self.picSteel = ImageTk.PhotoImage(Image.open(armorList[3][3]))
            self.btnSteel.configure(width=150, height=160, image=self.picSteel)
        except:
            self.btnSteel.configure(width=13, height=6,font="Arial 15", text="Image")
        self.lblSteelName = tk.Label(self.armorPage, width = 12, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Steel")
        self.lblSteelName.place(relx=.074, rely=.61)
        self.lblSteelHealth = tk.Label(self.armorPage, width = 15, height=1, bg="#1a1a1a", fg="white", font="Arial 15",justify="left", text="+"+str(armorList[3][1])+" Health")
        self.lblSteelHealth.place(relx=.0675, rely=.88)
        self.lblSteelCost = tk.Label(self.armorPage, width = 15, height=1, bg="#1a1a1a", fg="white", font="Arial 15",justify="left", text="Cost: "+str(armorList[3][2])+" gold")
        self.lblSteelCost.place(relx=.0675, rely=.92)

        self.btnKevlar = tk.Button(self.armorPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.buyArmor(4))
        self.btnKevlar.place(relx=.2855, rely=.66)

        try:
            self.picKevlar = ImageTk.PhotoImage(Image.open(armorList[4][3]))
            self.btnKevlar.configure(width=150, height=160, image=self.picKevlar)
        except:
            self.btnKevlar.configure(width=13, height=6,font="Arial 15", text="Image")
        self.lblKevlarName = tk.Label(self.armorPage, width = 12, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Light Kevlar")
        self.lblKevlarName.place(relx=.282, rely=.61)
        self.lblKevlarHealth = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="+"+str(armorList[4][1])+" Health")
        self.lblKevlarHealth.place(relx=.278, rely=.88)
        self.lblKevlarCost = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="Cost: "+str(armorList[4][2])+" gold")
        self.lblKevlarCost.place(relx=.278, rely=.92)

        self.btnHeavyKevlar = tk.Button(self.armorPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.buyArmor(5))
        self.btnHeavyKevlar.place(relx=.495, rely=.66)

        try:
            self.picHeavyKevlar = ImageTk.PhotoImage(Image.open(armorList[5][3]))
            self.btnHeavyKevlar.configure(width=150, height=160, image=self.picHeavyKevlar)
        except:
            self.btnHeavyKevlar.configure(width=13, height=6,font="Arial 15", text="Image")
        self.lblHeavyKevlarName = tk.Label(self.armorPage, width = 12, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Heavy Kevlar")
        self.lblHeavyKevlarName.place(relx=.492, rely=.61)
        self.lblHeavyKevlarHealth = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="+"+str(armorList[5][1])+" Health")
        self.lblHeavyKevlarHealth.place(relx=.488, rely=.88)
        self.lblHeavyKevlarCost = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="Cost: "+str(armorList[5][2])+" gold")
        self.lblHeavyKevlarCost.place(relx=.488, rely=.92)

        self.lblPlayer = tk.Label(self.armorPage, bg="#909090",highlightthickness=5, highlightbackground="black")
        self.lblPlayer.place(relx=.765, rely=.25)

        try:
            self.picPlayer = ImageTk.PhotoImage(Image.open(Armor.image))
            self.lblPlayer.configure(width=150, height=160, image=self.picPlayer)
        except:
            self.lblPlayer.configure(width=13, height=6,font="Arial 15")

        self.lblPlayerArmor = tk.Label(self.armorPage, width = 12, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text=Armor.name)
        self.lblPlayerArmor.place(relx=.762, rely=.2)
        self.lblPlayerArmorHealth = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="+"+str(Armor.healthBonus)+" Health")
        self.lblPlayerArmorHealth.place(relx=.758, rely=.475)
        self.lblHealth = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text=Player.name+"'s Health: ")
        self.lblHealth.place(relx=.758, rely=.7)
        self.lblPHealth = tk.Label(self.armorPage, height=1, width=20, bg="#751515", fg="white", font="Arial 15", text=str(Player.health)+" / "+str(Player.maxHealth))
        self.lblPHealth.place(relx=.73, rely=.75)

        self.lblInvalid = tk.Label(self.armorPage, width = 24, height=2, bg="#1a1a1a", fg="#fa6c61", font="Arial 15")
        self.lblInvalid.place(relx=.71, rely=.57)
    
    def buyArmor(self, index):
        self.updateClearColor()
        self.lblInvalid.configure(text="")
        if Armor.healthBonus > armorList[index][1]:
            self.lblInvalid.configure(text="Current armour is superior")
        elif Armor.healthBonus == armorList[index][1]:
            self.lblInvalid.configure(text="Already equipped")
        elif Bag.gold < armorList[index][2]:
            if index == 0:
                self.lblHideCost.configure(fg="gold")
            if index == 1:
                self.lblLeatherCost.configure(fg="gold")
            if index == 2:
                self.lblChainCost.configure(fg="gold")
            if index == 3:
                self.lblSteelCost.configure(fg="gold")
            if index == 4:
                self.lblKevlarCost.configure(fg="gold")
            if index == 5:
                self.lblHeavyKevlarCost.configure(fg="gold")
        else:
            Armor.name = armorList[index][0]
            Armor.healthBonus = armorList[index][1]
            Armor.goldCost = armorList[index][2]
            Armor.image = armorList[index][3]
            Player.armor = Armor.healthBonus
            Player.maxHealth = Player.totalHealth()
            Player.health = Player.maxHealth
            Bag.gold -= Armor.goldCost
            GameInfo.goldSpent+=Armor.goldCost
            self.updateInfo()
        
    def updateClearColor(self):
        self.lblHideCost.configure(fg="white")
        self.lblLeatherCost.configure(fg="white")
        self.lblChainCost.configure(fg="white")
        self.lblSteelCost.configure(fg="white")
        self.lblKevlarCost.configure(fg="white")
        self.lblHeavyKevlarCost.configure(fg="white")

    def updateInfo(self):
        self.lblInvalid.configure(text="")
        self.updateClearColor()
        self.goldTitle.configure(text="Gold: "+str(Bag.gold))
        try:
            self.picPlayer = ImageTk.PhotoImage(Image.open(Armor.image))
            self.lblPlayer.configure(width=150, height=160, image=self.picPlayer)
        except:
            self.lblPlayer.configure(width=13, height=7,font="Arial 15", text="No Armor")
        self.lblPlayerArmor.configure(text=Armor.name)
        self.lblPlayerArmorHealth.configure(text="+"+str(Armor.healthBonus)+" Health")
        self.lblHealth.configure(text=Player.name+"'s Health: ")
        self.lblPHealth.configure(text=str(Player.health)+" / "+str(Player.maxHealth))

class PotionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.potionPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.potionPage.pack()
        self.potionPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.potionPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(ShopPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.shopTitle = tk.Label(self.potionPage, width=15, height=1, font="Arial 25", fg="white", bg="#1a1a1a", text="Potion Shop")
        self.shopTitle.place(relx=.5, rely=.05, anchor="center")

        self.goldTitle = tk.Label(self.potionPage, width = 30,height=1, bg="#1a1a1a", fg="gold", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Gold: "+str(Bag.gold))
        self.goldTitle.place(relx=.1, rely=.12)

        self.shopBorder = tk.Label(self.potionPage, width = 30,height=19, bg="#1a1a1a", fg="white", font="Arial 20", highlightbackground="black", highlightthickness=3)
        self.shopBorder.place(relx=.1, rely=.17)

        self.btnHealth = tk.Button(self.potionPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchasePotion(0))
        self.btnHealth.place(relx=.186, rely=.35)
        try:
            self.picHealth = ImageTk.PhotoImage(Image.open(potionList[0][3]))
            self.btnHealth.configure(width=100, height=100, image=self.picHealth)
        except:
            self.btnHealth.configure(width=13, height=6, text=potionList[0][0])
            
        self.lblHealthName = tk.Label(self.potionPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Health Potion")
        self.lblHealthName.place(relx=.146, rely=.28)
        self.lblHealthBonus = tk.Label(self.potionPage, width = 20, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Health Points: +"+str(potionList[0][1]))
        self.lblHealthBonus.place(relx=.316, rely=.38)
        self.lblHealthCost = tk.Label(self.potionPage, width = 20, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(potionList[0][2])+" gold")
        self.lblHealthCost.place(relx=.316, rely=.43)

        self.btnStamina = tk.Button(self.potionPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchasePotion(1))
        self.btnStamina.place(relx=.186, rely=.66)
        try:
            self.picStamina = ImageTk.PhotoImage(Image.open(potionList[1][3]))
            self.btnStamina.configure(width=100, height=100, image=self.picStamina)
        except:
            self.btnStamina.configure(width=13, height=6, text=potionList[1][0])
            
        self.lblStaminaName = tk.Label(self.potionPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Stamina Potion")
        self.lblStaminaName.place(relx=.146, rely=.59)
        self.lblStaminaBonus = tk.Label(self.potionPage, width = 20, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina Points: +"+str(potionList[1][1]))
        self.lblStaminaBonus.place(relx=.316, rely=.69)
        self.lblStaminaCost = tk.Label(self.potionPage, width = 20, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(potionList[1][2])+" gold")
        self.lblStaminaCost.place(relx=.316, rely=.74)

        self.inventoryTitle = tk.Label(self.potionPage, width = 24,height=1, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Inventory")
        self.inventoryTitle.place(relx=.54, rely=.12)

        self.inventoryBorder = tk.Label(self.potionPage, width = 24,height=19, bg="#1a1a1a", fg="white", font="Arial 20", highlightbackground="black", highlightthickness=3)
        self.inventoryBorder.place(relx=.54, rely=.17)

        self.lblPlayerHealthPotion = tk.Label(self.potionPage, width = 20, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Health Potions:   "+str(Bag.healthPotion))
        self.lblPlayerHealthPotion.place(relx=.6, rely=.4)

        self.lblPlayerStaminaPotion = tk.Label(self.potionPage, width = 20, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text="Stamina Potions:   "+str(Bag.staminaPotion))
        self.lblPlayerStaminaPotion.place(relx=.6, rely=.71)

    def purchasePotion(self, index):
        self.updateClearRed()
        if Bag.gold < potionList[index][2]:
            if index == 0:
                self.lblHealthCost.configure(fg="gold")
            elif index == 1: 
                self.lblStaminaCost.configure(fg="gold")
        else:
            Bag.gold -= potionList[index][2]
            GameInfo.goldSpent+=potionList[index][2]
            if index == 0:
                Bag.healthPotion += 1
            elif index == 1: 
                Bag.staminaPotion += 1
            self.updateInfo()
    
    def updateClearRed(self):
        self.lblHealthCost.configure(fg="white")
        self.lblStaminaCost.configure(fg="white")

    def updateInfo(self):
        self.updateClearRed()
        self.goldTitle.configure(text=Player.name+"'s Gold: "+str(Bag.gold))
        self.lblPlayerHealthPotion.configure(text="Health Potions:   "+str(Bag.healthPotion))
        self.lblPlayerStaminaPotion.configure(text="Stamina Potions:   "+str(Bag.staminaPotion))

class WeaponPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.weaponPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.weaponPage.pack()
        self.weaponPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.weaponPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(ShopPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.lblTitle = tk.Label(self.weaponPage, height=1, width=25, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 25", text='Weapon Shop')
        self.lblTitle.place(relx=.5, rely=.1, anchor="center")

        btnMelee = tk.Button(self.weaponPage, bg="grey", fg="white", height=1, width=20, text="Melee", font="Arial 25", command=lambda: self.meleeFunction(controller))
        btnMelee.place(relx=.5, rely=.25, anchor="center")

        btnArchery = tk.Button(self.weaponPage, bg="grey", fg="white", height=1, width=20, text="Archery", font="Arial 25", command=lambda: self.archeryFunction(controller))
        btnArchery.place(relx=.5, rely=.40, anchor="center")

        btnSCal = tk.Button(self.weaponPage, bg="grey", fg="white", height=1, width=20, text="Sidearms", font="Arial 25", command=lambda: self.sidearmFunction(controller))
        btnSCal.place(relx=.5, rely=.55, anchor="center")
        
        btnMCal = tk.Button(self.weaponPage, bg="grey", fg="white", height=1, width=20, text="Rifles", font="Arial 25", command=lambda: self.rifleFunction(controller))
        btnMCal.place(relx=.5, rely=.70, anchor="center")

        btnSpecial = tk.Button(self.weaponPage, bg="grey", fg="white", height=1, width=20, text="Special", font="Arial 25", command=lambda: self.specialFunction(controller))
        btnSpecial.place(relx=.5, rely=.85, anchor="center")
    
    def meleeFunction(self, controller):
        controller.frames[MeleePage].updateInfo()
        controller.showFrame(MeleePage)

    def archeryFunction(self, controller):
        controller.frames[ArcheryPage].updateInfo()
        controller.showFrame(ArcheryPage)
    
    def sidearmFunction(self, controller):
        controller.frames[SidearmPage].updateInfo()
        controller.showFrame(SidearmPage)

    def rifleFunction(self, controller):
        controller.frames[RiflePage].updateInfo()
        controller.showFrame(RiflePage)

    def specialFunction(self, controller):
        controller.frames[SpecialPage].updateInfo()
        controller.showFrame(SpecialPage)
        
class MeleePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.meleePage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.meleePage.pack()
        self.meleePage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.meleePage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(WeaponPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.shopTitle = tk.Label(self.meleePage, width=15, height=1, font="Arial 25", fg="white", bg="#1a1a1a", text="Melee Department")
        self.shopTitle.place(relx=.5, rely=.05, anchor="center")

        self.goldTitle = tk.Label(self.meleePage, width = 44,height=1, bg="#1a1a1a", fg="gold", font="Arial 20",highlightbackground="black",highlightthickness=3, text="Gold: "+str(Bag.gold))
        self.goldTitle.place(relx=.03, rely=.12)

        self.shopBorder = tk.Label(self.meleePage, width = 44,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.shopBorder.place(relx=.03, rely=.17)

        self.btnStick = tk.Button(self.meleePage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(0))
        self.btnStick.place(relx=.07, rely=.2)
        try:
            self.picStick = ImageTk.PhotoImage(Image.open(weapons_list[0][9]))
            self.btnStick.configure(width=100, height=90, image=self.picStick)
        except:
            self.btnStick.configure(width=13, height=6, text=weapons_list[0][1])

        self.lblStickDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[0][2])+" - "+str(weapons_list[0][3]))
        self.lblStickDamage.place(relx=.19, rely=.203)
        self.lblStickStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[0][5]))
        self.lblStickStam.place(relx=.19, rely=.243)
        self.lblStickCost = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[0][8])+" gold")
        self.lblStickCost.place(relx=.19, rely=.283)
        self.lblStickName = tk.Label(self.meleePage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[0][1])
        self.lblStickName.place(relx=.064, rely=.333)


        self.btnKnife = tk.Button(self.meleePage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(1))
        self.btnKnife.place(relx=.07, rely=.4)
        try:
            self.picKnife = ImageTk.PhotoImage(Image.open(weapons_list[1][9]))
            self.btnKnife.configure(width=100, height=90, image=self.picKnife)
        except:
            self.btnKnife.configure(width=13, height=6, text=weapons_list[1][1])

        self.lblKnifeDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[1][2])+" - "+str(weapons_list[1][3]))
        self.lblKnifeDamage.place(relx=.19, rely=.403)
        self.lblKnifeStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[1][5]))
        self.lblKnifeStam.place(relx=.19, rely=.443)
        self.lblKnifeCost = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[1][8])+" gold")
        self.lblKnifeCost.place(relx=.19, rely=.483)
        self.lblKnifeName = tk.Label(self.meleePage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[1][1])
        self.lblKnifeName.place(relx=.064, rely=.533)

        self.btnBat = tk.Button(self.meleePage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(2))
        self.btnBat.place(relx=.07, rely=.6)
        try:
            self.picBat = ImageTk.PhotoImage(Image.open(weapons_list[2][9]))
            self.btnBat.configure(width=100, height=90, image=self.picBat)
        except:
            self.btnBat.configure(width=13, height=6, text=weapons_list[2][1])

        self.lblBatDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[2][2])+" - "+str(weapons_list[2][3]))
        self.lblBatDamage.place(relx=.19, rely=.603)
        self.lblBatStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[2][5]))
        self.lblBatStam.place(relx=.19, rely=.643)
        self.lblBatCost = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[2][8])+" gold")
        self.lblBatCost.place(relx=.19, rely=.683)
        self.lblBatName = tk.Label(self.meleePage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[2][1])
        self.lblBatName.place(relx=.064, rely=.733)

        self.btnMachete = tk.Button(self.meleePage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(3))
        self.btnMachete.place(relx=.07, rely=.8)
        try:
            self.picMachete = ImageTk.PhotoImage(Image.open(weapons_list[3][9]))
            self.btnMachete.configure(width=100, height=90, image=self.picMachete)
        except:
            self.btnMachete.configure(width=13, height=6, text=weapons_list[3][1])

        self.lblMacheteDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[3][2])+" - "+str(weapons_list[3][3]))
        self.lblMacheteDamage.place(relx=.19, rely=.803)
        self.lblMacheteStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[3][5]))
        self.lblMacheteStam.place(relx=.19, rely=.843)
        self.lblMacheteCost = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[3][8])+" gold")
        self.lblMacheteCost.place(relx=.19, rely=.883)
        self.lblMacheteName = tk.Label(self.meleePage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[3][1])
        self.lblMacheteName.place(relx=.064, rely=.933)

        self.btnSpear = tk.Button(self.meleePage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(4))
        self.btnSpear.place(relx=.37, rely=.2)
        try:
            self.picSpear = ImageTk.PhotoImage(Image.open(weapons_list[4][9]))
            self.btnSpear.configure(width=100, height=90, image=self.picSpear)
        except:
            self.btnSpear.configure(width=13, height=6, text=weapons_list[4][1])

        self.lblSpearDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[4][2])+" - "+str(weapons_list[4][3]))
        self.lblSpearDamage.place(relx=.49, rely=.203)
        self.lblSpearStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[4][5]))
        self.lblSpearStam.place(relx=.49, rely=.243)
        self.lblSpearCost = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[4][8])+" gold")
        self.lblSpearCost.place(relx=.49, rely=.283)
        self.lblSpearName = tk.Label(self.meleePage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[4][1])
        self.lblSpearName.place(relx=.364, rely=.333)

        self.btnAxe = tk.Button(self.meleePage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(5))
        self.btnAxe.place(relx=.37, rely=.4)
        try:
            self.picAxe = ImageTk.PhotoImage(Image.open(weapons_list[5][9]))
            self.btnAxe.configure(width=100, height=90, image=self.picAxe)
        except:
            self.btnAxe.configure(width=13, height=6, text=weapons_list[5][1])

        self.lblAxeDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[5][2])+" - "+str(weapons_list[5][3]))
        self.lblAxeDamage.place(relx=.49, rely=.403)
        self.lblAxeStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[5][5]))
        self.lblAxeStam.place(relx=.49, rely=.443)
        self.lblAxeCost = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[5][8])+" gold")
        self.lblAxeCost.place(relx=.49, rely=.483)
        self.lblAxeName = tk.Label(self.meleePage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[5][1])
        self.lblAxeName.place(relx=.364, rely=.533)

        self.btnSword = tk.Button(self.meleePage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(6))
        self.btnSword.place(relx=.37, rely=.6)
        try:
            self.picSword = ImageTk.PhotoImage(Image.open(weapons_list[6][9]))
            self.btnSword.configure(width=100, height=90, image=self.picSword)
        except:
            self.btnSword.configure(width=13, height=6, text=weapons_list[6][1])

        self.lblSwordDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[6][2])+" - "+str(weapons_list[6][3]))
        self.lblSwordDamage.place(relx=.49, rely=.603)
        self.lblSwordStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[6][5]))
        self.lblSwordStam.place(relx=.49, rely=.643)
        self.lblSwordCost = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[6][8])+" gold")
        self.lblSwordCost.place(relx=.49, rely=.683)
        self.lblSwordName = tk.Label(self.meleePage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[6][1])
        self.lblSwordName.place(relx=.364, rely=.733)

        self.btnHammer = tk.Button(self.meleePage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(7))
        self.btnHammer.place(relx=.37, rely=.8)
        try:
            self.picHammer = ImageTk.PhotoImage(Image.open(weapons_list[7][9]))
            self.btnHammer.configure(width=100, height=90, image=self.picHammer)
        except:
            self.btnHammer.configure(width=13, height=6, text=weapons_list[7][1])

        self.lblHammerDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[7][2])+" - "+str(weapons_list[7][3]))
        self.lblHammerDamage.place(relx=.49, rely=.803)
        self.lblHammerStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[7][5]))
        self.lblHammerStam.place(relx=.49, rely=.843)
        self.lblHammerCost = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[7][8])+" gold")
        self.lblHammerCost.place(relx=.49, rely=.883)
        self.lblHammerName = tk.Label(self.meleePage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[7][1])
        self.lblHammerName.place(relx=.364, rely=.933)

        self.inventoryTitle = tk.Label(self.meleePage, width = 20,height=1, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Inventory")
        self.inventoryTitle.place(relx=.666, rely=.12)

        self.inventory = tk.Label(self.meleePage, width = 20,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.inventory.place(relx=.666, rely=.17)

        self.lblmeleePic = tk.Label(self.meleePage, bg="#909090", highlightthickness=5, highlightbackground="black")
        self.lblmeleePic.place(relx=.765, rely=.3)
        self.lblmeleeDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblmeleeDamage.place(relx=.729, rely=.45)
        self.lblmeleeStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblmeleeStam.place(relx=.729, rely=.5)
        self.lblmeleeName = tk.Label(self.meleePage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 18")
        self.lblmeleeName.place(relx=.73, rely=.23)

        self.lblStamina = tk.Label(self.meleePage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="Stamina:")
        self.lblStamina.place(relx=.745, rely=.7)
        self.lblPStamina = tk.Label(self.meleePage, height=1, width=20, bg="#157528", fg="white", font="Arial 15")
        self.lblPStamina.place(relx=.715, rely=.76)

    def purchaseMelee(self, index):
        self.updateClearColor()
        if playerWeapons[0][1] == weapons_list[index][1]:
            self.lblmeleeName.configure(fg="#157528")
        elif Bag.gold < weapons_list[index][8]:
            if index == 0:
                self.lblStickCost.configure(fg="gold")
            elif index == 1:
                self.lblKnifeCost.configure(fg="gold")
            elif index == 2:
                self.lblBatCost.configure(fg="gold")
            elif index == 3:
                self.lblMacheteCost.configure(fg="gold")
            elif index == 4:
                self.lblSpearCost.configure(fg="gold")
            elif index == 5:
                self.lblAxeCost.configure(fg="gold")
            elif index == 6:
                self.lblSwordCost.configure(fg="gold")
            elif index == 7:
                self.lblHammerCost.configure(fg="gold")
        else:
            Bag.gold -= weapons_list[index][8]
            GameInfo.goldSpent+=weapons_list[index][8]
            playerWeapons[0] = weapons_list[index]
            self.updateInfo()

    def updateClearColor(self):
        self.lblStickCost.configure(fg="white")
        self.lblKnifeCost.configure(fg="white")
        self.lblBatCost.configure(fg="white")
        self.lblMacheteCost.configure(fg="white")
        self.lblSpearCost.configure(fg="white")
        self.lblAxeCost.configure(fg="white")
        self.lblSwordCost.configure(fg="white")
        self.lblHammerCost.configure(fg="white")
        self.lblmeleeName.configure(fg="white")

    def updateInfo(self):
        self.goldTitle.configure(text="Gold: "+str(Bag.gold))
        self.updateClearColor()
        try:
            self.picmelee = ImageTk.PhotoImage(Image.open(playerWeapons[0][9]))
            self.lblmeleePic.configure(width=100, height=90, image=self.picmelee)
        except:
            if playerWeapons[1][1] == "":
                self.lblmeleePic.configure(width=14, height=6, text="Empty Slot")
            else:
                self.lblmeleePic.configure(width=14, height=6, text="Image")

        self.lblmeleeName.configure(text=playerWeapons[0][1])
        self.lblmeleeDamage.configure(text="Damage: "+str(playerWeapons[0][2])+" - "+str(playerWeapons[0][3]))
        self.lblmeleeStam.configure(text="Stamina: "+str(playerWeapons[0][5]))
        self.lblPStamina.configure(text=str(Player.stamina)+" / "+str(Player.maxStamina))

class ArcheryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.archeryPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.archeryPage.pack()
        self.archeryPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.archeryPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(WeaponPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.shopTitle = tk.Label(self.archeryPage, width=15, height=1, font="Arial 25", fg="white", bg="#1a1a1a", text="Archery Shop")
        self.shopTitle.place(relx=.5, rely=.05, anchor="center")

        self.goldTitle = tk.Label(self.archeryPage, width = 30,height=1, bg="#1a1a1a", fg="gold", font="Arial 20",highlightbackground="black",highlightthickness=3, text="Gold: "+str(Bag.gold))
        self.goldTitle.place(relx=.13, rely=.12)

        self.shopBorder = tk.Label(self.archeryPage, width = 30,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.shopBorder.place(relx=.13, rely=.17)

        self.btnCompound = tk.Button(self.archeryPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseBow(8))
        self.btnCompound.place(relx=.22, rely=.23)
        try:
            self.picCompound = ImageTk.PhotoImage(Image.open(weapons_list[8][9]))
            self.btnCompound.configure(width=100, height=90, image=self.picCompound)
        except:
            self.btnCompound.configure(width=13, height=6, text=weapons_list[8][1])

        self.lblCompoundDamage = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[8][2])+" - "+str(weapons_list[8][3]))
        self.lblCompoundDamage.place(relx=.34, rely=.218)
        self.lblCompoundArrow = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Arrows: "+str(weapons_list[8][7]))
        self.lblCompoundArrow.place(relx=.34, rely=.256)
        self.lblCompoundStam = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[8][5]))
        self.lblCompoundStam.place(relx=.34, rely=.295)
        self.lblCompoundCost = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[8][8])+" gold")
        self.lblCompoundCost.place(relx=.34, rely=.333)
        self.lblCompoundName = tk.Label(self.archeryPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[8][1])
        self.lblCompoundName.place(relx=.203, rely=.373)

        self.btnRecurve = tk.Button(self.archeryPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseBow(9))
        self.btnRecurve.place(relx=.22, rely=.497)
        try:
            self.picRecurve = ImageTk.PhotoImage(Image.open(weapons_list[9][9]))
            self.btnRecurve.configure(width=100, height=90, image=self.picRecurve)
        except:
            self.btnRecurve.configure(width=13, height=6, text=weapons_list[9][1])

        self.lblRecurveDamage = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[9][2])+" - "+str(weapons_list[9][3]))
        self.lblRecurveDamage.place(relx=.34, rely=.485)
        self.lblRecurveArrow = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Arrows: "+str(weapons_list[8][7]))
        self.lblRecurveArrow.place(relx=.34, rely=.523)
        self.lblRecurveStam = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[9][5]))
        self.lblRecurveStam.place(relx=.34, rely=.562)
        self.lblRecurveCost = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[9][8])+" gold")
        self.lblRecurveCost.place(relx=.34, rely=.6)
        self.lblRecurveName = tk.Label(self.archeryPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[9][1])
        self.lblRecurveName.place(relx=.203, rely=.64)

        self.btnCrossbow = tk.Button(self.archeryPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseBow(10))
        self.btnCrossbow.place(relx=.22, rely=.76)
        try:
            self.picCrossbow = ImageTk.PhotoImage(Image.open(weapons_list[10][9]))
            self.btnCrossbow.configure(width=100, height=90, image=self.picCrossbow)
        except:
            self.btnCrossbow.configure(width=13, height=6, text=weapons_list[10][1])

        self.lblCrossbowDamage = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[10][2])+" - "+str(weapons_list[10][3]))
        self.lblCrossbowDamage.place(relx=.34, rely=.748)
        self.lblCompoundArrow = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Arrows: "+str(weapons_list[8][7]))
        self.lblCompoundArrow.place(relx=.34, rely=.786)
        self.lblCrossbowStam = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[10][5]))
        self.lblCrossbowStam.place(relx=.34, rely=.825)
        self.lblCrossbowCost = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[10][8])+" gold")
        self.lblCrossbowCost.place(relx=.34, rely=.863)
        self.lblCrossbowName = tk.Label(self.archeryPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[10][1])
        self.lblCrossbowName.place(relx=.203, rely=.903)

        self.inventoryTitle = tk.Label(self.archeryPage, width = 20,height=1, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Inventory")
        self.inventoryTitle.place(relx=.57, rely=.12)

        self.inventory = tk.Label(self.archeryPage, width = 20, height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.inventory.place(relx=.57, rely=.17)

        self.lblBowPic = tk.Label(self.archeryPage, bg="#909090", highlightthickness=5, highlightbackground="black")
        self.lblBowPic.place(relx=.669, rely=.3)
        self.lblBowDamage = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblBowDamage.place(relx=.633, rely=.45)
        self.lblBowArrow = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblBowArrow.place(relx=.633, rely=.5)
        self.lblBowStam = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblBowStam.place(relx=.633, rely=.55)
        self.lblBowName = tk.Label(self.archeryPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 18")
        self.lblBowName.place(relx=.634, rely=.23)

        self.lblAmmo = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left")
        self.lblAmmo.place(relx=.635, rely=.72)

        self.lblStamina = tk.Label(self.archeryPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="Stamina:")
        self.lblStamina.place(relx=.645, rely=.81)
        self.lblPStamina = tk.Label(self.archeryPage, height=1, width=20, bg="#157528", fg="white", font="Arial 15")
        self.lblPStamina.place(relx=.62, rely=.86)

    def purchaseBow(self, index):
        self.updateClearColor()
        if playerWeapons[1][1] == weapons_list[index][1]:
            self.lblBowName.configure(fg="#157528")
        elif Bag.gold < weapons_list[index][8]:
            if index == 8:
                self.lblCompoundCost.configure(fg="gold")
            elif index == 9:
                self.lblRecurveCost.configure(fg="gold")
            elif index == 10:
                self.lblCrossbowCost.configure(fg="gold")
        else:
            Bag.gold -= weapons_list[index][8]
            GameInfo.goldSpent+=weapons_list[index][8]
            playerWeapons[1] = weapons_list[index]
            self.updateInfo()

    def updateClearColor(self):
        self.lblCompoundCost.configure(fg="white")
        self.lblRecurveCost.configure(fg="white")
        self.lblCrossbowCost.configure(fg="white")
        self.lblBowName.configure(fg="white")

    def updateInfo(self):
        self.goldTitle.configure(text="Gold: "+str(Bag.gold))
        self.updateClearColor()
        try:
            self.picBow = ImageTk.PhotoImage(Image.open(playerWeapons[1][9]))
            self.lblBowPic.configure(width=100, height=90, image=self.picBow)
        except:
            if playerWeapons[1][1] == "":
                self.lblBowPic.configure(width=14, height=6, text="Empty Slot")
            else:
                self.lblBowPic.configure(width=14, height=6, text="Image")

        self.lblBowName.configure(text=playerWeapons[1][1])
        self.lblBowDamage.configure(text="Damage: "+str(playerWeapons[1][2])+" - "+str(playerWeapons[1][3]))
        self.lblBowArrow.configure(text="Arrows: "+str(playerWeapons[1][7]))
        self.lblBowStam.configure(text="Stamina: "+str(playerWeapons[1][5]))
        self.lblAmmo.configure(text="Total Arrows: "+str(Bag.arrows))
        self.lblPStamina.configure(text=str(Player.stamina)+" / "+str(Player.maxStamina))

class SidearmPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.sidearmPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.sidearmPage.pack()
        self.sidearmPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.sidearmPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(WeaponPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.shopTitle = tk.Label(self.sidearmPage, width=15, height=1, font="Arial 25", fg="white", bg="#1a1a1a", text="Sidearm Shop")
        self.shopTitle.place(relx=.5, rely=.05, anchor="center")

        self.goldTitle = tk.Label(self.sidearmPage, width = 45,height=1, bg="#1a1a1a", fg="gold", font="Arial 20",highlightbackground="black",highlightthickness=3, text="Gold: "+str(Bag.gold))
        self.goldTitle.place(relx=.03, rely=.12)

        self.shopBorder = tk.Label(self.sidearmPage, width = 45,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.shopBorder.place(relx=.03, rely=.17)

        self.btnSig = tk.Button(self.sidearmPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseSidearm(11))
        self.btnSig.place(relx=.07, rely=.24)
        try:
            self.picSig = ImageTk.PhotoImage(Image.open(weapons_list[11][9]))
            self.btnSig.configure(width=100, height=90, image=self.picSig)
        except:
            self.btnSig.configure(width=13, height=6, text=weapons_list[11][1])

        self.lblSigDamage = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[11][2])+" - "+str(weapons_list[11][3]))
        self.lblSigDamage.place(relx=.19, rely=.243)
        self.lblSigAmmo = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="9mm Rounds: "+str(weapons_list[11][7]))
        self.lblSigAmmo.place(relx=.19, rely=.283)
        self.lblSigCost = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[11][8])+" gold")
        self.lblSigCost.place(relx=.19, rely=.323)
        self.lblSigName = tk.Label(self.sidearmPage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[11][1])
        self.lblSigName.place(relx=.064, rely=.373)


        self.btnGlock = tk.Button(self.sidearmPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseSidearm(12))
        self.btnGlock.place(relx=.07, rely=.5)
        try:
            self.picGlock = ImageTk.PhotoImage(Image.open(weapons_list[12][9]))
            self.btnGlock.configure(width=100, height=90, image=self.picGlock)
        except:
            self.btnGlock.configure(width=13, height=6, text=weapons_list[12][1])

        self.lblGlockDamage = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[12][2])+" - "+str(weapons_list[12][3]))
        self.lblGlockDamage.place(relx=.19, rely=.503)
        self.lblGlockAmmo = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="9mm Rounds: "+str(weapons_list[12][7]))
        self.lblGlockAmmo.place(relx=.19, rely=.543)
        self.lblGlockCost = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[12][8])+" gold")
        self.lblGlockCost.place(relx=.19, rely=.583)
        self.lblGlockName = tk.Label(self.sidearmPage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[12][1])
        self.lblGlockName.place(relx=.064, rely=.633)

        self.btnRuger = tk.Button(self.sidearmPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseSidearm(13))
        self.btnRuger.place(relx=.07, rely=.75)
        try:
            self.picRuger = ImageTk.PhotoImage(Image.open(weapons_list[13][9]))
            self.btnRuger.configure(width=100, height=90, image=self.picRuger)
        except:
            self.btnRuger.configure(width=13, height=6, text=weapons_list[13][1])

        self.lblRugerDamage = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[13][2])+" - "+str(weapons_list[13][3]))
        self.lblRugerDamage.place(relx=.19, rely=.753)
        self.lblRugerAmmo = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="9mm Rounds: "+str(weapons_list[13][7]))
        self.lblRugerAmmo.place(relx=.19, rely=.793)
        self.lblRugerCost = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[13][8])+" gold")
        self.lblRugerCost.place(relx=.19, rely=.833)
        self.lblRugerName = tk.Label(self.sidearmPage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[13][1])
        self.lblRugerName.place(relx=.064, rely=.883)

        self.btnBeretta = tk.Button(self.sidearmPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseSidearm(14))
        self.btnBeretta.place(relx=.38, rely=.24)
        try:
            self.picBeretta = ImageTk.PhotoImage(Image.open(weapons_list[14][9]))
            self.btnBeretta.configure(width=100, height=90, image=self.picBeretta)
        except:
            self.btnBeretta.configure(width=13, height=6, text=weapons_list[14][1])

        self.lblBerettaDamage = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[14][2])+" - "+str(weapons_list[14][3]))
        self.lblBerettaDamage.place(relx=.5, rely=.243)
        self.lblBerettaAmmo = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="9mm Rounds: "+str(weapons_list[14][7]))
        self.lblBerettaAmmo.place(relx=.5, rely=.283)
        self.lblBerettaCost = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[14][8])+" gold")
        self.lblBerettaCost.place(relx=.5, rely=.323)
        self.lblBerettaName = tk.Label(self.sidearmPage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[14][1])
        self.lblBerettaName.place(relx=.374, rely=.373)

        self.btnMP5 = tk.Button(self.sidearmPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseSidearm(15))
        self.btnMP5.place(relx=.38, rely=.5)
        try:
            self.picMP5 = ImageTk.PhotoImage(Image.open(weapons_list[15][9]))
            self.btnMP5.configure(width=100, height=90, image=self.picMP5)
        except:
            self.btnMP5.configure(width=13, height=6, text=weapons_list[15][1])

        self.lblMP5Damage = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[15][2])+" - "+str(weapons_list[15][3]))
        self.lblMP5Damage.place(relx=.5, rely=.503)
        self.lblMP5Ammo = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="9mm Rounds: "+str(weapons_list[15][7]))
        self.lblMP5Ammo.place(relx=.5, rely=.543)
        self.lblMP5Cost = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[15][8])+" gold")
        self.lblMP5Cost.place(relx=.5, rely=.583)
        self.lblMP5Name = tk.Label(self.sidearmPage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[15][1])
        self.lblMP5Name.place(relx=.374, rely=.633)

        self.btnUMP = tk.Button(self.sidearmPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseSidearm(16))
        self.btnUMP.place(relx=.38, rely=.75)
        try:
            self.picUMP = ImageTk.PhotoImage(Image.open(weapons_list[16][9]))
            self.btnUMP.configure(width=100, height=90, image=self.picUMP)
        except:
            self.btnUMP.configure(width=13, height=6, text=weapons_list[16][1])

        self.lblUMPDamage = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[16][2])+" - "+str(weapons_list[16][3]))
        self.lblUMPDamage.place(relx=.5, rely=.753)
        self.lblUMPAmmo = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="9mm Rounds: "+str(weapons_list[16][7]))
        self.lblUMPAmmo.place(relx=.5, rely=.793)
        self.lblUMPCost = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[16][8])+" gold")
        self.lblUMPCost.place(relx=.5, rely=.833)
        self.lblUMPName = tk.Label(self.sidearmPage, width = 11, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[16][1])
        self.lblUMPName.place(relx=.374, rely=.883)

        self.inventoryTitle = tk.Label(self.sidearmPage, width = 18,height=1, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Inventory")
        self.inventoryTitle.place(relx=.7, rely=.12)

        self.inventory = tk.Label(self.sidearmPage, width = 18,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.inventory.place(relx=.7, rely=.17)

        self.lblSidearmPic = tk.Label(self.sidearmPage, bg="#909090", highlightthickness=5, highlightbackground="black")
        self.lblSidearmPic.place(relx=.784, rely=.3)
        self.lblSidearmDamage = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblSidearmDamage.place(relx=.749, rely=.45)
        self.lblSidearmStam = tk.Label(self.sidearmPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblSidearmStam.place(relx=.749, rely=.5)
        self.lblSidearmName = tk.Label(self.sidearmPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 18")
        self.lblSidearmName.place(relx=.75, rely=.23)

        self.lblAmmo = tk.Label(self.sidearmPage, width = 20, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left")
        self.lblAmmo.place(relx=.735, rely=.7)

    def purchaseSidearm(self, index):
        self.updateClearColor()
        if playerWeapons[2][1] == weapons_list[index][1]:
            self.lblSidearmName.configure(fg="#157528")
        elif Bag.gold < weapons_list[index][8]:
            if index == 11:
                self.lblSigCost.configure(fg="gold")
            elif index == 12:
                self.lblGlockCost.configure(fg="gold")
            elif index == 13:
                self.lblRugerCost.configure(fg="gold")
            elif index == 14:
                self.lblBerettaCost.configure(fg="gold")
            elif index == 15:
                self.lblMP5Cost.configure(fg="gold")
            elif index == 16:
                self.lblUMPCost.configure(fg="gold")
        else:
            Bag.gold -= weapons_list[index][8]
            GameInfo.goldSpent+=weapons_list[index][8]
            playerWeapons[2] = weapons_list[index]
            self.updateInfo()

    def updateClearColor(self):
        self.lblSigCost.configure(fg="white")
        self.lblGlockCost.configure(fg="white")
        self.lblRugerCost.configure(fg="white")
        self.lblBerettaCost.configure(fg="white")
        self.lblMP5Cost.configure(fg="white")
        self.lblUMPCost.configure(fg="white")
        self.lblSidearmName.configure(fg="white")

    def updateInfo(self):
        self.goldTitle.configure(text="Gold: "+str(Bag.gold))
        self.updateClearColor()
        try:
            self.picSidearm = ImageTk.PhotoImage(Image.open(playerWeapons[2][9]))
            self.lblSidearmPic.configure(width=100, height=90, image=self.picSidearm)
        except:
            if playerWeapons[2][1] == "":
                self.lblSidearmPic.configure(width=14, height=6, text="Empty Slot")
            else:
                self.lblSidearmPic.configure(width=14, height=6, text="Image")

        self.lblSidearmName.configure(text=playerWeapons[2][1])
        self.lblSidearmDamage.configure(text="Damage: "+str(playerWeapons[2][2])+" - "+str(playerWeapons[2][3]))
        self.lblSidearmStam.configure(text="9mm Rounds: "+str(playerWeapons[2][7]))
        self.lblAmmo.configure(text="Total 9mm: "+str(Bag.scaliber))

class RiflePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.riflePage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.riflePage.pack()
        self.riflePage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.riflePage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(WeaponPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.shopTitle = tk.Label(self.riflePage, width=15, height=1, font="Arial 25", fg="white", bg="#1a1a1a", text="Rifle Shop")
        self.shopTitle.place(relx=.5, rely=.05, anchor="center")

        self.goldTitle = tk.Label(self.riflePage, width = 30,height=1, bg="#1a1a1a", fg="gold", font="Arial 20",highlightbackground="black",highlightthickness=3, text="Gold: "+str(Bag.gold))
        self.goldTitle.place(relx=.13, rely=.12)

        self.shopBorder = tk.Label(self.riflePage, width = 30,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.shopBorder.place(relx=.13, rely=.17)

        self.btnSKS = tk.Button(self.riflePage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseRifle(17))
        self.btnSKS.place(relx=.22, rely=.2)
        try:
            self.picSKS = ImageTk.PhotoImage(Image.open(weapons_list[17][9]))
            self.btnSKS.configure(width=100, height=90, image=self.picSKS)
        except:
            self.btnSKS.configure(width=13, height=6, text=weapons_list[17][1])

        self.lblSKSDamage = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[17][2])+" - "+str(weapons_list[17][3]))
        self.lblSKSDamage.place(relx=.34, rely=.203)
        self.lblSKSAmmo = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="7.62mm Rounds: "+str(weapons_list[17][7]))
        self.lblSKSAmmo.place(relx=.34, rely=.243)
        self.lblSKSCost = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[17][8])+" gold")
        self.lblSKSCost.place(relx=.34, rely=.283)
        self.lblSKSName = tk.Label(self.riflePage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[17][1])
        self.lblSKSName.place(relx=.203, rely=.333)

        self.btnSR = tk.Button(self.riflePage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseRifle(18))
        self.btnSR.place(relx=.22, rely=.4)
        try:
            self.picSR = ImageTk.PhotoImage(Image.open(weapons_list[18][9]))
            self.btnSR.configure(width=100, height=90, image=self.picSR)
        except:
            self.btnSR.configure(width=13, height=6, text=weapons_list[18][1])

        self.lblSRDamage = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[18][2])+" - "+str(weapons_list[18][3]))
        self.lblSRDamage.place(relx=.34, rely=.403)
        self.lblSRAmmo = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="7.62mm Rounds: "+str(weapons_list[18][7]))
        self.lblSRAmmo.place(relx=.34, rely=.443)
        self.lblSRCost = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[18][8])+" gold")
        self.lblSRCost.place(relx=.34, rely=.483)
        self.lblSRName = tk.Label(self.riflePage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[18][1])
        self.lblSRName.place(relx=.203, rely=.533)

        self.btnAK = tk.Button(self.riflePage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseRifle(19))
        self.btnAK.place(relx=.22, rely=.6)
        try:
            self.picAK = ImageTk.PhotoImage(Image.open(weapons_list[19][9]))
            self.btnAK.configure(width=100, height=90, image=self.picAK)
        except:
            self.btnAK.configure(width=13, height=6, text=weapons_list[19][1])

        self.lblAKDamage = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[19][2])+" - "+str(weapons_list[19][3]))
        self.lblAKDamage.place(relx=.34, rely=.603)
        self.lblAKAmmo = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="7.62mm Rounds: "+str(weapons_list[19][7]))
        self.lblAKAmmo.place(relx=.34, rely=.643)
        self.lblAKCost = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[19][8])+" gold")
        self.lblAKCost.place(relx=.34, rely=.683)
        self.lblAKName = tk.Label(self.riflePage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[19][1])
        self.lblAKName.place(relx=.203, rely=.733)

        self.btnRPK = tk.Button(self.riflePage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseRifle(20))
        self.btnRPK.place(relx=.22, rely=.8)
        try:
            self.picRPK = ImageTk.PhotoImage(Image.open(weapons_list[20][9]))
            self.btnRPK.configure(width=100, height=90, image=self.picRPK)
        except:
            self.btnRPK.configure(width=13, height=6, text=weapons_list[20][1])

        self.lblRPKDamage = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[20][2])+" - "+str(weapons_list[20][3]))
        self.lblRPKDamage.place(relx=.34, rely=.803)
        self.lblRPKAmmo = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="7.62mm Rounds: "+str(weapons_list[20][7]))
        self.lblRPKAmmo.place(relx=.34, rely=.843)
        self.lblRPKCost = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[20][8])+" gold")
        self.lblRPKCost.place(relx=.34, rely=.883)
        self.lblRPKName = tk.Label(self.riflePage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[20][1])
        self.lblRPKName.place(relx=.203, rely=.933)

        self.inventoryTitle = tk.Label(self.riflePage, width = 20,height=1, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Inventory")
        self.inventoryTitle.place(relx=.57, rely=.12)

        self.inventory = tk.Label(self.riflePage, width = 20, height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.inventory.place(relx=.57, rely=.17)

        self.lblRiflePic = tk.Label(self.riflePage, bg="#909090", highlightthickness=5, highlightbackground="black")
        self.lblRiflePic.place(relx=.668, rely=.3)
        self.lblRifleDamage = tk.Label(self.riflePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblRifleDamage.place(relx=.633, rely=.45)
        self.lblRifleAmmo = tk.Label(self.riflePage, width = 20, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblRifleAmmo.place(relx=.617, rely=.5)
        self.lblRifleName = tk.Label(self.riflePage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 18")
        self.lblRifleName.place(relx=.634, rely=.23)

        self.lblAmmo = tk.Label(self.riflePage, width = 20, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left")
        self.lblAmmo.place(relx=.619, rely=.7)

    def purchaseRifle(self, index):
        self.updateClearColor()
        if playerWeapons[3][1] == weapons_list[index][1]:
            self.lblRifleName.configure(fg="#157528")
        elif Bag.gold < weapons_list[index][8]:
            if index == 17:
                self.lblSKSCost.configure(fg="gold")
            elif index == 18:
                self.lblSRCost.configure(fg="gold")
            elif index == 19:
                self.lblAKCost.configure(fg="gold")
            elif index == 20:
                self.lblRPKCost.configure(fg="gold")
        else:
            Bag.gold -= weapons_list[index][8]
            GameInfo.goldSpent+=weapons_list[index][8]
            playerWeapons[3] = weapons_list[index]
            self.updateInfo()

    def updateClearColor(self):
        self.lblSKSCost.configure(fg="white")
        self.lblSRCost.configure(fg="white")
        self.lblAKCost.configure(fg="white")
        self.lblRPKCost.configure(fg="white")
        self.lblRifleName.configure(fg="white")

    def updateInfo(self):
        self.goldTitle.configure(text="Gold: "+str(Bag.gold))
        self.updateClearColor()
        try:
            self.picRifle = ImageTk.PhotoImage(Image.open(playerWeapons[3][9]))
            self.lblRiflePic.configure(width=100, height=90, image=self.picRifle)
        except:
            if playerWeapons[3][1] == "":
                self.lblRiflePic.configure(width=14, height=6, text="Empty Slot")
            else:
                self.lblRiflePic.configure(width=14, height=6, text="Image")

        self.lblRifleName.configure(text=playerWeapons[3][1])
        self.lblRifleDamage.configure(text="Damage: "+str(playerWeapons[3][2])+" - "+str(playerWeapons[3][3]))
        self.lblRifleAmmo.configure(text="7.62mm Rounds: "+str(playerWeapons[3][7]))
        self.lblAmmo.configure(text="Total 7.62mm: "+str(Bag.lcaliber))

class SpecialPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.specialPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.specialPage.pack()
        self.specialPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.specialPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(WeaponPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.shopTitle = tk.Label(self.specialPage, width=15, height=1, font="Arial 25", fg="white", bg="#1a1a1a", text="Tactical Shop")
        self.shopTitle.place(relx=.5, rely=.05, anchor="center")

        self.goldTitle = tk.Label(self.specialPage, width = 30,height=1, bg="#1a1a1a", fg="gold", font="Arial 20",highlightbackground="black",highlightthickness=3, text="Gold: "+str(Bag.gold))
        self.goldTitle.place(relx=.13, rely=.12)

        self.shopBorder = tk.Label(self.specialPage, width = 30,height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.shopBorder.place(relx=.13, rely=.17)

        self.btnMerc = tk.Button(self.specialPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseSpecial(22))
        self.btnMerc.place(relx=.22, rely=.23)
        try:
            self.picMerc = ImageTk.PhotoImage(Image.open(weapons_list[22][9]))
            self.btnMerc.configure(width=100, height=90, image=self.picMerc)
        except:
            self.btnMerc.configure(width=13, height=6, text=weapons_list[22][1])

        self.lblMercDamage = tk.Label(self.specialPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[22][2])+" - "+str(weapons_list[22][3]))
        self.lblMercDamage.place(relx=.34, rely=.245)
        self.lblMercCost = tk.Label(self.specialPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[22][8])+" gold")
        self.lblMercCost.place(relx=.34, rely=.306)
        self.lblMercName = tk.Label(self.specialPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[22][1])
        self.lblMercName.place(relx=.203, rely=.373)

        self.btnNerve = tk.Button(self.specialPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseSpecial(23))
        self.btnNerve.place(relx=.22, rely=.497)
        try:
            self.picNerve = ImageTk.PhotoImage(Image.open(weapons_list[23][9]))
            self.btnNerve.configure(width=100, height=90, image=self.picNerve)
        except:
            self.btnNerve.configure(width=13, height=6, text=weapons_list[23][1])

        self.lblNerveDamage = tk.Label(self.specialPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[23][2])+" - "+str(weapons_list[23][3]))
        self.lblNerveDamage.place(relx=.34, rely=.512)
        self.lblNerveCost = tk.Label(self.specialPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[23][8])+" gold")
        self.lblNerveCost.place(relx=.34, rely=.573)
        self.lblNerveName = tk.Label(self.specialPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[23][1])
        self.lblNerveName.place(relx=.203, rely=.64)

        self.btnStrike = tk.Button(self.specialPage, bg="#909090", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseSpecial(24))
        self.btnStrike.place(relx=.22, rely=.76)
        try:
            self.picStrike = ImageTk.PhotoImage(Image.open(weapons_list[24][9]))
            self.btnStrike.configure(width=100, height=90, image=self.picStrike)
        except:
            self.btnStrike.configure(width=13, height=6, text=weapons_list[24][1])

        self.lblStrikeDamage = tk.Label(self.specialPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[24][2])+" - "+str(weapons_list[24][3]))
        self.lblStrikeDamage.place(relx=.34, rely=.775)
        self.lblStrikeCost = tk.Label(self.specialPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[24][8])+" gold")
        self.lblStrikeCost.place(relx=.34, rely=.836)
        self.lblStrikeName = tk.Label(self.specialPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[24][1])
        self.lblStrikeName.place(relx=.203, rely=.903)

        self.inventoryTitle = tk.Label(self.specialPage, width = 20,height=1, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Inventory")
        self.inventoryTitle.place(relx=.57, rely=.12)

        self.inventory = tk.Label(self.specialPage, width = 20, height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.inventory.place(relx=.57, rely=.17)

        self.lblSpecialPic = tk.Label(self.specialPage, bg="#909090", text="Special", highlightthickness=5, highlightbackground="black")
        self.lblSpecialPic.place(relx=.669, rely=.3)
        self.lblSpecialDamage = tk.Label(self.specialPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblSpecialDamage.place(relx=.633, rely=.45)
        self.lblSpecialName = tk.Label(self.specialPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 18")
        self.lblSpecialName.place(relx=.634, rely=.23)

    def purchaseSpecial(self, index):
        self.updateClearColor()
        if playerWeapons[5][1] == weapons_list[index][1]:
            self.lblSpecialName.configure(fg="#157528")
        elif Bag.gold < weapons_list[index][8]:
            if index == 22:
                self.lblMercCost.configure(fg="gold")
            elif index == 23:
                self.lblNerveCost.configure(fg="gold")
            elif index == 24:
                self.lblStrikeCost.configure(fg="gold")
        else:
            Bag.gold -= weapons_list[index][8]
            GameInfo.goldSpent+=weapons_list[index][8]
            playerWeapons[5] = weapons_list[index]
            self.updateInfo()

    def updateClearColor(self):
        self.lblMercCost.configure(fg="white")
        self.lblNerveCost.configure(fg="white")
        self.lblStrikeCost.configure(fg="white")
        self.lblSpecialName.configure(fg="white")

    def updateInfo(self):
        self.goldTitle.configure(text="Gold: "+str(Bag.gold))
        self.updateClearColor()
        try:
            self.picSpecial = ImageTk.PhotoImage(Image.open(playerWeapons[5][9]))
            self.lblSpecialPic.configure(width=100, height=90, image=self.picSpecial)
        except:
            if playerWeapons[5][1] == "":
                self.lblSpecialPic.configure(width=14, height=6, text="Empty Slot", image="")
            else:
                self.lblSpecialPic.configure(width=14, height=6, text="Image", image="")

        self.lblSpecialName.configure(text=playerWeapons[5][1])
        self.lblSpecialDamage.configure(text="Damage: "+str(playerWeapons[5][2])+" - "+str(playerWeapons[5][3]))

class BlackPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.blackPage = tk.Frame(self,width=1100, height=800, bg="#08451b")
        self.blackPage.pack()
        self.blackPage.pack_propagate(0) #prevents frame from shrinking to fit widgets
        textChecker = self.register(self.validInput)

        self.btnBack = tk.Button(self.blackPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(TownPage))
        self.btnBack.place(relx=.03, rely=.03)

        self.lblTitle = tk.Label(self.blackPage, height=1, width=15, bg="black", highlightbackground="white", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 20", text='Black Jack')
        self.lblTitle.place(relx=.27, rely=.055, anchor="center")

        self.lblDealerTitle = tk.Label(self.blackPage, height=1, width=25, bg="black", highlightbackground="white", highlightthickness=3, fg="white", font="Arial 20", text="Dealers Hand: ")
        self.lblDealerTitle.place(relx=.023, rely=.16)

        self.lblCard1 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard1.place(relx=.022, rely=.25)

        self.lblCard2 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard2.place(relx=.142, rely=.25)

        self.lblCard3 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard3.place(relx=.262, rely=.25)

        self.lblCard4 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard4.place(relx=.382, rely=.25)

        self.lblCard5 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard5.place(relx=.502, rely=.25)

        self.lblCard6 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard6.place(relx=.622, rely=.25)

        self.lblCard7 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard7.place(relx=.742, rely=.25)

        self.lblCard8 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard8.place(relx=.862, rely=.25)

        self.lblPlayerTitle = tk.Label(self.blackPage, height=1, width=25, bg="black", highlightbackground="white", highlightthickness=3, fg="white", font="Arial 20", text=Player.name+"'s Hand: ")
        self.lblPlayerTitle.place(relx=.023, rely=.56)

        self.lblCard9 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard9.place(relx=.022, rely=.65)

        self.lblCard10 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard10.place(relx=.142, rely=.65)

        self.lblCard11 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard11.place(relx=.262, rely=.65)

        self.lblCard12 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard12.place(relx=.382, rely=.65)

        self.lblCard13 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard13.place(relx=.502, rely=.65)

        self.lblCard14 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard14.place(relx=.622, rely=.65)

        self.lblCard15 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard15.place(relx=.742, rely=.65)

        self.lblCard16 = tk.Label(self.blackPage, bg="#08451b", activebackground="#909090", width=15, height=10)
        self.lblCard16.place(relx=.862, rely=.65)

        self.lblOutcome = tk.Label(self.blackPage, height=1, width=35, bg="black", fg="white", font="Arial 17",highlightthickness=2, highlightbackground="white", padx=33, pady=6)
        self.lblOutcome.place(relx=.4596, rely=.155)

        self.goldTitle = tk.Label(self.blackPage, width=35, height= 3, font="Arial 17", bg="black", fg="gold", text=Player.name+"'s Gold: "+str(Bag.gold), anchor="nw", padx=33, pady = 10, highlightthickness=2, highlightbackground="white")
        self.goldTitle.place(relx=.46, rely=.025)

        self.betVar = tk.StringVar()
        entBet = tk.Entry(self.blackPage, width=10, bg="white", font="Arial 18", textvariable=self.betVar,validate="key", validatecommand=(textChecker,'%P', 5))
        entBet.place(relx=.55, rely=.1)

        self.btnPlaceBet = tk.Button(self.blackPage, height=1, width=20, font="Arial 15", bg="grey", fg="white", text="Place Bet", cursor="hand2", relief="solid", command=self.checkBet)
        self.btnPlaceBet.place(relx=.7, rely=.095)

        self.entLabel = tk.Label(self.blackPage, width = 4, height= 1, bg="black", fg="white",font="Arial 18", text="Bet:")
        self.entLabel.place(relx=.486, rely=.1)

        self.btnHit = tk.Button(self.blackPage, height=1, width=11, font="Arial 20", bg="grey", fg="white", cursor="hand2", state="disabled", text = "Hit", command=self.hitFunction)
        self.btnHit.place(relx=.023, rely=.9)

        self.btnStay = tk.Button(self.blackPage, height=1, width=11, font="Arial 20", bg="grey", fg="white", cursor="hand2", state="disabled", text = "Stay", command=self.stayFunction)
        self.btnStay.place(relx=.23, rely=.9)

        self.badBet = tk.Label(self.blackPage, width = 20, height=1, font="Arial 15", bg="black", fg="white", anchor="w")
        self.badBet.place(relx=.7, rely=.043)

        self.cardPlaces = (self.lblCard1,self.lblCard2,self.lblCard3,self.lblCard4,self.lblCard5,self.lblCard6,self.lblCard7,self.lblCard8,self.lblCard9,self.lblCard10,self.lblCard11,self.lblCard12,self.lblCard13,self.lblCard14,self.lblCard15, self.lblCard16)

    def validInput(self, text, maxLength):
        if text:
            return len(text) <= int(maxLength) and text.isdigit()
        return True

    def checkBet(self):
        if Bag.gold < 1:
            self.badBet.configure(text="Please exit the Casino")
        elif self.betVar.get() == "":
            self.badBet.configure(text="Invalid bet amount")
        else:
            bet = int(self.betVar.get())
            if bet < 1:
                self.badBet.configure(text="Invalid bet amount")
            elif Bag.gold < bet:
                self.badBet.configure(text="Invalid bet amount")
            else:
                self.badBet.configure(text="Bet's good")
                self.goldTitle.configure(text = Player.name+"'s Gold: "+ str(Bag.gold))
                self.playerCards = []
                self.dealerCards = []
                self.thePlay()

    def thePlay(self):
        self.resetPage()
        self.btnBack.configure(state="disabled")
        self.playerOutcome = ""
        self.dealerOutcome = ""
        self.tempDeck = cardsList[:]
        self.playerCards.append(self.randomCard(self.tempDeck))
        self.playerCards.append(self.randomCard(self.tempDeck))
        self.dealerCards.append(self.randomCard(self.tempDeck))

        self.blackPage.after(1000, lambda: self.displayCard(self.playerCards[0][5],9))
        self.blackPage.after(2000, lambda: self.displayCard(self.playerCards[1][5],10))
        self.blackPage.after(3000, lambda: self.displayCard(self.dealerCards[0][5],1))
        self.manageAceValue(self.playerCards)
        self.dealerSum = self.cardsSum(self.dealerCards)
        self.playerSum = self.cardsSum(self.playerCards)
        self.blackPage.after(2000, lambda: self.changePlayerTitle(Player.name+"'s Hand: "+str(self.playerSum)))
        self.blackPage.after(3000, lambda: self.changeDealerTitle("Dealers Hand: "+str(self.dealerSum)))
        if self.playerSum == 21:
            self.blackPage.after(3100, lambda: self.changeOutcome("You have a Natural!"))
            self.playerOutcome = 21
            self.blackPage.after(4000, self.dealerTurn)
        else:
            self.blackPage.after(3500, lambda: self.btnState("normal"))

    def hitFunction(self):
        self.btnState("disabled")
        self.playerCards.append(self.randomCard(self.tempDeck))
        numPlayerCards = len(self.playerCards)
        self.blackPage.after(1000, lambda: self.displayCard(self.playerCards[numPlayerCards-1][5],8+numPlayerCards))
        self.manageAceValue(self.playerCards)
        self.playerSum = self.cardsSum(self.playerCards)
        self.blackPage.after(1000, lambda: self.changePlayerTitle(Player.name+"'s Hand: "+str(self.playerSum)))
        if self.playerSum < 21:
            self.blackPage.after(1500, lambda: self.btnState("normal"))

        elif self.playerSum == 21:
            self.playerOutcome = 21
            self.dealerTurn()
        else:
            Bag.gold -= int(self.betVar.get())
            GameInfo.goldSpent+=int(self.betVar.get())
            self.blackPage.after(3001, lambda: self.changeOutcome("Bust! You lost "+self.betVar.get()+" gold"))
            self.goldTitle.configure(text = Player.name+"'s Gold: "+ str(Bag.gold))
            self.btnBack.configure(state="normal")

    def stayFunction(self):
        self.btnState("disabled")
        self.playerOutcome = self.playerSum
        self.dealerTurn()

    def dealerTurn(self):
        self.dealerCards.append(self.randomCard(self.tempDeck))
        numDealerCards2 = 2
        displayTime = 2000
        self.blackPage.after(displayTime, lambda: self.displayCard(self.dealerCards[numDealerCards2-1][5],numDealerCards2))
        self.manageAceValue(self.dealerCards)
        dealerSum2 = self.cardsSum(self.dealerCards)
        self.blackPage.after(displayTime, lambda: self.changeDealerTitle("Dealer's Hand: "+str(dealerSum2)))

        if dealerSum2 < 17:
            self.dealerCards.append(self.randomCard(self.tempDeck))
            numDealerCards3 = 3
            displayTime+=2000
            self.blackPage.after(displayTime, lambda: self.displayCard(self.dealerCards[numDealerCards3-1][5],numDealerCards3))
            self.manageAceValue(self.dealerCards)
            dealerSum3 = self.cardsSum(self.dealerCards)
            self.blackPage.after(displayTime, lambda: self.changeDealerTitle("Dealer's Hand: "+str(dealerSum3)))

            if dealerSum3 < 17:

                self.dealerCards.append(self.randomCard(self.tempDeck))
                numDealerCards4 = 4
                displayTime+=2000
                self.blackPage.after(displayTime, lambda: self.displayCard(self.dealerCards[numDealerCards4-1][5],numDealerCards4))
                self.manageAceValue(self.dealerCards)
                dealerSum4 = self.cardsSum(self.dealerCards)
                self.blackPage.after(displayTime, lambda: self.changeDealerTitle("Dealer's Hand: "+str(dealerSum4)))

                if dealerSum4 < 17:
                    self.dealerCards.append(self.randomCard(self.tempDeck))
                    numDealerCards5 = 5
                    displayTime+=2000
                    self.blackPage.after(displayTime, lambda: self.displayCard(self.dealerCards[numDealerCards5-1][5],numDealerCards5))
                    self.manageAceValue(self.dealerCards)
                    dealerSum5 = self.cardsSum(self.dealerCards)
                    self.blackPage.after(displayTime, lambda: self.changeDealerTitle("Dealer's Hand: "+str(dealerSum5))) 

                    if dealerSum5 < 17:
                        self.dealerCards.append(self.randomCard(self.tempDeck))
                        numDealerCards6 = 6
                        displayTime+=2000
                        self.blackPage.after(displayTime, lambda: self.displayCard(self.dealerCards[numDealerCards6-1][5],numDealerCards6))
                        self.manageAceValue(self.dealerCards)
                        dealerSum6 = self.cardsSum(self.dealerCards)
                        self.blackPage.after(displayTime, lambda: self.changeDealerTitle("Dealer's Hand: "+str(dealerSum6)))  

                        if dealerSum6 < 17:
                            self.dealerCards.append(self.randomCard(self.tempDeck))
                            numDealerCards7 = 7
                            displayTime+=2000
                            self.blackPage.after(displayTime, lambda: self.displayCard(self.dealerCards[numDealerCards7-1][5],numDealerCards7))
                            self.manageAceValue(self.dealerCards)
                            dealerSum7 = self.cardsSum(self.dealerCards)
                            self.blackPage.after(displayTime, lambda: self.changeDealerTitle("Dealer's Hand: "+str(dealerSum7))) 

                            if dealerSum7 < 17:
                                self.dealerCards.append(self.randomCard(self.tempDeck))
                                numDealerCards8 = 8
                                displayTime+=2000
                                self.blackPage.after(displayTime, lambda: self.displayCard(self.dealerCards[numDealerCards8-1][5],numDealerCards8))
                                self.manageAceValue(self.dealerCards)
                                dealerSum8 = self.cardsSum(self.dealerCards)
                                self.blackPage.after(displayTime, lambda: self.changeDealerTitle("Dealer's Hand: "+str(dealerSum8)))
        
        self.dealerOutcome = self.cardsSum(self.dealerCards)
        displayTime+=2000
        self.blackPage.after(displayTime, self.computeOutcome)
            

    def dealerNewCard(self):
        self.dealerCards.append(self.randomCard(self.tempDeck))
        numDealerCards = len(self.dealerCards)
        self.displayCard(self.dealerCards[numDealerCards-1][5],numDealerCards)
        self.manageAceValue(self.dealerCards)
        self.dealerSum = self.cardsSum(self.dealerCards)
        self.changeDealerTitle("Dealer's Hand: "+str(self.dealerSum))

    def computeOutcome(self):
        bet = int(self.betVar.get())
        if self.playerOutcome == 21 and len(self.playerCards) == 2 and self.dealerOutcome != 21: #if player has a natural, and dealer doesn't have 21
            winning = (bet*1.5)
            if winning % 1 != 0:
                winning+= 0.5
            winning = int(winning)
            Bag.gold+=winning
            GameInfo.goldEarned+=winning
            self.lblOutcome.configure(text="You win "+str(winning)+" Gold!")
        elif int(self.dealerOutcome) > 21: # if dealer busts
            Bag.gold+=bet
            GameInfo.goldEarned+=bet
            self.lblOutcome.configure(text="You win "+str(bet)+" Gold!")
        elif self.playerOutcome < int(self.dealerOutcome) <= 21: #if dealer has higher sum than player, but not bust
            Bag.gold -= bet
            GameInfo.goldSpent+=bet
            self.lblOutcome.configure(text="You lose "+str(bet)+" Gold")
        elif self.playerOutcome == self.dealerOutcome:
            self.lblOutcome.configure(text="Push")
        else:
            Bag.gold += bet
            GameInfo.goldEarned+=bet
            self.lblOutcome.configure(text="You win "+str(bet)+" Gold!")

        self.goldTitle.configure(text = Player.name+"'s Gold: "+ str(Bag.gold))
        self.btnBack.configure(state="normal")

    def cardsSum(self, userCards):
        total = 0
        for x in range(len(userCards)):
            total += userCards[x][2]
        return total    
        
    def manageAceValue(self, userCards):
        aceIndex = -1
        for x in range(len(userCards)):
            if userCards[x][2] == 11:
                aceIndex = x
                print(aceIndex)
                break
        if self.cardsSum(userCards) > 21 and aceIndex != -1: # if players cards sum is over 21, and they have an ace with a value of 11
            print("ace is changing. value is: "+str(self.cardsSum(userCards)))
            userCards[aceIndex][2] = 1 #changes the value of an acce from an 11 to a 1
    
    def btnState(self, newState):
        self.btnHit.configure(state=newState)
        self.btnStay.configure(state=newState)

    def resetPage(self):
        for x in self.cardPlaces:
            x.configure(image="", highlightbackground="#08451b")
        self.goldTitle.configure(text=Player.name+"'s Gold: "+ str(Bag.gold))
        self.lblDealerTitle.configure(text="Dealers Hand: ")
        self.lblPlayerTitle.configure(text=Player.name+"'s Hand: ")
        self.lblOutcome.configure(text="")

    def changeOutcome(self, newText):
        self.lblOutcome.configure(text=newText)
    
    def changePlayerTitle(self, newText):
        self.lblPlayerTitle.configure(text=newText)
    
    def changeDealerTitle(self, newText):
        self.lblDealerTitle.configure(text=newText)

    def displayCard(self, cardImage, x):
        if x == 1:
            try:
                self.picCard1 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard1.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard1)
            except:
                self.lblCard1.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==2:
            try:
                self.picCard2 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard2.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard2)
            except:
                self.lblCard2.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==3:
            try:
                self.picCard3 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard3.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard3)
            except:
                self.lblCard3.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==4:
            try:
                self.picCard4 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard4.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard4)
            except:
                self.lblCard4.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==5:
            try:
                self.picCard5 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard5.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard5)
            except:
                self.lblCard5.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==6:
            try:
                self.picCard6 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard6.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard6)
            except:
                self.lblCard6.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==7:
            try:
                self.picCard7 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard7.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard7)
            except:
                self.lblCard7.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==8:
            try:
                self.picCard8 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard8.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard8)
            except:
                self.lblCard8.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==9:
            try:
                self.picCard9 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard9.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard9)
            except:
                self.lblCard9.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==10:
            try:
                self.picCard10 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard10.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard10)
            except:
                self.lblCard10.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==11:
            try:
                self.picCard11 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard11.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard11)
            except:
                self.lblCard11.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==12:
            try:
                self.picCard12 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard12.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard12)
            except:
                self.lblCard12.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==13:
            try:
                self.picCard13 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard13.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard13)
            except:
                self.lblCard13.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==14:
            try:
                self.picCard14 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard14.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard14)
            except:
                self.lblCard14.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==15:
            try:
                self.picCard15 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard15.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard15)
            except:
                self.lblCard15.configure(width=11, height=7, font="Arial 15", text="Image")
        elif x==16:
            try:
                self.picCard16 = ImageTk.PhotoImage(Image.open(cardImage))
                self.lblCard16.configure(width=120, height=170, highlightbackground="black", highlightthickness=3, image=self.picCard16)
            except:
                self.lblCard16.configure(width=11, height=7, font="Arial 15", text="Image")

        

    def randomCard(self, listOfCards):
        """Chooses a random card from a given deck"""

        ranNum = random.randint(0, len(listOfCards)-1)
        card = listOfCards[ranNum]
        del listOfCards[ranNum]
        return card #the index value of the selected card

class EndPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.endPage = tk.Frame(self,width=1100, height=800, bg="black")
        self.endPage.pack()
        self.endPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        lblGameName = tk.Label(self.endPage, text="---------------- The End ----------------", font="Arial 50", bg='black', fg="white")
        lblGameName.place(relx=0.5, rely=0.125, anchor="center")

        self.lblEnemies = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblEnemies.place(relx=.125, rely=.27)

        self.lblDamDealt = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblDamDealt.place(relx=.125, rely=.345)

        self.lblDamTaken = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblDamTaken.place(relx=.125, rely=.42)

        self.lblArrows = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblArrows.place(relx=.125, rely=.495)

        self.lblSCal = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblSCal.place(relx=.125, rely=.57)

        self.lblMCal = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblMCal.place(relx=.125, rely=.645)

        self.lblGrenades = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblGrenades.place(relx=.515, rely=.27)

        self.lblSpecial = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblSpecial.place(relx=.515, rely=.345)

        self.lblHPotion = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblHPotion.place(relx=.515, rely=.42)

        self.lblSPotion = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblSPotion.place(relx=.515, rely=.495)

        self.lblGoldEarned = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblGoldEarned.place(relx=.515, rely=.57)

        self.lblGoldSpent = tk.Label(self.endPage, height=1, width=27, bg="black", fg="white", font="Arial 18")
        self.lblGoldSpent.place(relx=.515, rely=.645)

        self.btnTown = tk.Button(self.endPage, height=2, width=20,bg="grey",fg="white", state="normal", relief="sunken", cursor="hand2", font="Arial 19", text="Return to Town", command=lambda: self.goToTown(controller))
        self.btnTown.place(relx=.16, rely=.8)

        self.btnMenu = tk.Button(self.endPage, height=2, width=20,bg="grey",fg="white", state="normal", relief="sunken", cursor="hand2", font="Arial 19", text="Exit to Main Menu", command=lambda: self.goToMain(controller))
        self.btnMenu.place(relx=.55, rely=.8)

    def goToTown(self,controller):
        GameInfo.location == "town"
        GameInfo.mode=2
        controller.showFrame(TownPage)

    def goToMain(self,controller):
        controller.showFrame(MainPage)

    def updateInfo(self):
        self.lblEnemies.configure(text="Enemies Killed: "+str(GameInfo.enemies))
        self.lblDamDealt.configure(text="Damage Dealt: "+str(GameInfo.damDealt))
        self.lblDamTaken.configure(text="Damage Taken: "+str(GameInfo.damTaken))
        self.lblArrows.configure(text="Arrows Used: "+str(GameInfo.arrows))
        self.lblSCal.configure(text="9mm Rounds Used: "+str(GameInfo.sCal))
        self.lblMCal.configure(text="7.62mm Rounds Used: "+str(GameInfo.mCal))
        self.lblGrenades.configure(text="Grenades Used: "+str(GameInfo.grenades))
        self.lblSpecial.configure(text="Specials Used: "+str(GameInfo.special))
        self.lblHPotion.configure(text="Health Potions Used: "+str(GameInfo.hPotion))
        self.lblSPotion.configure(text="Stamina Potions Used: "+str(GameInfo.sPotion))
        self.lblGoldEarned.configure(text="Gold Aquired: "+str(GameInfo.goldEarned))
        self.lblGoldSpent.configure(text="Gold Spent: "+str(GameInfo.goldSpent))

game = GameApp()

game.mainloop()
