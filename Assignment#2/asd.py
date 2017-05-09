__author__ = 'Minsu Lee'
#Declare random
import random

dice1=random.randint(1,6)
dice2=random.randint(1,6)
dice3=random.randint(1,6)
dice4=random.randint(1,6)
dice5=random.randint(1,6)

#Declare Variable to determine the number
amountOfOne = 0
amountOfTwo = 0
amountOfThree = 0
amountOfFour = 0
amountOfFive = 0
amountOfSix = 0

#print the random numbers
print("Dice 1: "+str(dice1))
print("Dice 2: "+str(dice2))
print("Dice 3: "+str(dice3))
print("Dice 4: "+str(dice4))
print("Dice 5: "+str(dice5))

#The number of dice1
if dice1 == 1:
 amountOfOne = amountOfOne + 1
elif dice1 == 2:
 amountOfTwo = amountOfTwo + 1
elif dice1 == 3:
 amountOfThree = amountOfThree + 1
elif dice1 == 4:
 amountOfFour = amountOfFour + 1
elif dice1 == 5:
 amountOfFive = amountOfFive + 1
else :
 amountOfSix = amountOfSix + 1

#The number of dice2
if dice2 == 1:
 amountOfOne = amountOfOne + 1
elif dice2 == 2:
 amountOfTwo = amountOfTwo + 1
elif dice2 == 3:
 amountOfThree = amountOfThree + 1
elif dice2 == 4:
 amountOfFour = amountOfFour + 1
elif dice2 == 5:
 amountOfFive = amountOfFive + 1
else :
 amountOfSix = amountOfSix + 1

#The number of dice3
if dice3 == 1:
 amountOfOne = amountOfOne + 1
elif dice3 == 2:
 amountOfTwo = amountOfTwo + 1
elif dice3 == 3:
 amountOfThree = amountOfThree + 1
elif dice3 == 4:
 amountOfFour = amountOfFour + 1
elif dice3 == 5:
 amountOfFive = amountOfFive + 1
else :
 amountOfSix = amountOfSix + 1

#The number of dice4
if dice4 == 1:
 amountOfOne = amountOfOne + 1
elif dice4 == 2:
 amountOfTwo = amountOfTwo + 1
elif dice4 == 3:
 amountOfThree = amountOfThree + 1
elif dice4 == 4:
 amountOfFour = amountOfFour + 1
elif dice4 == 5:
 amountOfFive = amountOfFive + 1
else :
 amountOfSix = amountOfSix + 1

#The number of dice5
if dice5 == 1:
 amountOfOne = amountOfOne + 1
elif dice5 == 2:
 amountOfTwo = amountOfTwo + 1
elif dice5 == 3:
 amountOfThree = amountOfThree + 1
elif dice5 == 4:
 amountOfFour = amountOfFour + 1
elif dice5 == 5:
 amountOfFive = amountOfFive + 1
else :
 amountOfSix = amountOfSix + 1

combination = " " #Str Variable

if amountOfOne == 3 or amountOfTwo == 3 or amountOfThree == 3 or amountOfFour == 3 or amountOfFive == 3 or amountOfSix == 3 :
    if amountOfOne ==2 or amountOfTwo == 2 or amountOfThree == 2 or amountOfFour == 2 or amountOfFive == 2 or amountOfSix == 2:
        combination = "Full house"

elif amountOfOne == 1 and amountOfTwo == 1 and amountOfThree == 1 and amountOfFour == 1 and amountOfFive == 1 and amountOfSix == 1:
    combination = "Large Straight"



elif amountOfOne == 5 or amountOfTwo == 5 or amountOfThree == 5 or amountOfFour == 5 or amountOfFive == 5 or amountOfSix == 5 :
    combination = "Five of a Kind"

elif amountOfOne == 4 or amountOfTwo == 4 or amountOfThree == 4 or amountOfFour == 4 or amountOfFive == 4 or amountOfSix == 4 :
    combination = "Four of Kind"

elif amountOfOne == 3 or amountOfTwo == 3 or amountOfThree == 3 or amountOfFour == 3 or amountOfFive == 3 or amountOfSix == 3 :
    combination = "Three of Kind"


elif amountOfOne or amountOfTwo or amountOfThree or amountOfFour or amountOfFive or amountOfSix == 2 :
    combination = "One Pair"

else:
    combination = "No Combination"

print("Highest Combination: "+ combination)