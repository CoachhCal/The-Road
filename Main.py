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
    def __init__(self, name, age, color, height, weight, sex, armor, max_health, health, stamina, max_stamina, mode):
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
        self.mode = mode
    
    def total_health(self):
        return self.armor + self.max_health
    
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
ammo_list = list_from_csv("csvFiles/ammo_list.csv", "r")
armor_list = list_from_csv("csvFiles/armor_list.csv", "r")
potionList = list_from_csv("csvFiles/potions_list.csv", "r")
cards_list = list_from_csv("csvFiles/cards_list.csv", "r")
# except:


playerWeapons = create_player_weapon_list()
playerWeapons[0] = weapons_list[0]
playerWeapons[1] = weapons_list[8]
playerWeapons[2] = weapons_list[14]
playerWeapons[3] = weapons_list[20]
playerWeapons[4] = weapons_list[21]
playerWeapons[5] = weapons_list[22]
Enemy = EnemyObject

Player = PlayerObject("Calvin", 0, "White", 178, 152, "Man", "none", 100, 100, 100, 100, 2)
Bag = Inventory(1000, 0, 100, 0, 0, 0, 0)

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
        for F in (SplashPage, StartPage, MainPage, FightPage, TownPage, ArenaPage):
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
        # controller.frames[FightPage].enemyBattle(4,5,"random", "none")
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

        self.lblHealth = tk.Label(self.mainPage, height=3, width=20, bg="#1a1a1a",fg="white", font="Arial 20", text="Health : "+str(Player.health)+"/"+str(Player.max_health))
        self.lblHealth.place(relx=.2, rely=.1, anchor="center")

        self.lblStamina = tk.Label(self.mainPage, height=3, width=20, bg="#1a1a1a", fg="white", font="Arial 20", text = "Stamina: "+str(Player.stamina)+"/"+str(Player.max_stamina))
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
        self.lblEnemyPic.place(relx=.05, rely=.05)

        self.lblEnemyHealth = tk.Label(self.fightPage, height=1, width=25, bg="#751515", fg="white", font="Arial 15")
        self.lblEnemyHealth.place(relx=.05, rely=.359)

        self.lblAddEH = tk.Label(self.fightPage, height=1, width=2, bg="#751515", font="Arial 15")
        self.lblAddEH.place(relx=.2845, rely=.359)

        self.lblEnemyName = tk.Label(self.fightPage, height=1, width=25, bg="black", fg="white", font="Arial 15")
        self.lblEnemyName.place(relx=.05, rely=.05)

        self.lblAddEN = tk.Label(self.fightPage, height=1, width=2, bg="black", font="Arial 15")
        self.lblAddEN.place(relx=.2845, rely=.05)

        # self.lblEnemyHealth = tk.Label(self.lblEnemyPic, height=1, width=25, bg="blue", fg="white", font="Arial 15")
        # self.lblEnemyHealth.place(relx=.0000, rely=.9)

        self.lblInventory = tk.Label(self.fightPage, height=18, width=75, bg="black")
        self.lblInventory.place(relx=.45, rely=.05)

        # canvas = tk.Canvas(self.fightPage, width=526, height=1)
        # canvas.place(relx=.45, rely=.095)

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

        self.lblSpecial = tk.Label(self.fightPage, height=3, width=20, bg="black", fg="white", font="Arial 15", text="Special:\n"+str(playerWeapons[5][1]), anchor='nw', justify="left", wraplength=250, )
        self.lblSpecial.place(relx=.70, rely=.12)

        self.lblHealthPot = tk.Label(self.fightPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Health Potions: "+str(Bag.healthPotion), anchor='w')
        self.lblHealthPot.place(relx=.70, rely=.24)

        self.lblStaminaPot = tk.Label(self.fightPage, height=1, width=18, bg="black", fg="white", font="Arial 15", text="Stamina Potions: "+str(Bag.staminaPotion), anchor='w')
        self.lblStaminaPot.place(relx=.70, rely=.30)

        self.lblPHealth = tk.Label(self.fightPage, height=1, width=24, bg="#751515", fg="white", font="Arial 15", text="Health: "+str(Player.health)+"/"+str(Player.max_health))
        self.lblPHealth.place(relx=.45, rely=.359)

        self.lblPStamina = tk.Label(self.fightPage, height=1, width=24, bg="#157528", fg="white", font="Arial 15", text="Stamina: "+str(Player.stamina)+"/"+str(Player.max_stamina))
        self.lblPStamina.place(relx=.687, rely=.359)

        self.fightText = tk.Text(self.fightPage, height=9, width=60, state="disabled", bg="black", fg="white", font="Arial 18", padx=25)
        self.fightText.tag_configure("center", justify='center', spacing1=5)
        self.fightText.tag_add("center", 1.0, "end")
        self.fightText.place(relx=.05, rely=.445)
       

        self.btnMelee = tk.Button(self.fightPage, width=13, height=6, bg="grey",text="Melee", cursor="hand2", command=lambda: self.playerAttack(0, controller))
        self.btnMelee.place(relx=.08, rely=.81)

        self.btnBow = tk.Button(self.fightPage, width=13, height=6, bg="grey",text="Bow",cursor="hand2", command=lambda: self.playerAttack(1, controller))
        self.btnBow.place(relx=.21, rely=.81)

        self.btnSmallCal = tk.Button(self.fightPage, width=13, height=6, bg="grey",text= "Sidearm",cursor="hand2", command=lambda: self.playerAttack(2, controller))
        self.btnSmallCal.place(relx=.34, rely=.81)

        self.btnMedCal = tk.Button(self.fightPage, width=13, height=6, bg="grey",text="Rifle",cursor="hand2", command=lambda: self.playerAttack(3, controller))
        self.btnMedCal.place(relx=.47, rely=.81)

        self.btnGrenade = tk.Button(self.fightPage, width=13, height=6, bg="grey",text="Grenade",cursor="hand2", command=lambda: self.playerAttack(4, controller))
        self.btnGrenade.place(relx=.60, rely=.81)

        self.btnSpecial = tk.Button(self.fightPage, width=13, height=6, bg="grey",text="Special",cursor="hand2", command=lambda: self.playerAttack(5, controller))
        self.btnSpecial.place(relx=.73, rely=.81)

        self.btnFlee = tk.Button(self.fightPage, width=13, height=6,cursor="hand2",text="Flee", bg="grey")
        self.btnFlee.place(relx=.86, rely=.81)

        self.btnHealth = tk.Button(self.fightPage, width=13, height=6,cursor="hand2",text="Health Pot", bg="grey", command= self.healthPotion)
        self.btnHealth.place(relx=.86, rely=.44)

        self.btnStamina = tk.Button(self.fightPage, width=13, height=6,cursor="hand2", bg="grey", text="Stamina Pot", command = self.staminaPotion)
        self.btnStamina.place(relx=.86, rely=.63)

    def enemyBattle(self, minEnemyLvl, maxEnemyLvl, nameOrRandom, zeroOrGoldAmt):
        self.enemySelector(minEnemyLvl, maxEnemyLvl, nameOrRandom, zeroOrGoldAmt)
        
        self.lblEnemyName.configure(text = Enemy.name)
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

    
    def playerAttack(self,index, controller):
        self.buttonState("disabled", "x_cursor")
        successfulAttack = False
        if playerWeapons[index] == "":
            self.clearText()
            self.updateText("Empty weapon slot")
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
                playerWeapons[5] = ["", "", "", "", "", "", "", ""] #If the player does have a special attack, this will remove it after they use it - to ensure the player cant stack multiple special attacks
        
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
        elif Player.health == Player.max_health:
            self.clearText()
            self.updateText("\n\nAlready at max health")
        else:
            Player.health += potionList[0][1]
            if Player.health > Player.max_health:
                Player.health == Player.max_health
    
    def staminaPotion(self):
        if Bag.staminaPotion == 0:
            self.clearText()
            self.updateText("\nInsufficient stamina potions\n\nYou have: "+str(Bag.staminaPotion)+"\nRequired amount: 1")
        elif Player.stamina == Player.maxStamina:
            self.clearText()
            self.updateText("\n\nAlready at max stamina")
        else:
            Player.stamina += potionList[1][1]
            if Player.stamina > Player.maxStamina:
                Player.stamina == Player.maxStamina

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
        self.lblSpecial.configure(text="Special:\n"+str(playerWeapons[5][1]))
        self.lblHealthPot.configure(text="Health Potions: "+str(Bag.healthPotion))
        self.lblStaminaPot.configure(text="Stamina Potions: "+str(Bag.staminaPotion))
        self.lblPHealth.configure(text="Health: "+str(Player.health)+"/"+str(Player.max_health))
        self.lblPStamina.configure(text="Stamina: "+str(Player.stamina)+"/"+str(Player.max_stamina))
        

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

        btnShop = tk.Button(self.townPage, bg="grey", fg="white", height=1, width=20, text="Item Shop", font="Arial 25")
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

        self.lblPHealth = tk.Label(self.arenaPage, height=1, width=18, bg="#751515", fg="white", font="Arial 15", text="Health: "+str(Player.health)+"/"+str(Player.max_health))
        self.lblPHealth.place(relx=.175, rely=.84)

        self.lblPStamina = tk.Label(self.arenaPage, height=1, width=17, bg="#157528", fg="white", font="Arial 15", text="Stamina: "+str(Player.stamina)+"/"+str(Player.max_stamina))
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
        self.lblPHealth.configure(text="Health: "+str(Player.health)+"/"+str(Player.max_health))
        self.lblPStamina.configure(text="Stamina: "+str(Player.stamina)+"/"+str(Player.max_stamina))

game = GameApp()

game.mainloop()
