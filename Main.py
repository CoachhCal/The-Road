try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from PIL import ImageTk, Image
import math

import time
import random


"""
IMPORTANT:

https://deckofcardsapi.com/

https://deckofcardsapi.com/static/img/AS.png

"""



class PlayerClass:
    def __init__(self, name, age, color, height, weight, sex, armor, maxHealth, health, stamina, maxStamina, mode, next):
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
        self.mode = mode
        self.next = next
    
    def totalHealth(self):
        return self.armor + 100
    
class GameClass:
    def __init__(self, mode, nextFunction, location):
        self.mode = mode
        self.nextFunction = nextFunction
        self.location = location #Can either be road, or town
    
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
# playerWeapons[0] = weapons_list[0]
# playerWeapons[1] = weapons_list[10]
# playerWeapons[2] = weapons_list[11]
# playerWeapons[3] = weapons_list[19]
# playerWeapons[4] = weapons_list[21]
# playerWeapons[5] = weapons_list[22]
GameInfo = GameClass(1, "None", "road")
Enemy = EnemyClass
Armor = ArmorClass

Player = PlayerClass("Calvin", 0, "White", 178, 152, "man", "none", 100, 100, 100, 100, 2, "none")
Bag = Inventory(0, 0, 100, 0, 0, 0, 0)

class GameApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self, height=800, width=1100, bg="black")
        super().minsize(1100, 800) #super refers to the window
        # window.configure()
        window.pack(side="top", fill = "both", expand=True)

        self.frames = {}
        for F in (SplashPage, StartPage, MainPage, FightPage, TownPage, ArenaPage, ShopPage, AmmoPage, ArmorPage, PotionPage, WeaponPage, MeleePage, ArcheryPage, SidearmPage, RiflePage, SpecialPage, BlackPage):
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

        lblGameName = tk.Label(initialPage, text="The Game", font="Arial 50", bg='#c5c5c5')
        lblGameName.place(relx=0.5, rely=0.1, anchor="center")

        lblCreatorName = tk.Label(initialPage, text="By: Calvin Murray", font="Arial 36", bg="grey")
        lblCreatorName.place(relx=0.01,rely= .95, anchor="w")

        lblDate = tk.Label(initialPage, text="2024", font="Arial 36", bg="grey")
        lblDate.place(relx = .96, rely= .95, anchor="e")

        btnBegin = tk.Button(initialPage, text="Click to Start", font="Arial 36", relief="solid", bg="grey",cursor="hand2", command=lambda: self.yup(controller))
        btnBegin.place(relx=.5, rely=.6, anchor="center")

    def yup(self, controller):
        controller.showFrame(StartPage)
        # controller.showFrame(FightPage) #Take this out to make it work
        # controller.frames[FightPage].updateWeapons()
        # controller.frames[FightPage].updateInfo()
        # controller.frames[FightPage].enemyBattle(1,4,"Cyclopes", 0)
        # controller.showFrame(MainPage)
        # controller.frames[MainPage].one1(controller)
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
                if rbValue == 1:
                    Player.sex = "man"
                elif rbValue == 2:
                    Player.sex = "woman"
                Player.name = nameVar
                Player.age = int(ageVar)
                Player.color = skinVar
                Player.height = (int(heightVarFt) * 12) + int(heightVarIn)
                Player.weight = int(weightVar)
                GameInfo.mode = btnValue
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

        self.btnYes = tk.Button(self.mainPage, height=1, width=10,bg="grey",fg="white",state="disabled", relief="solid", cursor="hand2", font="Arial 20")
        self.btnYes.place(relx=.32, rely=.85)

        self.btnNo = tk.Button(self.mainPage, height=1, width=10,bg="grey",fg="white", state="disabled", relief="solid", cursor="hand2", font="Arial 20")
        self.btnNo.place(relx=.52, rely=.85)

    def healthPotion(self):
        print("hi")
    #     if Bag.healthPotion == 0:
    #         self.updateText("\nInsufficient health potions\n\nYou have: "+str(Bag.healthPotion)+"\nRequired amount: 1")
    #     elif Player.health == Player.maxHealth:
    #         self.clearText()
    #         self.updateText("\n\nAlready at max health")
    #     else:
    #         Bag.healthPotion -= 1
    #         Player.health += potionList[0][1]
    #         if Player.health > Player.maxHealth:
    #             Player.health = Player.maxHealth
    #         self.updateInfo()

    def staminaPotion(self):
        print("no")
    #     if Bag.staminaPotion == 0:
    #         self.clearText()
    #         self.updateText("\nInsufficient stamina potions\n\nYou have: "+str(Bag.staminaPotion)+"\nRequired amount: 1")
    #     elif Player.stamina == Player.maxStamina:
    #         self.clearText()
    #         self.updateText("\n\nAlready at max stamina")
    #     else:
    #         Player.stamina += potionList[1][1]
    #         Bag.staminaPotion -= 1
    #         if Player.stamina > Player.maxStamina:
    #             Player.stamina = Player.maxStamina
    #         self.updateInfo()

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

    def one1(self, controller):
        self.snapBottom()
        self.after(3000, lambda: self.updateText("\nYou wake up, laying face down in the dirt."))
        self.after(7000, lambda: self.updateText("\n\nFinding your footing, you see your flipped truck nearby, still radiating heat."))
        self.after(13000, lambda: self.updateText("\n\nUnsure of your whereabouts, you hear something rustling in a bush."))
        self.after(18000, lambda: self.updateText("\n\nSlowing making your way over, you see a goose pecking at your bag."))
        self.after(25000, lambda: self.updateText("\n\nWithin seconds, the goose sees you, flaring out its wings."))
        self.after(31000, lambda: self.updateText("\n\nLooking around quickly, you pick up a stick to defend yourself."))
        playerWeapons[0] = weapons_list[0]
        self.after(37000, lambda: controller.showFrame(FightPage))
        self.after(37001,lambda: controller.frames[FightPage].enemyBattle(1,2,"Goose", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.one2
        self.after(38000, self.clearBox)

    def one2(self, controller):
        self.after(3000, lambda: self.updateText("\nYou toss the dead goose aside and look through the bag."))
        self.after(7000, lambda: self.updateText("\n\nMost of your supplies is missing."))
        self.after(10000, lambda: self.updateText("\n\nYou'll need to re-stock quickly if you want to survive."))
        self.after(15000, lambda: self.updateText("\n\nYou quickly gather the remaining supplies scattered around your bag:"))
        self.after(21000, lambda: self.updateText("\n\nA few potions, a pouch of gold, a bow and arrows, along with a single grenade."))
        Bag.gold +=120
        Bag.healthPotion +=2
        Bag.staminaPotion +=1
        Bag.arrows +=4
        Bag.grenades +=1
        playerWeapons[4] = weapons_list[21]
        playerWeapons[1] = weapons_list[8]
        self.after(22000, self.updateInfo)
        self.after(28000, lambda: self.updateText("\n\nIt's not much, but it will have to do for now."))
        self.after(34000, lambda: self.updateText("\n\nYou head back to the main road and begin your journey."))
        self.after(38000, self.clearBox)
        self.after(39000, lambda: self.updateText("\n\n*A few miles later...*"))
        self.after(41000, lambda: self.updateText("\n\nYou spot a carriage abandoned on the road ahead."))
        self.after(46000, lambda: self.updateText("\n\nAs you get closer, a man shouts from inside the carriage."))
        if Player.sex == "man":
            self.after(51000, lambda: self.updateText("\n\nMan: \"Hey Mister, could you please get this thing away from me!?\""))
        else:
            self.after(51000, lambda: self.updateText("\n\nMan: \"Hey Miss, could you please get this thing away from me!?\""))
        self.after(56000, lambda: self.updateText("\n\nA metal creature slowly crawls out from under the carriage."))
        self.after(61000, lambda: controller.showFrame(FightPage))
        self.after(61001,lambda: controller.frames[FightPage].enemyBattle(1,2,"Dwarven Spider", 0))
        controller.frames[FightPage].updateWeapons()
        GameInfo.nextFunction = self.one3
        self.after(62000, self.clearBox)

    def one3(self, controller):
        self.after(3000, lambda: self.updateText("\nThe man gets out of the carriage, looking at the pile of scrap metal."))
        self.after(8000, lambda: self.updateText("\n\nMan: \"Thank you for the assistance! I'm far too old to be fighting these things.\""))
        self.after(15000, lambda: self.updateText("\n\nMan: \"You on the other hand look like a "+Player.sex+" who can take care of themselves.\""))
        self.after(22000, lambda: self.updateText("\n\nMan: \"Still, an out-of-towner like you could end up being food if youre not too careful.\""))
        self.after(29000, lambda: self.updateText("\n\nMan: \"A bit of advice, the only way to survive these lands is to stay stocked up on gear.\""))
        self.after(36000, lambda: self.updateText("\n\nMan: \"Be mindful of your ammunition and health before getting into any fights.\""))
        self.after(42000, self.clearBox)
        self.after(43000, lambda: self.updateText("\n\nMan: \"You know what, I was headed to the next town to sell supplies, but I can give you a quick look right now.\""))
        self.after(51000, lambda: self.updateText("\n\nMan: \"And remember, you can never have too many potions on hand!\""))
        self.after(56000, self.clearBox)
        self.after(56000, lambda: controller.showFrame(ShopPage))
        GameInfo.nextFunction = self.one4

    def one4(self, controller):
        print("hi")
        
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
       
        
        self.btnMelee = tk.Button(self.fightPage, bg="#909090",text="Melee", cursor="hand2", command=lambda: self.playerAttack(0, controller))
        self.btnMelee.place(relx=.05, rely=.76)
        self.lblMelee = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblMelee.place(relx=.037, rely=.88)

        self.btnBow = tk.Button(self.fightPage, bg="#909090",text="Bow",cursor="hand2", command=lambda: self.playerAttack(1, controller))
        self.btnBow.place(relx=.188, rely=.76)
        self.lblBow = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblBow.place(relx=.179, rely=.8925)

        self.btnSmallCal = tk.Button(self.fightPage, bg="#909090",text= "Sidearm",cursor="hand2", command=lambda: self.playerAttack(2, controller))
        self.btnSmallCal.place(relx=.318, rely=.76)
        self.lblSmallCal = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblSmallCal.place(relx=.309, rely=.88)

        self.btnMedCal = tk.Button(self.fightPage, bg="#909090",text="Rifle",cursor="hand2", command=lambda: self.playerAttack(3, controller))
        self.btnMedCal.place(relx=.448, rely=.76)
        self.lblMedCal = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblMedCal.place(relx=.439, rely=.88)

        self.btnGrenade = tk.Button(self.fightPage, bg="#909090",text="Grenade",cursor="hand2", command=lambda: self.playerAttack(4, controller))
        self.btnGrenade.place(relx=.578, rely=.76)
        self.lblGren = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblGren.place(relx=.569, rely=.88)

        self.btnSpecial = tk.Button(self.fightPage, bg="#909090",text="Special",cursor="hand2", command=lambda: self.playerAttack(5, controller))
        self.btnSpecial.place(relx=.712, rely=.76)
        self.lblSpec = tk.Label(self.fightPage, width = 14, height=4, bg = "#1a1a1a", fg="white", font="Arial 12")
        self.lblSpec.place(relx=.703, rely=.88)

        self.btnFlee = tk.Button(self.fightPage, width=13, height=5,cursor="hand2",text="Flee", bg="grey")
        self.btnFlee.place(relx=.845, rely=.76)

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

    def playerAttack(self,index, controller):
        self.buttonState("disabled", "x_cursor")
        successfulAttack = False
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
                Player.stamina -= playerWeapons[index][5]
                Bag.arrows -= playerWeapons[index][7]
                self.displayAttack(index, damage)
        elif index == 2:
            if Bag.scaliber < playerWeapons[index][7]:
                self.clearText()
                self.updateText("\nInsufficient 9mm rounds\n\nYou have: "+str(Bag.scaliber)+"\nRequired amount: "+str(playerWeapons[2][7]))
            else:
                successfulAttack = True
                damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                Bag.scaliber -= playerWeapons[index][7]
                self.displayAttack(index, damage)
        elif index == 3:
            if Bag.lcaliber < playerWeapons[index][7]:
                self.clearText()
                self.updateText("\nInsufficient 7.62mm rounds\n\nYou have: "+str(Bag.lcaliber)+"\nRequired amount: "+str(playerWeapons[3][7]))
            else:
                successfulAttack = True
                damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                Bag.lcaliber -= playerWeapons[index][7]
                self.displayAttack(index, damage)
        elif index == 4:
            if Bag.grenades < 1:
                self.clearText()
                self.updateText("\nInsufficient grenades\n\nYou have: "+str(Bag.grenades)+"\nRequired amount: "+str(playerWeapons[4][7]))
            else:
                successfulAttack = True
                damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                Bag.grenades -= playerWeapons[index][7]
                self.displayAttack(index, damage)
        elif index == 5:
            if playerWeapons[5][1] == "": #does the player have a speical attack in their inventory?
                self.clearText()
                self.updateText("\n\nYou do not own a special attack")
            else:
                successfulAttack = True
                damage = random.randint(playerWeapons[index][2], playerWeapons[index][3])
                self.displayAttack(index, damage)
                playerWeapons[5] = ["", "", "", "", "", "", "", "", "", ""] #If the player does have a special attack, this will remove it after they use it - to ensure the player cant stack multiple special attacks
        
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
                    self.fightText.after(3000, lambda: self.updateText("\n\nYou've killed the "+Enemy.name+" and found "+str(gold)+" gold!"))
                    self.fightPage.after(5000, lambda: self.updateText("\n\nExiting..."))
                    self.fightPage.after(6999, self.clearText)
                    self.fightPage.after(7000, lambda: controller.showFrame(MainPage))
                    self.fightPage.after(7000, controller.frames[MainPage].updateInfo)
                    self.fightPage.after(7000, lambda: GameInfo.nextFunction(controller))
                elif GameInfo.location == "town":
                    gold = Enemy.reward
                    Bag.gold += gold
                    self.fightText.after(3000, lambda: self.updateText("\n\nYou've killed the "+Enemy.name+" and earned "+str(gold)+" gold!"))
                    self.fightPage.after(5000, lambda: self.updateText("\n\nExiting..."))
                    self.fightPage.after(6999, self.clearText)
                    controller.frames[ArenaPage].updateInfo()
                    self.fightPage.after(7000, lambda: controller.showFrame(ArenaPage)) 
            elif GameInfo.mode == 2: #if playing quick play
                gold = Enemy.reward
                Bag.gold += gold
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
            if Player.stamina > Player.maxStamina:
                Player.stamina = Player.maxStamina
            self.updateInfo()

    def enemyGold(self, enemyLevel):
        """Choses a random amount of gold to give the player after the monsters is defeated"""
        ranNum = random.randint(0, 30)
        goldRecovered = ranNum*enemyLevel #Amount of gold received based on enemies level
        Bag.gold += goldRecovered
        return goldRecovered

    def buttonState(self, text, curs):
        self.btnBow.configure(state=text, cursor=curs)
        self.btnMelee.configure(state=text, cursor=curs)
        self.btnSmallCal.configure(state=text, cursor=curs)
        self.btnMedCal.configure(state=text, cursor=curs)
        self.btnGrenade.configure(state=text, cursor=curs)
        self.btnSpecial.configure(state=text, cursor=curs)
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


        # self.lblTownPerson = tk.Label(self.townPage, height=5, width=12, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 25")
        # self.lblTownPerson.place(relx=.075, rely=.05)

        self.lblWelcome = tk.Label(self.townPage, height=1, width=25, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 25", text='"Welcome to the Town!"')
        self.lblWelcome.place(relx=.5, rely=.1, anchor="center")

        # self.lblExit = tk.Label(self.townPage, height=1, width=30, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 10", text="Exiting will return to main menu")
        # self.lblExit.place(relx=.38, rely=.15)

        btnArena = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="Arena", font="Arial 25", command=lambda: self.arenaFunction(controller))
        btnArena.place(relx=.5, rely=.3, anchor="center")
        lblArena = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Fight against enemies for gold")
        lblArena.place(relx=.5, rely=.36, anchor="center")

        btnCasino = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="Casino", font="Arial 25",command=lambda: controller.showFrame(BlackPage)) #add reset() function for blackPage
        btnCasino.place(relx=.5, rely=.47, anchor="center")
        lblCasino = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Gamble your gold")
        lblCasino.place(relx=.5, rely=.53, anchor="center")

        btnShop = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="Item Shop", font="Arial 25", command=lambda: controller.showFrame(ShopPage))
        btnShop.place(relx=.5, rely=.64, anchor="center")
        lblShop = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Shop weapons, armour, ammo, and potions")
        lblShop.place(relx=.5, rely=.7, anchor="center")

        btnSchool = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="School", font="Arial 25")
        btnSchool.place(relx=.5, rely=.81, anchor="center")
        lblSchool = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Answer math questions for gold")
        lblSchool.place(relx=.5, rely=.87, anchor="center")
    
    def arenaFunction(self, controller):
        controller.frames[ArenaPage].updateInfo()
        controller.showFrame(ArenaPage)

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
            controller.showFrames[MainPage]
            controller.frames[MainPage].updateInfo()
            GameInfo.nextFunction(controller)
        else:
            controller.showFrame[TownPage]

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
            self.lblOutcome.configure(text="You win "+str(winning)+" Gold!")
        elif int(self.dealerOutcome) > 21: # if dealer busts
            Bag.gold+=bet
            self.lblOutcome.configure(text="You win "+str(bet)+" Gold!")
        elif self.playerOutcome < int(self.dealerOutcome) <= 21: #if dealer has higher sum than player, but not bust
            Bag.gold -= bet
            self.lblOutcome.configure(text="You lose "+str(bet)+" Gold")
        elif self.playerOutcome == self.dealerOutcome:
            self.lblOutcome.configure(text="Push")
        else:
            Bag.gold += bet
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

game = GameApp()

game.mainloop()
