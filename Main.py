try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from PIL import ImageTk, Image
import math
import operator
import time
import random
import threading

"""
IMPORTANT:

https://deckofcardsapi.com/

"""



class PlayerObject:
    def __init__(self, name, age, color, height, weight, sex, armor, maxHealth, health, stamina, maxStamina, mode):
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
    
    def totalHealth(self):
        return self.armor + 100
    
class ArmorObject:
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

class EnemyObject:
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
        for y in range(8):
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
playerWeapons[0] = weapons_list[0]
playerWeapons[1] = weapons_list[10]
playerWeapons[2] = weapons_list[11]
# playerWeapons[3] = weapons_list[19]
playerWeapons[4] = weapons_list[21]
playerWeapons[5] = weapons_list[22]
Enemy = EnemyObject
Armor = ArmorObject

Player = PlayerObject("Calvin", 0, "White", 178, 152, "Man", "none", 100, 100, 100, 100, 2)
Bag = Inventory(200, 0, 100, 0, 0, 2, 2)

# gameMode = 0 #did they click "Story Mode" (1) or "Quick Play" (2)?

class Helper:
    __name__ = 'Helper'
    def __init__(self, func, *args, **kwargs):
        self.gen = func(self.sleep, *args, **kwargs)
        self()

    def __call__(self):
        try:
            next(self.gen)
        except StopIteration:
            pass

    def sleep(self, ms):
        game.after(ms, self)

helper = Helper

