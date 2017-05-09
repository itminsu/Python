__author__ = 'w0293156'
#Declare Variable
maritalStatus = " "         #str variable
amountOfIncome = 0.00       # float variable
maritalStatus = " "         #str variable
total = 0.00 #float variable

#Enter the information of marital status
maritalStatus = input("Enter your marital status: ").lower()

#Enter the amount of income
amountOfIncome = float(input("Enter your taxable income: "))

#Condition of tax for single
if maritalStatus == "single":

    if amountOfIncome < 8000:
        amountOfIncome = amountOfIncome * 0.1

    elif amountOfIncome >= 8000  and amountOfIncome < 32000:
        amountOfIncome = 800 + ((amountOfIncome - 8000) * 0.15)

    elif amountOfIncome >= 32000:
        amountOfIncome = 4400 + ((amountOfIncome - 32000) * 0.25)

#Condition of tax for married
if maritalStatus == "married":

    if amountOfIncome < 16000:
        amountOfIncome = amountOfIncome * 0.1

    elif amountOfIncome >= 16000 and amountOfIncome < 64000:
        amountOfIncome = 1600 + ((amountOfIncome - 16000) * 0.15)

    elif amountOfIncome >= 64000:
        amountOfIncome = 8800 + ((amountOfIncome - 64000) * 0.25)

#Print the result
print("Your total tax is ${0:.2f}".format(amountOfIncome))