from turtle import *
import random
import time


WIDTH , HEIGHT = 400 ,400 
COLORS = ["red","green","yellow","blue","brown","cyan","black","orange","purple","violet"]

# Taking inputs from user to create turtles
def No_Of_Turtles():
    racers = 0
    while True:
        racers= input("Enter the NO.Of Racers ( 2 - 10 ): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Entered Number is Not Numeric .....Please Try Again !!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Please Enter the number in the range ( 2 - 10)")

# Creating turtles
def Create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)
    x = spacingx
    for  i,color in enumerate (colors):
        racer = Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH //2 + ( i + 1) * spacingx , -HEIGHT // 2 + 20)
        #racer.setpos((-WIDTH//2 )+ (spacingx+x) , -HEIGHT//2 )
        x+=spacingx
        #racer.pendown()
        racer.speed(1)
        turtles.append(racer)

    return turtles

#Racing the turtles
def race(colors):
    turtles  = Create_turtles(colors)

    while True :
        for racer in turtles :
            distance = random.randrange(5 ,20)
            racer.forward(distance)

            x , y = racer.pos()
            if y >= HEIGHT//2  :
                return colors[turtles.index(racer)]

# Creating screen to race turtle
def Create_screen():
    screen = Screen()
    screen.setup(WIDTH , HEIGHT)
    screen.title("Turtle racing")
    screen.bgcolor("silver")
    
racers = No_Of_Turtles ()
Create_screen()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The Winner is The Turtle With Color : {winner}")
time.sleep(5)







        

