import turtle as trtl
import random as rand
writer = trtl.Turtle()
grid = trtl.Turtle()
wn = trtl.Screen()
homebase = trtl.Turtle()


wn.setup(width=515.0, height=270.0)
homebase.shape("circle")
armylist =[]
army = trtl.Turtle()
armylist.append(army)
cordx = [-5,-4,-3,-2,-1,1,2,3,4,5]
cordy = [-5,-4,-3,-2,-1,1,2,3,4,5]
antispamx = []
antispamy = []
homebase.fillcolor("blue")
army.fillcolor("green")

tax = 10
armycost = 100
score = 0
ownage = 0
phase = 1
triv = 0
check = 0
wn.tracer(False)

#---------The Functions---------
def gameover():
  writer.clear()
  scwriter.clear()
  arwriter.clear()
  tawriter.clear()
  grid.clear()
  for a in armylist:
    a.clear()
    a.hideturtle()
  homebase.hideturtle()
  writer.goto(-130,0)
  writer.color("red")
  writer.write("GAME OVER", font=("Arial", 30, "bold"))
  writer.goto(-120,-40)
  writer.color("black")
  writer.write("Your score was...", font=("Arial", 20, "bold"))
  writer.goto(0,-90)
  writer.write(score, font=("Arial", 30, "bold"))

def t1():
  global armycost
  global tax
  print("You will be asked the following questions on the Great War to recieve deflations and inflations to your army cost and land tax.")
  answer = input("Y OR N The archduke who was assassinated in 1914 to spark the first world war resided in Bosnia")
  if answer == "N":
    print("Correct! He resided in the dual monarchy of Austria-Hungary, not Bosnia. ")
    armycost = armycost - 10
    tax = tax - 2 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  else:
    print("Wrong! He resided in the dual monarchy of Austria-Hungary, not Bosnia. ")
    armycost = armycost + 20
    tax = tax + 5 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  print("---------Next Question!---------")
  answer = int(input("In millions, how many casualties did the German Empire have by the end of the war?"))
  if answer == 2:
    print("Very Good! About 2 Million German soldiers did not come home in the war.")
    armycost = armycost - 10
    tax = tax - 2 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  else:
    print("Too bad! About 2 million German soldiers did not come home in the war, not",answer,"million.")
    armycost = armycost + 20
    tax = tax + 5 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  print("---------Final Question!---------")
  answer = input("Y OR N After the end of WWI, communism came into Russia and renamed it The United States of Communism")
  if answer == "N":
    print("Good. Although Russia did become communist, they were called the Soviet Union or USSR, not The USC")
    armycost = armycost - 10
    tax = tax - 2 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  else:
    print("No, Although Russia did become communist, they were called the Soviet Union or USSR, not The USC")
    armycost = armycost + 20
    tax = tax + 5 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))

def t2():
  global armycost
  global tax
  print("You will be asked the following questions on the Second World War to recieve deflations and inflations to your army cost and land tax.")
  answer = input("The three major factions of WW2 were the Allied, Third International, and")
  if answer == "Axis":
    print("Very Nice! The Axis were the 3rd faction of WW2.")
    armycost = armycost - 10
    tax = tax - 2 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  else:
    print("Incorrect, the Axis were the 3rd faction of WW2.")
    armycost = armycost + 20
    tax = tax + 5 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  print("---------Next Question!---------")
  answer = int(input("Which year did the Second World War end?"))
  if answer == 1945:
    print("Correct, the Allies beat Germany in 1945.")
    armycost = armycost - 10
    tax = tax - 2 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  else:
    print("Wrong, the Allies beat Germany in 1945.")
    armycost = armycost + 20
    tax = tax + 5 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  print("---------Final Question!---------")
  answer = input("Y OR N The naval invasion of Iberia in 1943 happened")
  if answer == "N":
    print("Good, this invasion never happened.")
    armycost = armycost - 10
    tax = tax - 2 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  else:
    print("False, you must be confusing this with the Normandy invasion of 1944, right?")
    armycost = armycost + 20
    tax = tax + 5 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))

def t3():
  global armycost
  global tax
  print("You will be asked the following questions on the Cold War era to recieve deflations and inflations to your army cost and land tax.")
  answer = input("Y OR N After the end of World War 2, the world was split into 2 East and West This marked the beginning of the era called the Cold War")
  if answer == "Y":
    print("Very good. The Cold War era started after WW2")
    armycost = armycost - 10
    tax = tax - 2 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  else:
    print("Incorrect. The Cold War era did, in fact, start after WW2")
    armycost = armycost + 20
    tax = tax + 5 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  print("---------Next Question!---------")
  answer = int(input("The Vietnam War started in what year?"))
  if answer == 1959:
    print("Correct! Very Good! The Vietnam War ran from 1959 to 1975.")
    armycost = armycost - 10
    tax = tax - 2 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  else:
    print("Incorrect. The Vietnam War ran from 1959 to 1975.")
    armycost = armycost + 20
    tax = tax + 5 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  print("---------Final Question!---------")
  answer = input("Y OR N There are no more communist states in the world after the aftermath of the Cold War.")
  if answer == "N":
    print("Good. There are 5 remaining communist countries to date: China, Cuba, Laos, Vietnam, and North Korea.")
    armycost = armycost - 10
    tax = tax - 2 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))
  else:
    print("Too bad! There are actually 5 remaining communist countries to date: China, Cuba, Laos, Vietnam, and North Korea.")
    armycost = armycost + 20
    tax = tax + 5 
    arwriter.clear()
    tawriter.clear()
    arwriter.write(armycost, font=("Arial", 12, "bold"))
    tawriter.write(tax, font=("Arial", 12, "bold"))


