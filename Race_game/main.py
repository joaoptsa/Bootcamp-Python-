import random as rand
from turtle import Turtle,Screen

screen= Screen()
screen.setup(height=500,width=500)
screen.title("Race")
colors=["red","orange","yellow","green","blue","purple"]
positions_y=[-70,-40,-10,20,50,80]
all_obj=[]
vitory=0

def ask():
    while(True):
        input_choose = screen.textinput(title="Race", prompt="Choose the color?\n(red,orange,yellow,green,blue,purple)")
        if  input_choose  in colors:
            break
    
    return input_choose

def star_game():
    for index in range(0,6):
        tim=Turtle(shape="triangle")
        tim.penup()
        tim.color(colors[index])
        tim.goto(x=-250,y=positions_y[index])
        all_obj.append(tim)

def restar_game(all_obj):
    i=0
    for obj in all_obj:
        obj.goto(x=-250,y=positions_y[i])
        i=i+1


game=True
your=ask()

while game:
    star_game()
    race_is_fire =True
    while race_is_fire:
        for obj in all_obj:
            if obj.xcor()>220:
                winning=obj.pencolor()
                print(winning)
                print("a tua cor " + your)
                if winning ==your.lower():
                    vitory=vitory+1
                    your = screen.textinput(title=f"Number vitorys: {vitory}",prompt="Your Winner \nChoose the color :").title()
                    restar_game(all_obj)

                else:
                    your = screen.textinput(title=f"Number vitorys: {vitory}",prompt="Your Losser \nChoose the color ").title()
                    restar_game(all_obj)


            rand_distance=rand.randint(0,10)
            obj.forward(rand_distance)



screen.exitonclick()
