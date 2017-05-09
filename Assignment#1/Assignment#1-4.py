__author__ = 'w0293156'
#1.Declare Variable
tenHundred = 0      #int Variable
fiveHundred = 0     #int Variable
oneHundred = 0      #int Variable
single = 0          #int Variable

#2.Enter the number of sheets
sheets=input("Enter the number of sheets of paper needed: ")

#3.Calculate
tenHundred = int(sheets)//1000
fiveHundred = int(sheets)%1000//500
oneHundred = int(sheets)%1000%500//100
single = int(sheets)%1000%500%100
###Declare Variable to calculate
amountOfTen = 0       #int Variable
amountOfFive = 0      #int Variable
amountOfOne = 0       #int Variable
amountOfSingle = 0    #int Variable
total = 0             #int Variable

if int(single) >= 55:
    single = int(single)*0
    oneHundred = int(oneHundred) + 1
if int(oneHundred) >= 4:
    oneHundred = int(oneHundred)*0
    fiveHundred = int(fiveHundred) + 1
if int(single)+int(oneHundred) >= :

#4.Display the numbers of sheet
print("Number of 1000 package: " + str(tenHundred))
print("Number of 500 package: " + str(fiveHundred))
print("Number of 100 package: " + str(oneHundred))
print("Number of singles: " + str(single))

#5.Calculate efficiently
amountOfTen= int(tenHundred)*30
amountOfFive= int(fiveHundred)*20
amountOfOne= int(oneHundred)*5.5
amountOfSingle= int(single)*0.10



#6.Display the total cost
total = amountOfTen+amountOfFive+amountOfOne+amountOfSingle
print("Total cost: $"+ str(round(total,2)))