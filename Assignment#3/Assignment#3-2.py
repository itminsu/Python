__author__ = 'Minsu Lee'
#declare variable to count vowel
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
word = " "
#while
while word != "quit":
#Enter a phrase to be counted
    word = input("Type a phrase (or quit to exit program): \n").lower()
    print()
#Determine quit or not
    if word == "quit":
        print("End of Program")
    else:
#Determine vowels
        for letter in word:
            if letter == "a":
                count_a += 1
            elif letter == "e":
                count_e += 1
            elif letter == "i":
                count_i += 1
            elif letter == "o":
                count_o += 1
            elif letter == "u":
                count_u += 1
#Print the result
        print("Letter A count: "+ str(count_a))
        print("Letter E count: "+ str(count_e))
        print("Letter I count: "+ str(count_i))
        print("Letter O count: "+ str(count_o))
        print("Letter U count: "+ str(count_u))
        print()
#Redefine the variables
        count_a = 0
        count_e = 0
        count_i = 0
        count_o = 0
        count_u = 0