import random

wordList=["car","camel","blue","door","orange"]
choseWord=random.choice(wordList)


endgame = False;
display=[]

for x in range(len(choseWord)):
  display +="_"
print(display)  




while endgame==False:
 
 guess=input("Guess a letter: ").lower()


 for position in range (len(choseWord)):
  letter=choseWord[position]
  if letter==guess:
     display[position]=letter
 
 print(display)
 
 if "_" not in display:
     endgame=True
     print("You Win.")
  
