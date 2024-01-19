import tkinter as tk
from tkinter import messagebox

profit=0
user_balance=0
change=0
drink=""

MENU = {

    "espresso": {
    "ingredients":{
    "water":58,
    "milk":0,
    "coffee":18,
    
    },
    "cost":1.5,
    },

    "latte": {
    "ingredients":{
    "water":100,
    "milk":150,
    "coffee":24,
     },
    "cost":3.5,
    },

    "cappuccino":{
    "ingredients":{
    "water":250,
    "milk":100,
    "coffee":24,
     },
    "cost":3.0,
    },

    }

resources= {
    "water":500,
    "milk":580,
    "coffee":500,
}


def makeCoffe(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    


def verfResource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            return False
    return True


def is_transactionPossible(money_received, drink_cost):
    global change
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        return True
    else:
        return False      




class CoffeeMachineApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coffee Machine")

        self.confirm_payment_button = tk.Button(self.root, text="Confirm Payment", command=self.confirm_payment)
        self.confirm_payment_button.pack(side=tk.LEFT)
        self.confirm_payment_button.config(state=tk.DISABLED) 

        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack()

        self.off_button = tk.Button(self.root, text="Off", command=self.turn_off)
        self.off_button.pack(side=tk.LEFT)

        self.report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.report_button.pack(side=tk.LEFT)

        # Adicionando botões para cada bebida
        self.espresso_button = tk.Button(self.root, text="Espresso", command=lambda: self.select_drink("espresso"))
        self.espresso_button.pack(side=tk.LEFT)

        self.latte_button = tk.Button(self.root, text="Latte", command=lambda: self.select_drink("latte"))
        self.latte_button.pack(side=tk.LEFT)
        

        self.cappuccino_button = tk.Button(self.root, text="Cappuccino", command=lambda: self.select_drink("cappuccino"))
        self.cappuccino_button.pack(side=tk.LEFT)

        self.one_button = tk.Button(self.root, text="1 euro", command=lambda: self.pay_money(1))
        self.one_button.pack(side=tk.LEFT)
        self.one_button.config(state=tk.DISABLED)   

        self.five_button = tk.Button(self.root, text="0.50 euro", command=lambda: self.pay_money(0.5))
        self.five_button.pack(side=tk.LEFT)
        self.five_button.config(state=tk.DISABLED) 


    def turn_off(self):
        self.text_area.insert(tk.END, "Turning off the machine...\n")
        self.root.destroy()

    def generate_report(self):
        self.text_area.insert(tk.END, f"Generating report...\n water:{resources['water']}ml\n milk:{resources['milk']}ml\n coffee:{resources['coffee']}ml\n money:{profit}")

    def pay_money(self,money):
        global user_balance
        self.text_area.insert(tk.END, f"{money} euros \n") 
        user_balance= user_balance + money 
    

    def confirm_payment(self):
        global user_balance
        global change
        global drink

        if is_transactionPossible(user_balance, drink["cost"]):
            self.five_button.config(state=tk.DISABLED)
            self.one_button.config(state=tk.DISABLED)
            self.confirm_payment_button.config(state=tk.DISABLED)

            makeCoffe(drink["ingredients"])
            
            if change > 0:
                self.text_area.insert(tk.END, f"Here is your {change} change\n")
            self.text_area.insert(tk.END, f"Here is your drink\n")
        else:
            self.text_area.insert(tk.END, f"Error: not enough money\n")
        
        self.reset()
    
    def select_drink(self, drink1):
        
        global MENU
        global drink
        drink = MENU[drink1]
        
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"Selected drink: {drink1}\n")
        self.off_button.config(state=tk.DISABLED)
        self.report_button.config(state=tk.DISABLED)
        self.espresso_button.config(state=tk.DISABLED)
        self.latte_button.config(state=tk.DISABLED)
        self.cappuccino_button.config(state=tk.DISABLED)
      
        if verfResource(drink["ingredients"]):
            self.text_area.insert(tk.END, f"Price: {drink['cost']}\n")
            self.five_button.config(state=tk.ACTIVE)
            self.one_button.config(state=tk.ACTIVE)
            self.confirm_payment_button.config(state=tk.ACTIVE)

        else:
            self.text_area.insert(tk.END, f"Error: not enough ingredients\n")

    def reset(self):
        global user_balance
        user_balance=0

        self.off_button.config(state=tk.NORMAL)
        self.report_button.config(state=tk.NORMAL)
        self.espresso_button.config(state=tk.NORMAL)
        self.latte_button.config(state=tk.NORMAL)
        self.cappuccino_button.config(state=tk.NORMAL)
        

     
       


    def run(self):
        self.root.mainloop()

app = CoffeeMachineApp()
app.run()



   
    
