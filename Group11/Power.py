#---------------------------- IMPORTS ----------------------------------------------
from asyncio import events
from email.mime import image
import tkinter as tk
from tokenize import Pointfloat
from turtle import up 
import winsound
import random
#---------------------------- CONSTANT ---------------------------------------------

WINDOW_WIDTH = 1430 
WINDOW_HEIGHT = 750 

#------------------------------ MAIN -----------------------------------------------
root = tk.Tk()  
root.geometry( str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
root.title("Yummy")
icon=tk.PhotoImage(file="images\Amung us.png")
root.iconphoto(True,icon)
canvas = tk.Canvas(root)
medicine = tk.PhotoImage(file="images\Medicine.png")
doctor = tk.PhotoImage(file="images\Doctor.png")
chose= tk.PhotoImage(file="images\Choselevel.png")
level1bg= tk.PhotoImage(file="images\Level1bg.png")
bgwin= tk.PhotoImage(file="images\Bgwin.png")
doctorlevel =tk.PhotoImage(file="images\Doctorlevel2.png")
boxlevel= tk.PhotoImage(file="images\Box level1.png")
bglose= tk.PhotoImage(file="images\Bglose.png")
virus = tk.PhotoImage(file="images\Virus.png")
#----------------------------------- Fruits-----------------------------------------------------
banana = tk.PhotoImage(file = "images\Banana.png")
apple = tk.PhotoImage(file = "images\Apple.png")
mango = tk.PhotoImage(file = "images\Mango1.png")
water = tk.PhotoImage(file = "images\Water.png")
carrot = tk.PhotoImage(file = "images\Carrot.png")
coconut = tk.PhotoImage(file = "images\Coconut.png")

#_______________________________________________Some style________________________
Rule= tk.PhotoImage(file='images\Rule.png')
intruction = tk.PhotoImage(file="images\Intruction1.png")
stylewooden = tk.PhotoImage(file="images\Stylewooden.png")
bgupdate = tk.PhotoImage(file="images\Bgupdate.png")
rlud = tk.PhotoImage(file="images\RLUD.png")

#__________________________________grid_______________________________________________

gridlevel1 =[[5, 5,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 6, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [5, 0, 0, 4, 0, 0, 3, 3, 7, 0, 3, 0, 5, 0, 7, 5, 0, 0, 7, 5, 5, 0, 0, 5],
        [5, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 5, 3, 4, 5, 0, 3, 0, 5, 2, 0, 0, 5],
        [5, 0, 0, 0, 0, 3, 3, 0, 0, 4, 0, 0, 5, 5, 5, 5, 0, 0, 0, 5, 5, 0, 0, 5],
        [5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 4, 0, 0, 3, 0, 0, 0, 5, 0, 5],
        [5, 0, 0, 0, 0, 5, 0, 0, 5, 4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [5, 0, 0, 5, 7, 5, 0, 0, 5, 0, 0, 7, 0, 0, 4, 0, 0, 0, 5, 0, 0, 0, 0, 5],
        [5, 0, 0, 5, 4, 5, 7, 3, 5, 5, 5, 0, 0, 7, 3, 0, 5, 5, 5, 0, 0, 0, 0, 5],
        [5, 0, 0, 5, 5, 5, 5, 5, 5, 0, 7, 0, 0, 0, 0, 3, 5, 3, 0, 0, 0, 0, 0, 5],
        [5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 4, 0, 7, 2, 4, 0, 5, 5, 5, 5, 0, 0, 0, 5],
        [5, 0, 0, 0, 0, 4, 0, 7, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0, 0, 0, 5],
        [5, 0, 0, 3, 0, 0, 0, 0, 0, 5, 0, 5, 5, 5, 5, 0, 4, 0, 0, 0, 0, 0, 0, 5],
        [5, 0, 0, 0, 0, 0, 0, 0, 7, 0, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]

#--------------------------------- functions ---------------------------------------------
notWin = True
def drawing1():
    if notWin:
        global timelabel,powerLabel,power
        canvas.delete("doctor1")
        for row in range(len(gridlevel1)):
            for column in range(len(gridlevel1[row])):
                if gridlevel1[row][column] == 1:
                    canvas.create_image(100 + column*35, row*35 + 97, image = doctorlevel ,tags = "doctor1")
                elif gridlevel1[row][column] == 5:
                    canvas.create_image(97 + column*35, row*35 + 97, image = boxlevel ,tags = "doctor1")
                if gridlevel1[row][column] == 2:
                    canvas.create_image(97 + column*35, row*35 + 97, image = coconut ,tags = "doctor1")
                if gridlevel1[row][column] == 3:
                    canvas.create_image(97 + column*35, row*35 + 97, image = apple ,tags = "doctor1")
                if gridlevel1[row][column] == 4:
                    canvas.create_image(97 + column*35, row*35 + 97, image = water ,tags = "doctor1")
                if gridlevel1[row][column] == 7:
                    canvas.create_image(97 + column*35, row*35 + 97, image = virus ,tags = "doctor1")


#__________________________________________fuunction power_______________________________

power=0
def powerCounter():
    global power
    canvas.itemconfig(powerLabel, text = "Power: " + str(power), anchor= 'se')
    canvas.after(10, powerCounter)
powerLabel = canvas.create_text(150, 70, text = power, font=('Peach Days', 24, 'bold'), fill='black')

#__________________________________________fuunction defind number 1_______________________________

def getIndexdoctorlevel1():
    global power,r,col,row,column
    for r in range(len(gridlevel1)):
        for col in range(len(gridlevel1[r])):
            if gridlevel1[r][col] == 1:
                row = r
                column = col
    return[ row, column]

#__________________________________________fuunction _______________________________

def move(directionlevel):
    global power,row,column,notWin
    indexlevel1 = getIndexdoctorlevel1()
    rowLine = indexlevel1[0]
    columnLine = indexlevel1[1]
    notWin=True
    if directionlevel == "right":
        if columnLine != len(gridlevel1[rowLine]) - 1 and gridlevel1[rowLine][columnLine + 1] != 5:
            gridlevel1[rowLine][columnLine] = 0
            if  gridlevel1[rowLine][columnLine + 1] == 2:
                power += 15
            if  gridlevel1[rowLine][columnLine + 1] == 3:
                power += 15
            if  gridlevel1[rowLine][columnLine + 1] == 4:
                power += 5
            if  gridlevel1[rowLine][columnLine + 1] == 7:
                power -= 10
            gridlevel1[rowLine][columnLine + 1] = 1
            winsound.PlaySound("sound\\Move.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    elif directionlevel == "left":
        if columnLine != 0 and gridlevel1[rowLine][columnLine - 1] != 5:
            gridlevel1[rowLine][columnLine] = 0
            if  gridlevel1[rowLine][columnLine - 1] == 2:
                power += 15
            if  gridlevel1[rowLine][columnLine - 1] == 3:
                power += 15
            if  gridlevel1[rowLine][columnLine - 1] == 4:
                power += 5
            if  gridlevel1[rowLine][columnLine - 1] == 7:
                power -= 10
            gridlevel1[rowLine][columnLine - 1] = 1
            winsound.PlaySound("sound\\Move.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    elif directionlevel == "up":
        if rowLine != 0 and gridlevel1[rowLine - 1][columnLine] != 5:
            gridlevel1[rowLine][columnLine] = 0
            if  gridlevel1[rowLine - 1][columnLine ] == 2:
                power += 5
            if  gridlevel1[rowLine - 1][columnLine ] == 3:
                power += 15
            if  gridlevel1[rowLine - 1][columnLine ] == 4:
                power += 5
            if  gridlevel1[rowLine - 1][columnLine ] == 7:
                power -= 10
                winsound.PlaySound("sound\\Eating.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
            gridlevel1[rowLine - 1][columnLine] = 1
            winsound.PlaySound("sound\\Move.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    elif directionlevel == "down":
        if rowLine != len(gridlevel1) - 1 and gridlevel1[rowLine + 1][columnLine] != 5:
            gridlevel1[rowLine][columnLine] = 0
            if  gridlevel1[rowLine+ 1][columnLine ] == 2:
                power += 15
            if  gridlevel1[rowLine+ 1][columnLine ] == 3:
                power += 15
            if  gridlevel1[rowLine+ 1][columnLine ] == 4:
                power += 5
            if  gridlevel1[rowLine+ 1][columnLine ] == 7:
                power -= power
            gridlevel1[rowLine + 1][columnLine] = 1
            winsound.PlaySound("sound\\Move.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    if power>=30:
        notWin = False
        youWin()
    elif power <0 or minute==1:
        notWin = False
        youLose()
    drawing1()  



#____________________________Move____________________________________________
def moveRight(event):
    move("right")

def moveLeft(event):
    move("left")

def moveUp(event):
    move("up")


def moveDown(event):
    move("down")
#__________________________________________fuunction Win_______________________________
def youWin():
    global notWin
    notWin = False
    canvas.delete("all")
    canvas.create_image(0,0,anchor="nw",image = bgwin)
    winsound.PlaySound("sound\\Win.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_text(660, 325, text = "You Win!🎊🎉✨", font=('Peach Days', 40, 'bold'), fill='green')
    canvas.create_text(650, 400, text = "Your Score: " + str(power) + " Point", font=('consolas', 15, 'bold'), fill='black')
    canvas.create_text(650, 450, text = "Time: " + str(minute) + " : " + str(time) + "s", font=('consolas', 15, 'bold'), fill='black')
    canvas.create_text(150,680,text='Back',anchor='se',font=('consolas 15Peach Days', 30,'underline'), fill='black', tags="back")
    canvas.create_text(1300,680,text="Exit",anchor='se', font=('consolas 15', 30,'underline'), fill='black',tags='exit')
    
#__________________________________________fuunction lose_______________________________

def youLose():
    global notWin
    notWin = False
    canvas.delete("all")
    canvas.create_image(0,0,anchor="nw",image = bglose)
    winsound.PlaySound("sound\\Lost.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_text(660, 325, text = "You Lose!😞😭🔥", font=('Peach Days', 40, 'bold'), fill='red')
    canvas.create_text(650, 400, text = "Your Score: " + str(power) + " Point", font=('consolas', 15, 'bold'), fill='black')
    canvas.create_text(650, 450, text = "Time: " + str(minute) + " : " + str(time) + "s", font=('consolas', 15, 'bold'), fill='black')
    canvas.create_text(150,680,text='Back',anchor='se',font=('consolas 15', 30,'underline'), fill='black', tags="back")
    canvas.create_text(1300,680,text="Exit",anchor='se', font=('consolas 15', 30,'underline'), fill='black',tags='exit')


#__________________________________________fuunction countime_______________________________


notWin=True   
minute = 0
time = 0
def timeCounter():
    global time, minute
    if time == 60:
        minute += 1
        time = 0
    time += 1
    canvas.itemconfig(timelabel, text = "Time: " + str(minute) + " : " + str(time) + "s")
    canvas.after(1000, timeCounter)
timelabel = canvas.create_text(100, 70, text = time, font=('consolas', 24, 'bold'), fill='white')

def level1(event):
    global powerCounter,timeCounter,timelabel,powerLabel,drawing1
    canvas.delete('all')
    winsound.PlaySound("sound\\Level1.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    powerCounter()
    timeCounter()
    canvas.create_image(0,0,anchor="nw",image = level1bg)
    canvas.create_text(1120,100,text="Intructions",font=('Peach Days', 24), fill='yellow')
    canvas.create_image(1125,380,image=intruction)
    canvas.create_text(150,680,text='Back',anchor='se',font=('Peach Days', 30,'underline'), fill='white', tags="back")
    timelabel = canvas.create_text(200, 50, text = time, font=('Peach Days', 24), fill='white')
    powerLabel = canvas.create_text(800, 70, text = power, font=('Peach Days', 24), fill='white')
    drawing1()
    
#----------------------------------- Key control ------------------------------------------------

def chooseLevel(event):
    canvas.delete('all')
    winsound.PlaySound("sound\\Tik tik.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(0,0,anchor='nw',image=chose)
    canvas.create_text(900,180,text="Choose level" ,anchor='se',font=('Peach Days', 50, 'bold'),fill='white' )
    canvas.create_text(750,360,text="Level1",anchor='se',font=('Peach Days', 40), fill='black', tags="level1")
    canvas.create_text(750,490,text="Level2",anchor='se',font=('Peach Days', 40), fill='black', tags="level2")
    canvas.create_text(750,610,text="Level3",anchor='se',font=('Peach Days', 40), fill='black', tags="level3")
    canvas.create_text(280,655,text='Back',anchor='se',font=('Peach Days', 30, 'underline'), fill='white', tags="back")

def startGame(event):
    canvas.delete('all')
    winsound.PlaySound("sound\\Start.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(0,0,anchor='nw',image=doctor)
    canvas.create_text(980,150,text="Welcome to yummy" ,anchor='se',font=('Peach Days', 50, 'bold'),fill='green' )
    canvas.create_text(750,300,text="Start",anchor='se',font=('Peach Days', 40, 'bold'), fill='black', tags="start")
    canvas.create_text(740,425,text="Help",anchor='se', font=('Peach Days', 40, 'bold'), fill='black',tags='rule')
    canvas.create_text(740,535,text="Exit",anchor='se', font=('Peach Days', 40, 'bold'), fill='black',tags='exit')
def rule(event):
    canvas.delete('all')
    canvas.create_image(0,0,anchor='nw',image=bgupdate)
    canvas.create_rectangle(400, 150,950,400, outline="pink", fill="white")
    canvas.create_text(650,200, text = "You need to you button", fill="black", font="consolas 15 bold")
    canvas.create_text(550,230, text = "Right", fill="black", font="consolas 15")
    canvas.create_text(545,260, text = "Left", fill="black", font="consolas 15")
    canvas.create_text(535,290, text = "Up", fill="black", font="consolas 15")
    canvas.create_text(545,320, text = "Down", fill="black", font="consolas 15")
    canvas.create_text(650,350, text = "...", fill="black", font="consolas 15")
    canvas.create_image(750,300,image=rlud)
    canvas.create_text(920,170, text = "X", fill="red", font=("Peach Days ", 20 ,'bold'), tags='Back' )
canvas.tag_bind('Back',"<Button-1>",startGame) 
def exitedGame(event):
    root.quit()
canvas.tag_bind('exit',"<Button-1>",exitedGame)


def update(event):
    canvas.delete('all')
    canvas.create_image(0,0,anchor='nw',image=bgupdate)
    canvas.create_rectangle(400, 150,950,300, outline="pink", fill="white")
    canvas.create_text(650,200, text = "Try again!", fill="black", font="consolas 15 bold")
    canvas.create_text(650,230, text = "This level we Updating.", fill="black", font="consolas 15")
    canvas.create_text(650,260, text = "...", fill="black", font="consolas 15")
    canvas.create_text(920,170, text = "X", fill="red", font=("Peach Days ", 20 ,'bold'), tags='delete' )
canvas.tag_bind('level2',"<Button-1>",update)
canvas.tag_bind('level3',"<Button-1>",update)
canvas.tag_bind('delete',"<Button-1>",chooseLevel)
startGame(event=startGame)
canvas.pack(expand=True, fill='both')

canvas.tag_bind('rule',"<Button-1>",rule)
canvas.tag_bind('back',"<Button-1>",startGame)
canvas.tag_bind('start',"<Button-1>",chooseLevel)
canvas.tag_bind('level1',"<Button-1>",level1)
root.bind("<Right>",moveRight)
root.bind("<Left>",moveLeft)
root.bind("<Up>",moveUp)
root.bind("<Down>",moveDown)

root.mainloop()