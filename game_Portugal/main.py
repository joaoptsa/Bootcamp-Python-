import turtle
import pandas

image="portugal.gif"
screen = turtle.Screen()
screen.title("Portugal")
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("distritos.csv")
dataa=data.state.to_list()
print(dataa)
respCheck=[]
t=turtle.Turtle()
t.hideturtle()
t.penup()
missing = []
while len(respCheck)<18:
 resp = screen.textinput(title=f"{len(respCheck)}/18 corretas", prompt="Qual o distrito que falta?").title()
 if resp =="Exit":
     for state in dataa:
         if state not in respCheck:
             missing.append(state)
     t.write(f"FALHOU:: {len(missing)}",align="center", font=("Arial", 100, "normal"))
     break
 print(resp)
 if resp in dataa:
    print(resp)
    state_data=data[data.state == resp]
    t.goto(int(state_data.x),int(state_data.y))
    t.write(resp)
    respCheck.append(resp)


turtle.mainloop()
screen.exitonclick()





