try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from PIL import ImageTk, Image
import math
import operator
import time
import random

"""
IMPORTANT:
Splash Page button command has replaced StartPage with MainPage to skip the character input

"""

class PlayerObject:
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
    
class Inventory:
    def __init__(self, gold, arrows, scaliber, lcaliber, grenades, health_potion, stamina_potion):
        self.gold = gold
        self.arrows = arrows
        self.scaliber = scaliber
        self.lcaliber = lcaliber
        self.grenades = grenades
        self.health_potion = health_potion
        self.stamina_potion = stamina_potion

class EnemyObject:
    level = 0
    name = "none"
    health = 0
    attack1 = ["name", 0,1]
    attack2 = ["name", 0,1]
    attack3 = ["name", 0,1]
    finalMove = "none"

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
potion_list = list_from_csv("csvFiles/potions_list.csv", "r")
cards_list = list_from_csv("csvFiles/cards_list.csv", "r")
# except:


playerWeapons = create_player_weapon_list()
Enemy = EnemyObject

Player = PlayerObject("Calvin", 0, "White", 178, 152, "Man", "none", 100, 100, 100, 100)
Bag = Inventory(100, 0, 0, 0, 0, 0, 0)

class GameApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self, height=800, width=1100, bg="black")
        super().minsize(1100, 800) #super refers to the window
        # window.configure()
        window.pack(side="top", fill = "both", expand=True)

        self.frames = {}
        for F in (SplashPage, StartPage, MainPage, FightPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.place(height=800, width=1100)
        
        self.showFrame(SplashPage)


    def showFrame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def start(self):
        self.frames[MainPage].snapBottom()
        self.frames[MainPage].clearBox()
        self.after(1000, lambda: self.frames[MainPage].updateText("\nYou awaken, laying face down on the forest floor.\nThere's a flipped Jeep to your left, completely charred.\n"))
        self.after(10000, lambda: self.frames[MainPage].updateText("\nUnsure of your whereabouts, you hear something rustling only a few feet away.\n"))
        self.after(15000, lambda: self.frames[MainPage].updateText("Gradually finding your footing, you approach the source of the noise.\n"))
        self.after(20000, lambda: self.frames[MainPage].updateText("You see a Goose pecking at a familiar looking backpack. Within seconds, the goose sees you, flaring out its wings.\n"))
        self.after(27000, lambda: self.frames[MainPage].updateText("Looking around quickly, you pick up a stick to defend yourself.\n"))
        playerWeapons[0] = weapons_list[0]

        
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
        controller.showFrame(FightPage) #Take this out to make it work
        controller.frames[FightPage].enemySelector(1,2,"random")
        # controller.start() #take this out to make it work
        # controller.trial(MainPage)


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
        btnStory = tk.Button(lblBtnStory, text="Story Mode", font="Arial 30", relief="solid", bg="black",fg="gold", width=15, activebackground="gold", cursor="hand2", command= lambda: self.storyModeValidation(controller, nameVar.get(), skinVar.get(), rbValue.get(), ageVar.get(), heightVar.get(), weightVar.get()))
        # btnStory.place(relx=.27, rely=.75, anchor="center")
        btnStory.pack()
        lblBtnQuick = tk.LabelFrame(startPage, bd=5, bg="gold")
        lblBtnQuick.place(relx=.565, rely=.8)
        btnQuick = tk.Button(lblBtnQuick, text="Quick Play", font="Arial 30", relief="solid", bg="black",fg="gold", width=15, activebackground="gold", cursor="hand2")
        # btnQuick.place(relx=.73, rely=.75, anchor="center")
        btnQuick.pack()

    def storyModeValidation(self, controller, nameVar, skinVar, rbValue, ageVar, heightVar, weightVar):
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
                controller.showFrame(MainPage)
                controller.start()
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

        lblEnemyPic = tk.Label(self.fightPage, height=18, width=40, bg="black")
        lblEnemyPic.place(relx=.08, rely=.05)

        lblInventory = tk.Label(self.fightPage, height=18, width=75, bg="black")
        lblInventory.place(relx=.45, rely=.05)

        lblFightText = tk.Text(self.fightPage, height=16, width=100, bg="black")
        lblFightText.place(relx=.447, rely=.6, anchor="center")

        btnMelee = tk.Button(self.fightPage, width=15, height=6, bg="grey")
        btnMelee.place(relx=.08, rely=.81)

        btnBow = tk.Button(self.fightPage, width=15, height=6, bg="grey")
        btnBow.place(relx=.23, rely=.81)

        btnSmallCal = tk.Button(self.fightPage, width=15, height=6, bg="grey")
        btnSmallCal.place(relx=.38, rely=.81)

        btnMedCal = tk.Button(self.fightPage, width=15, height=6, bg="grey")
        btnMedCal.place(relx=.53, rely=.81)

        btnSpecial = tk.Button(self.fightPage, width=15, height=6, bg="grey")
        btnSpecial.place(relx=.68, rely=.81)

        btnFlee = tk.Button(self.fightPage, width=15, height=6, bg="grey")
        btnFlee.place(relx=.68, rely=.96)

        btnHealth = tk.Button(self.fightPage, width=15, height=6, bg="grey")
        btnHealth.place(relx=.85, rely=.44)

        btnStamina = tk.Button(self.fightPage, width=15, height=6, bg="grey")
        btnStamina.place(relx=.85, rely=.63)

    def enemyBattle(self, minEnemyLvl, maxEnemyLvl, nameOrRandom, goldOrNone):
        self.enemySelector(minEnemyLvl, maxEnemyLvl, nameOrRandom)


    def enemySelector(self,minEnemyLvl, maxEnemyLvl, nameOrRandom):
        """Chooses a monster from a 2D list"""
        if nameOrRandom != "random":
            for x in range(len(monsterList)): #Goes through the list looking for the correct monsters name. Once found, the details of the monster is assigned to the monster_index variable
                if monsterList[x][1] == nameOrRandom: #If the correct enemy is found
                    selectedEnemy = monsterList[x]
                    self.updateEnemyObject(selectedEnemy)
        else:
            x = 0
            while x < 100:
                selectedEnemy = monsterList[random.randint(0, len(monsterList)-1)] #Chooses a random monster from the list
                if minEnemyLvl <= selectedEnemy[0] <= maxEnemyLvl: #Checks to see of the chosen monster is the right level
                    self.updateEnemyObject(selectedEnemy)
                else:
                    x += 1

    def updateEnemyObject(self, enemy):
        Enemy.level = enemy[0]
        Enemy.name = enemy[1]
        Enemy.health = enemy[2]
        Enemy.attack1 = [enemy[3], enemy[4], enemy[5]]
        Enemy.attack2 = [enemy[6], enemy[7], enemy[8]]
        Enemy.attack3 = [enemy[9], enemy[10], enemy[11]]
        Enemy.finalMove = enemy[12]

game = GameApp()

game.mainloop()
