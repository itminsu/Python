__author__ = 'w0293156'
#Declare the dices
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

#declare a combination variable
combination = " " #Str Variable

#determine Full house
if amountOfOne == 3 or amountOfTwo == 3 or amountOfThree == 3 or amountOfFour == 3 or amountOfFive == 3 or amountOfSix == 3 :
    if amountOfOne ==2 or amountOfTwo == 2 or amountOfThree == 2 or amountOfFour == 2 or amountOfFive == 2 or amountOfSix == 2:
        combination = "Full house"
    #determine Three of a Kind
    else:
        combination = "Three of a Kind"
#determine Large Straight
elif amountOfOne == 1 and amountOfTwo == 1 and amountOfThree == 1 and amountOfFour == 1 and amountOfFive == 1:
        combination = "Large Straight"
elif amountOfTwo == 1 and amountOfThree == 1 and amountOfFour == 1 and amountOfFive == 1 and amountOfSix == 1:
        combination = "Large Straight"

#determin Small Straight
elif amountOfOne == 0 and amountOfTwo == 1 and amountOfThree == 1 and amountOfFour == 1 and amountOfFive == 1 and amountOfSix == 1:
    if amountOfOne == 0 and amountOfTwo == 1 and amountOfThree == 1 and amountOfFour == 1 and amountOfFive == 1 and amountOfSix == 1:
        if amountOfOne == 1 and amountOfTwo == 0 and amountOfThree == 1 and amountOfFour == 1 and amountOfFive == 1 and amountOfSix == 1:
            if amountOfOne == 1 and amountOfTwo == 1 and amountOfThree == 0 and amountOfFour == 1 and amountOfFive == 1 and amountOfSix == 1:
                if amountOfOne == 1 and amountOfTwo == 1 and amountOfThree == 1 and amountOfFour == 0 and amountOfFive == 1 and amountOfSix == 1:
                    if amountOfOne == 1 and amountOfTwo == 1 and amountOfThree == 1 and amountOfFour == 1 and amountOfFive == 0 and amountOfSix == 1:
                        if amountOfOne == 1 and amountOfTwo == 1 and amountOfThree == 1 and amountOfFour == 1 and amountOfFive == 1 and amountOfSix == 0:
                             combination = "Small Straight"
#determine Five of a Kind
elif amountOfOne == 5 or amountOfTwo == 5 or amountOfThree == 5 or amountOfFour == 5 or amountOfFive == 5 or amountOfSix == 5 :
    combination = "Five of a Kind"
#determine Four of a Kind
elif amountOfOne == 4 or amountOfTwo == 4 or amountOfThree == 4 or amountOfFour == 4 or amountOfFive == 4 or amountOfSix == 4 :
    combination = "Four of a Kind"

#determine One Pair
elif amountOfOne == 2 or amountOfTwo == 2 or amountOfThree == 2 or amountOfFour == 2 or amountOfFive == 2 or amountOfSix == 2 :
    combination = "One Pair"

#determine Two Pair (FAIL)
###elif amountOfOne == 1 or amountOfTwo == 1 or amountOfThree == 1 or amountOfFour == 1 or amountOfFive == 1 or amountOfSix == 1:
    ###if amountOfOne == 2 or 0 and amountOfTwo == 2 or 0 and amountOfThree == 1 and amountOfFour == 2 or 0 and amountOfFive == 2 or 0 and amountOfSix == 2 or 0 :
        ###if amountOfOne == 2 or 0 and amountOfTwo == 2 or 0 and amountOfThree == 2 or 0 and amountOfFour == 1 and amountOfFive == 2 or 0 and amountOfSix == 2 or 0 :
            ###if amountOfOne == 2 or 0 and amountOfTwo == 2 or 0 and amountOfThree == 2 or 0 and amountOfFour == 2 or 0 and amountOfFive == 1 and amountOfSix == 2 or 0 :
                ###if amountOfOne == 2 or 0 and amountOfTwo == 2 or 0 and amountOfThree == 2 or 0 and amountOfFour == 2 or 0 and amountOfFive == 2 or 0 and amountOfSix == 1 :
                        ###combination = "Two Pair"

#determine No Combination
else:
    combination = "No Combination"
#Print the result
print("Highest Combination: "+ combination)