#set up grid
x = -100
y = -100
xask = 10
yask = 10
grid.setheading(90)
while xask+1 > 0:
  grid.penup()
  grid.goto(x,-100)
  grid.pendown()
  grid.forward(200)
  x = x + 20
  xask = xask - 1
grid.setheading(0)
while yask+1 > 0:
  grid.penup()
  grid.goto(-100,y)
  grid.pendown()
  grid.forward(200)
  y = y + 20
  yask = yask - 1

grid.hideturtle()
writer.penup()
writer.goto(-95,100)
writer.setheading(0)
for x in cordx:
  writer.write((x), font=("Arial", 10, "bold"))
  writer.forward(20)
writer.goto(-115,85)
writer.setheading(270)
for y in cordy:
  writer.write((y), font=("Arial", 10, "bold"))
  writer.forward(21)

#-----Scores setup----
writer.goto(-225, 85)
writer.write("Score:", font=("Arial", 12, "bold"))
writer.hideturtle()
scwriter = trtl.Turtle()
arwriter = trtl.Turtle()
tawriter = trtl.Turtle()
scwriter.hideturtle()
tawriter.hideturtle()
arwriter.hideturtle()
scwriter.penup()
tawriter.penup()
arwriter.penup()
scwriter.goto(-225, 65)
scwriter.write(score, font=("Arial", 12, "bold"))
writer.goto(-225, 15)
writer.write("Army Cost:", font=("Arial", 12, "bold"))
arwriter.goto(-225, -5)
arwriter.write(armycost, font=("Arial", 12, "bold"))
writer.goto(-225, -45)
writer.write("Tax:", font=("Arial", 12, "bold"))
tawriter.goto(-225, -65)
tawriter.write(tax, font=("Arial", 12, "bold"))
writer.goto(100,100)
wn.tracer(True)

homebase.penup()
homebase.goto(90,-90)
army.penup()
army.goto(90,-90)
print("-----DIRECTIONS: PLEASE PAY ATTENTION TO THIS!!!!!-----")
print("Conquest phase: your highlighted army, in yellow, is the one you are moving. A blue army on a square means you have already taken the square. Do not move here, you will recieve no points. The blue circle means a homebase. Do not set a move direction to 0. Pay attention to your score, army cost, and tax on the graphics window")
print("Buy phase: You will lose the game if your score is lower than 0 at the start of the buy phase.")
print("Trivia phase: The questions are about conflicts the world has faced. Please capitalize your Y or N. Don't put a 'the' in front of an answer. Questions add more Army Cost and Tax when you get them wrong than subtract when you get them right, so know your trivia! Repl.it has weird print bugs in the trivia phase, watch out. After all three trivia phases are over, the game will be over and you will recieve your final score. ")
while phase > 0:
  print("-+-+-+-+-Conquest phase start!!!-+-+-+-+-")
  for a in armylist:
    #---------CONQUEST PHASE-----------------
    a.fillcolor("yellow")
    conx = int(input("Where do you want your army to go (x value)"))
    if conx < -5:
      print("You didn't enter a value from -5 to 5, Too bad!")
      conx = 5
    if conx > 5:
      print("You didn't enter a value from -5 to 5, Too bad!")
      conx = 5
    cony = int(input("Where do you want your army to go (y value)"))
    if cony < -5:
      print("You didn't enter a value from -5 to 5, Too bad!")
      cony = 5
    if cony > 5:
      print("You didn't enter a value from -5 to 5, Too bad!")
      cony = 5
    cony = cony * -17
    conx = conx * 17
    a.goto(conx,cony)
    #---------ANTI EXPLOIT MEASURES-----------------
    if len(antispamx) == 0:
      score = score + rand.randint(100,200)
      ownage = ownage + 1
      check = 1
    for t in antispamx:
      for n in antispamy:
        if conx == t:
          if cony == n:
            score = score + 0
            check = 1
            print("You moved to the same space as an army before, no points!")
    if check == 0:
      score = score + rand.randint(100,200)
      ownage = ownage + 1
    check = 0
    scwriter.clear()
    scwriter.write(score, font=("Arial", 12, "bold"))
    antispamx.append(conx)
    antispamy.append(cony)
    a.fillcolor("blue")
    a.stamp()
    a.fillcolor("green")
  #---------BUY PHASE-----------------
  if score < 0:
    gameover()
  print("-+-+-+-+-Buy phase start!!!-+-+-+-+-")
  abuy = int(input("How many armys would you like to buy?"))
  while abuy > 0:
    army = trtl.Turtle()
    army.fillcolor("green")
    armylist.append(army)
    army.penup()
    army.goto(90,-90)
    abuy = abuy - 1
    score = score - armycost
    scwriter.clear()
    scwriter.write(score, font=("Arial", 12, "bold"))
  print("You must now use some of your score to feed your army(s)")
  score = score - (len(armylist) * 20)
  scwriter.clear()
  scwriter.write(score, font=("Arial", 12, "bold"))
  print("Also, you are responsible to pay taxes on the land you now own!")
  score = score - (ownage * tax)
  scwriter.clear()
  scwriter.write(score, font=("Arial", 12, "bold"))
  print("-+-+-+-+-Trivia phase start!!!-+-+-+-+-")
  if triv == 0:
    t1()
  if triv == 1:
    t2()
  if triv == 2:
    t3()
  if triv == 3:
    gameover()
  triv = triv + 1