class GameApp(tk.Tk):
    
    

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self, height=800, width=1100, bg="black")
        super().minsize(1100, 800) #super refers to the window
        # window.configure()
        window.pack(side="top", fill = "both", expand=True)

        self.frames = {}
        for F in (SplashPage, StartPage, MainPage, FightPage, TownPage, ArenaPage, ShopPage, AmmoPage, ArmorPage, PotionPage, WeaponPage, MeleePage, ArcheryPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.place(height=800, width=1100)
        
        self.showFrame(SplashPage)


    def showFrame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    # def start(self):
    #     self.frames[MainPage].snapBottom()
    #     self.frames[MainPage].clearBox()
    #     self.after(1000, lambda: self.frames[MainPage].updateText("\nYou awaken, laying face down on the forest floor.\nThere's a flipped Jeep to your left, completely charred.\n"))
    #     self.after(8000, lambda: self.frames[MainPage].updateText("\nUnsure of your whereabouts, you hear something rustling only a few feet away.\n"))
    #     self.after(10000, lambda: self.frames[MainPage].updateText("Gradually finding your footing, you approach the source of the noise.\n"))
    #     self.after(12000, lambda: self.frames[MainPage].updateText("You see a Goose pecking at a familiar looking backpack. Within seconds, the goose sees you, flaring out its wings.\n"))
    #     self.after(14000, lambda: self.frames[MainPage].updateText("Looking around quickly, you pick up a stick to defend yourself.\n"))
    #     playerWeapons[0] = weapons_list[0]
    #     self.after(16000, lambda: self.showFrame(FightPage)) #Take this out to make it work
    #     self.after(16001,lambda: self.frames[FightPage].enemyBattle(4,5,"random", "none"))
    #     self.after(20000, lambda: print("hello"))

    def popUp(self):
        popWin = tk.Toplevel()
        label = tk.Label(popWin, text="window")
        label.grid()
        btn = tk.Button(popWin, text="close", command=popWin.destroy)
        btn.grid(row=1)       

    def start(self, sleep):
        
        self.frames[MainPage].snapBottom()
        self.frames[MainPage].clearBox()

        self.frames[MainPage].updateText("\nYou awaken, laying face down on the forest floor.\nThere's a flipped Jeep to your left, completely charred.\n")
        yield sleep(2000)
        # self.popUp()
        self.frames[MainPage].updateText("\nUnsure of your whereabouts, you hear something rustling only a few feet away.\n")
        yield sleep(2000)
        self.frames[MainPage].updateText("Gradually finding your footing, you approach the source of the noise.\n")
        yield sleep(2000)
        self.frames[MainPage].updateText("You see a Goose pecking at a familiar looking backpack. Within seconds, the goose sees you, flaring out its wings.\n")
        yield sleep(2000)
        self.frames[MainPage].updateText("Looking around quickly, you pick up a stick to defend yourself.\n")
        yield sleep(2000)
        playerWeapons[0] = weapons_list[0]

        self.showFrame(FightPage)
        self.frames[FightPage].enemyBattle(4,5,"random", 0)
        
    def part2(self, sleep):
        yield sleep(2000)
        self.frames[MainPage].updateText("\n\ntest\n")
        print("noice")
        

        
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
        # controller.showFrame(StartPage)
        # controller.showFrame(FightPage) #Take this out to make it work
        # controller.frames[FightPage].updateWeapons()
        # controller.frames[FightPage].enemyBattle(1,4,"Cyclopes", 0)
        # controller.start() #take this out to make it work
        # controller.trial(MainPage)

        controller.showFrame(TownPage)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        startPage = tk.Frame(self,width="1100", height="800", bg="black")
        startPage.pack()
        startPage.pack_propagate(0) #prevents frame from shrinking to fit widgets
        textChecker = self.register(self.validInput) #used for max character length in entry widgets

        lblTitle1 = tk.Label(startPage, text="Enter your characters information", font="Arial 30", bg='black', fg="gold")
        lblTitle1.place(relx=0.5, rely=0.07, anchor="center")

        nameVar = tk.StringVar()
        lblName = tk.Label(startPage, text="Name: ", font="Arial 20", fg="gold", bg="black")
        lblName.place(relx=.075, rely=.175)
        entName = tk.Entry(startPage, bg="white", font="Arial 20", width=20, textvariable=nameVar, validate="key", validatecommand=(textChecker,'%P', 15, "letter"))
        entName.place(relx=.22, rely=.175)
        self.validName = tk.Label(startPage, bg="black",fg="gold",text="1-15 letters. No whitespaces",font="Arial 10")
        self.validName.place(relx=.28, rely=.222)

        skinVar = tk.StringVar()
        lblSkinColor = tk.Label(startPage, text="Skin Color: ", font="Arial 20", fg="gold", bg="black")
        lblSkinColor.place(relx=.075, rely=.325)
        entSkinColor = tk.Entry(startPage, bg="white", font="Arial 20", width=20, textvariable=skinVar,validate="key", validatecommand=(textChecker,'%P', 10, "letter"))
        entSkinColor.place(relx=.22, rely=.325)
        self.validSkin = tk.Label(startPage, bg="black",fg="gold",text="3-10 letters. No whitespaces",font="Arial 10")
        self.validSkin.place(relx=.28, rely=.372)

        rbValue = tk.StringVar()
        lblSex = tk.Label(startPage, text="Sex: ", font="Arial 20", fg="gold", bg="black")
        lblSex.place(relx=.075, rely=.475)
        lblBtnMale = tk.LabelFrame(startPage, bd=2, bg="gold")
        lblBtnMale.place(relx=.22, rely=.47)
        rbMale = tk.Radiobutton(lblBtnMale, text="Male", variable=rbValue, value=1, font="Arial 18", bg="black", fg="gold",indicatoron=0,width=21,activebackground="black",activeforeground="gold",selectcolor="#022678",cursor="hand2")
        
        rbMale.pack()
        lblBtnFemale = tk.LabelFrame(startPage, bd=2, bg="gold")
        lblBtnFemale.place(relx=.22, rely=.54)
        rbFemale = tk.Radiobutton(lblBtnFemale, text="Female", variable=rbValue, value=2, font="Arial 18", bg="black", fg="gold", indicatoron=0, width=21,activebackground="black",activeforeground="gold",selectcolor="#61023e",cursor="hand2")
        rbFemale.pack()
        self.validSex = tk.Label(startPage, bg="black",fg="black",text="Select one",font="Arial 10")
        self.validSex.place(relx=.33, rely=.6)
        

        ageVar = tk.StringVar()
        lblAge = tk.Label(startPage, text="Age: ", font="Arial 20", fg="gold", bg="black")
        lblAge.place(relx=.585, rely=.175)
        entAge = tk.Entry(startPage, bg="white", font="Arial 20", width=10, textvariable=ageVar,validate="key", validatecommand=(textChecker,'%P', 2, "number"))
        entAge.place(relx=.7, rely=.175)
        self.validAge = tk.Label(startPage, bg="black",fg="gold",text="18-99",font="Arial 10")
        self.validAge.place(relx=.75, rely=.222)
        lblAgeUnit = tk.Label(startPage, text="years", font="Arial 15", fg="gold", bg="black")
        lblAgeUnit.place(relx=.85, rely=.19)

        heightVar = tk.StringVar()
        lblHeight = tk.Label(startPage, text="Height: ", font="Arial 20", fg="gold", bg="black")
        lblHeight.place(relx=.585, rely=.325)
        entHeight = tk.Entry(startPage, bg="white", font="Arial 20", width=10, textvariable=heightVar,validate="key", validatecommand=(textChecker,'%P', 3, "number"))
        entHeight.place(relx=.7, rely=.325)
        self.validHeight = tk.Label(startPage, bg="black",fg="gold",text="120-300",font="Arial 10")
        self.validHeight.place(relx=.745, rely=.372)
        lblHeightUnit = tk.Label(startPage, text="cm", font="Arial 15", fg="gold", bg="black")
        lblHeightUnit.place(relx=.85, rely=.34)

        weightVar = tk.StringVar()
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

        lblBtnStory = tk.LabelFrame(startPage, bd=5, bg="gold")
        lblBtnStory.place(relx=.1, rely=.8)
        btnStory = tk.Button(lblBtnStory, text="Story Mode", font="Arial 30", relief="solid", bg="black",fg="gold", width=15, activebackground="gold", cursor="hand2", command= lambda: self.modeValidation(controller, nameVar.get(), skinVar.get(), rbValue.get(), ageVar.get(), heightVar.get(), weightVar.get(), 1))
        # btnStory.place(relx=.27, rely=.75, anchor="center")
        btnStory.pack()
        lblBtnQuick = tk.LabelFrame(startPage, bd=5, bg="gold")
        lblBtnQuick.place(relx=.565, rely=.8)
        btnQuick = tk.Button(lblBtnQuick, text="Quick Play", font="Arial 30", relief="solid", bg="black",fg="gold", width=15, activebackground="gold", cursor="hand2", command= lambda: self.modeValidation(controller, nameVar.get(), skinVar.get(), rbValue.get(), ageVar.get(), heightVar.get(), weightVar.get(), 2))
        # btnQuick.place(relx=.73, rely=.75, anchor="center")
        btnQuick.pack()

    def modeValidation(self, controller, nameVar, skinVar, rbValue, ageVar, heightVar, weightVar, btnValue):
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
                    Player.sex = "man"
                elif rbValue == 2:
                    Player.sex == "woman"
                Player.name = nameVar
                Player.age = int(ageVar)
                Player.color = skinVar
                Player.height = int(heightVar)
                Player.weight = int(weightVar)
                Player.mode = btnValue
                if btnValue == 1:
                    controller.showFrame(MainPage)
                    helper(controller.start)
                elif btnValue == 2:
                    controller.showFrame(TownPage)
    
                # controller.start()
                # controller.frames[MainPage].updateText()
                
    def validInput(self, text, maxLength, type):
        if text:
            if type == "letter":
                return len(text) <= int(maxLength) and text.isalpha()
            elif type == "number":
                return len(text) <= int(maxLength) and text.isdigit()
        return True
    def trial1():
        print("trial")
            
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.mainPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.mainPage.pack()
        self.mainPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.mainText = tk.Text(self.mainPage, state="disabled", height=16, width=75, bg="black", highlightbackground="gold", highlightcolor="gold", highlightthickness=2, fg="white", font="Arial 15", wrap="word")
        self.mainText.place(relx=.5, rely=.4, anchor="center")

        self.btnHealth = tk.Button(self.mainPage, height=6, width=16, relief="raised", cursor="hand2")
        self.btnHealth.place(relx=.3, rely=.85, anchor="w")

        self.lblHealth = tk.Label(self.mainPage, height=3, width=20, bg="#1a1a1a",fg="white", font="Arial 20", text="Health : "+str(Player.health)+"/"+str(Player.maxHealth))
        self.lblHealth.place(relx=.2, rely=.1, anchor="center")

        self.lblStamina = tk.Label(self.mainPage, height=3, width=20, bg="#1a1a1a", fg="white", font="Arial 20", text = "Stamina: "+str(Player.stamina)+"/"+str(Player.maxStamina))
        self.lblStamina.place(relx=.6, rely=.1, anchor="center")
       
        
    def updateText(self, text): #displays the text in the text box
        self.mainText.configure(state="normal")
        self.mainText.insert(tk.END, text)
        self.mainText.configure(state="disabled")

    # def story(self):
        # self.after(2000, lambda: self.updateText("first"))
        # self.after(3000, lambda: self.updateText("second")) 
    def snapBottom(self):
        self.mainText.see("end")
        self.after(1000, self.snapBottom)
    
    def clearBox(self):
        if self.mainText.yview == (0.0, 1.0):
            print("hello")
            self.mainText.configure(state="normal")
            self.mainText.delete(0.0, "end")
            self.mainText.configure(state="disabled")
        self.after(1000, self.clearBox)
        
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
                playerWeapons[5] = ["", "", "", "", "", "", "", "", ""] #If the player does have a special attack, this will remove it after they use it - to ensure the player cant stack multiple special attacks
        
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
            if Player.mode == 1: #If playing story mode
                gold = self.enemyGold(Enemy.level)
                Bag.gold += gold
                self.fightText.after(3000, lambda: self.updateText("\n\nYou've killed the "+Enemy.name+" and found "+str(gold)+" gold!"))
                self.fightPage.after(5000, lambda: self.updateText("\n\nExiting..."))
                self.fightPage.after(6999, self.clearText)
                self.fightPage.after(7000, lambda: controller.showFrame(MainPage))
            elif Player.mode == 2: #if playing quick play
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

        btnArena = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="Arena", font="Arial 25", command=lambda: controller.showFrame(ArenaPage))
        btnArena.place(relx=.5, rely=.3, anchor="center")
        lblArena = tk.Label(self.townPage, height=1, width=40, fg="white", bg="#1a1a1a", text="Fight against enemies for gold")
        lblArena.place(relx=.5, rely=.36, anchor="center")

        btnCasino = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="Casino", font="Arial 25")
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

class ArenaPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.arenaPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.arenaPage.pack()
        self.arenaPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

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

        self.lblBowPic = tk.Label(self.ammoPage, bg="#909090")
        self.lblBowPic.place(relx=.57, rely=.202)
        self.lblBowAmt = tk.Label(self.ammoPage, width = 18, height=4, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Arrow Count: "+str(Bag.arrows))
        self.lblBowAmt.place(relx=.70, rely=.200)
        self.lblBowName = tk.Label(self.ammoPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=playerWeapons[1][1])
        self.lblBowName.place(relx=.55, rely=.325)

        self.lblSCalPic = tk.Label(self.ammoPage, bg="#909090")
        self.lblSCalPic.place(relx=.57, rely=.402)
        self.lblSCalAmt = tk.Label(self.ammoPage, width = 18, height=4, bg = "#1a1a1a", fg="white", font="Arial 15",anchor="w", text="9mm Rounds: "+str(Bag.scaliber))
        self.lblSCalAmt.place(relx=.70, rely=.400)
        self.lblSCalGunName = tk.Label(self.ammoPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=playerWeapons[2][1])
        self.lblSCalGunName.place(relx=.55, rely=.525)

        self.lblMCalPic = tk.Label(self.ammoPage, bg="#909090")
        self.lblMCalPic.place(relx=.57, rely=.617)
        self.lblMCalAmt = tk.Label(self.ammoPage, width = 18, height=4, bg = "#1a1a1a", fg="white", font="Arial 15",anchor="w", text="7.62mm Rounds: "+str(Bag.lcaliber))
        self.lblMCalAmt.place(relx=.70, rely=.615)
        self.lblMCalGunName = tk.Label(self.ammoPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=playerWeapons[3][1])
        self.lblMCalGunName.place(relx=.55, rely=.740)

        self.lblGrenadesPic = tk.Label(self.ammoPage, bg="#909090",text=playerWeapons[4][1])
        self.lblGrenadesPic.place(relx=.57, rely=.807)
        self.lblGrenadesAmt = tk.Label(self.ammoPage, width = 18, height=4, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Grenades: "+str(Bag.grenades))
        self.lblGrenadesAmt.place(relx=.70, rely=.805)
        self.lblGrenadesGunName = tk.Label(self.ammoPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text="Grenade")
        self.lblGrenadesGunName.place(relx=.55, rely=.93)

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
                self.lblMCalPic.configure(width=14, height=6, text="Empty Slot")
            else:
                self.lblMCalPic.configure(width=14, height=6, text="Image")
        self.lblBowName.configure(text=playerWeapons[1][1])

        try:
            self.picSCalGun = ImageTk.PhotoImage(Image.open(playerWeapons[2][9]))
            self.lblSCalPic.configure(width=100, height=90, image=self.picSCalGun)
        except:
            if playerWeapons[2][1] == "":
                self.lblMCalPic.configure(width=14, height=6, text="Empty Slot")
            else:
                self.lblMCalPic.configure(width=14, height=6, text="Image")
        self.lblSCalGunName.configure(text=playerWeapons[2][1])

        try:
            self.picMCalGun = ImageTk.PhotoImage(Image.open(playerWeapons[3][9]))
            self.lblMCalPic.configure(width=100, height=90, image=self.picMCalGun)
        except:
            if playerWeapons[3][1] == "":
                self.lblMCalPic.configure(width=14, height=6, text="Empty Slot")
            else:
                self.lblMCalPic.configure(width=14, height=6, text="Image")
        self.lblMCalGunName.configure(text=playerWeapons[3][1])

        try:
            self.picGrenadesGun = ImageTk.PhotoImage(Image.open(playerWeapons[4][9]))
            self.lblGrenadesPic.configure(width=100, height=90, image=self.picGrenadesGun)
        except:
            if playerWeapons[4][1] == "":
                self.lblMCalPic.configure(width=14, height=6, text="Empty Slot")
            else:
                self.lblMCalPic.configure(width=14, height=6, text="Image")

class ArmorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.armorPage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.armorPage.pack()
        self.armorPage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.armorPage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: self.exitPage(controller))
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

        self.lblPlayer = tk.Button(self.armorPage, bg="#909090", cursor="hand2")
        self.lblPlayer.place(relx=.765, rely=.25)

        try:
            self.picPlayer = ImageTk.PhotoImage(Image.open(Armor.image))
            self.lblPlayer.configure(width=150, height=160, image=self.picPlayer)
        except:
            self.lblPlayer.configure(width=13, height=6,font="Arial 15")

        self.lblPlayerArmor = tk.Label(self.armorPage, width = 12, height=1, bg = "#1a1a1a", fg="white", font="Arial 17", text=Armor.name)
        self.lblPlayerArmor.place(relx=.762, rely=.2)
        self.lblPlayerArmorHealth = tk.Label(self.armorPage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text="+"+str(Armor.healthBonus)+" Health")
        self.lblPlayerArmorHealth.place(relx=.758, rely=.47)
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
        self.updateClearColor()
        self.goldTitle.configure(text="Gold: "+str(Bag.gold))
        try:
            self.picPlayer = ImageTk.PhotoImage(Image.open(Armor.image))
            self.lblPlayer.configure(width=150, height=160, image=self.picPlayer)
        except:
            self.lblPlayer.configure(width=13, height=6,font="Arial 15")
        self.lblPlayerArmor.configure(text=Armor.name)
        self.lblPlayerArmorHealth.configure(text="+"+str(Armor.healthBonus)+" Health")
        self.lblHealth.configure(text=Player.name+"'s Health: ")
        self.lblPHealth.configure(text=str(Player.health)+" / "+str(Player.maxHealth))
    
    def exitPage(self, controller):
        self.lblInvalid.configure(text="")
        controller.showFrame(ShopPage)

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
        
        btnMCal = tk.Button(self.weaponPage, bg="grey", fg="white", height=1, width=20, text="Rifles", font="Arial 25")
        btnMCal.place(relx=.5, rely=.70, anchor="center")

        btnSpecial = tk.Button(self.weaponPage, bg="grey", fg="white", height=1, width=20, text="Special", font="Arial 25")
        btnSpecial.place(relx=.5, rely=.85, anchor="center")
    
    def meleeFunction(self, controller):
        controller.frames[MeleePage].updateInfo()
        controller.showFrame(MeleePage)

    def archeryFunction(self, controller):
        controller.frames[ArcheryPage].updateInfo()
        controller.showFrame(ArcheryPage)
    
    # def sidearmFunction(self, controller):
    #     controller.frames[SidearmPage].updateInfo()
    #     controller.showFrame(SidearmPage)
        
class MeleePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.meleePage = tk.Frame(self,width=1100, height=800, bg="#1a1a1a")
        self.meleePage.pack()
        self.meleePage.pack_propagate(0) #prevents frame from shrinking to fit widgets

        self.btnBack = tk.Button(self.meleePage, width=10, height=1, text="Return", bg="#909090", fg="white", font="Arial 15", cursor="hand2", command=lambda: controller.showFrame(ShopPage))
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

        self.lblmeleePic = tk.Label(self.meleePage, bg="#909090")
        self.lblmeleePic.place(relx=.77, rely=.3)
        self.lblmeleeDamage = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblmeleeDamage.place(relx=.729, rely=.45)
        self.lblmeleeStam = tk.Label(self.meleePage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblmeleeStam.place(relx=.729, rely=.5)
        self.lblmeleeName = tk.Label(self.meleePage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 18")
        self.lblmeleeName.place(relx=.73, rely=.23)

        self.lblStamina = tk.Label(self.meleePage, width = 15, height=1, bg = "#1a1a1a", fg="white", font="Arial 15",justify="left", text=Player.name+"'s Stamina: ")
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

        self.lblBowPic = tk.Label(self.archeryPage, bg="#909090")
        self.lblBowPic.place(relx=.674, rely=.405)
        self.lblBowDamage = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblBowDamage.place(relx=.633, rely=.555)
        self.lblBowArrow = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblBowArrow.place(relx=.633, rely=.605)
        self.lblBowStam = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblBowStam.place(relx=.633, rely=.655)
        self.lblBowName = tk.Label(self.archeryPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 18")
        self.lblBowName.place(relx=.634, rely=.335)

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

class RiflePage(tk.Frame):
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

        self.btnCompound = tk.Button(self.archeryPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(4))
        self.btnCompound.place(relx=.22, rely=.2)
        try:
            self.picCompound = ImageTk.PhotoImage(Image.open(weapons_list[8][9]))
            self.btnCompound.configure(width=100, height=90, image=self.picCompound)
        except:
            self.btnCompound.configure(width=13, height=6, text=weapons_list[8][1])

        self.lblCompoundDamage = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[8][2])+" - "+str(weapons_list[8][3]))
        self.lblCompoundDamage.place(relx=.34, rely=.203)
        self.lblCompoundStam = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[8][5]))
        self.lblCompoundStam.place(relx=.34, rely=.243)
        self.lblCompoundCost = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[8][8])+" gold")
        self.lblCompoundCost.place(relx=.34, rely=.283)
        self.lblCompoundName = tk.Label(self.archeryPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[8][1])
        self.lblCompoundName.place(relx=.203, rely=.333)

        self.btnRecurve = tk.Button(self.archeryPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(5))
        self.btnRecurve.place(relx=.22, rely=.4)
        try:
            self.picRecurve = ImageTk.PhotoImage(Image.open(weapons_list[9][9]))
            self.btnRecurve.configure(width=100, height=90, image=self.picRecurve)
        except:
            self.btnRecurve.configure(width=13, height=6, text=weapons_list[9][1])

        self.lblRecurveDamage = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[9][2])+" - "+str(weapons_list[9][3]))
        self.lblRecurveDamage.place(relx=.34, rely=.403)
        self.lblRecurveStam = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[9][5]))
        self.lblRecurveStam.place(relx=.34, rely=.443)
        self.lblRecurveCost = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[9][8])+" gold")
        self.lblRecurveCost.place(relx=.34, rely=.483)
        self.lblRecurveName = tk.Label(self.archeryPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[9][1])
        self.lblRecurveName.place(relx=.203, rely=.533)

        self.btnCrossbow = tk.Button(self.archeryPage, bg="#909090",text="Arrows", activebackground="#909090", cursor="hand2", relief="solid", borderwidth=5, command=lambda: self.purchaseMelee(6))
        self.btnCrossbow.place(relx=.22, rely=.6)
        try:
            self.picCrossbow = ImageTk.PhotoImage(Image.open(weapons_list[10][9]))
            self.btnCrossbow.configure(width=100, height=90, image=self.picCrossbow)
        except:
            self.btnCrossbow.configure(width=13, height=6, text=weapons_list[10][1])

        self.lblCrossbowDamage = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Damage: "+str(weapons_list[10][2])+" - "+str(weapons_list[10][3]))
        self.lblCrossbowDamage.place(relx=.34, rely=.603)
        self.lblCrossbowStam = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Stamina: "+str(weapons_list[10][5]))
        self.lblCrossbowStam.place(relx=.34, rely=.643)
        self.lblCrossbowCost = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", anchor="w", text="Cost: "+str(weapons_list[10][8])+" gold")
        self.lblCrossbowCost.place(relx=.34, rely=.683)
        self.lblCrossbowName = tk.Label(self.archeryPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 15", text=weapons_list[10][1])
        self.lblCrossbowName.place(relx=.203, rely=.733)

        self.inventoryTitle = tk.Label(self.archeryPage, width = 20,height=1, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3, text=Player.name+"'s Inventory")
        self.inventoryTitle.place(relx=.57, rely=.12)

        self.inventory = tk.Label(self.archeryPage, width = 20, height=20, bg="#1a1a1a", fg="white", font="Arial 20",highlightbackground="black",highlightthickness=3)
        self.inventory.place(relx=.57, rely=.17)

        self.lblBowPic = tk.Label(self.archeryPage, bg="#909090")
        self.lblBowPic.place(relx=.674, rely=.405)
        self.lblBowDamage = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblBowDamage.place(relx=.633, rely=.555)
        self.lblBowStam = tk.Label(self.archeryPage, width = 17, height=1, bg = "#1a1a1a", fg="white", font="Arial 15")
        self.lblBowStam.place(relx=.633, rely=.605)
        self.lblBowName = tk.Label(self.archeryPage, width = 13, height=1, bg = "#1a1a1a", fg="white", font="Arial 18")
        self.lblBowName.place(relx=.634, rely=.335)

    def purchaseMelee(self, index):
        self.updateClearColor()
        if playerWeapons[0][1] == weapons_list[index][1]:
            self.lblBowName.configure(fg="#157528")
        elif Bag.gold < weapons_list[index][8]:
            if index == 0:
                self.lblCompoundCost.configure(fg="gold")
            elif index == 1:
                self.lblRecurveCost.configure(fg="gold")
            elif index == 2:
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

        self.lblBowName.configure(text=playerWeapons[0][1])
        self.lblBowDamage.configure(text="Damage: "+str(playerWeapons[1][2])+" - "+str(playerWeapons[1][3]))
        self.lblBowStam.configure(text="Stamina: "+str(playerWeapons[1][5]))

game = GameApp()

game.mainloop()
