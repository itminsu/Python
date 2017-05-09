__author__ = 'w0293156'
#1.Declare Variable
wage = 0.00       #float variable
taxCost = 0.00 #float variable
total = 0.00   #float variable

#2.Display Instruction.

print("McNair's PC Repair - Work Order Tracking Program")
#3a.Enter the customer's name.
customerName = input("\nEnter the customer's name: ")
#3b.Enter the work hours.
labourHour = input("Enter the number of hours of labour: ")
#3c.Enter the cost of parts and supplies.
costOfParts = input("Enter the cost of any parts and/or supplies: ")

#4. Calculate
wage = float(labourHour)*65
taxCost = float(costOfParts)*1.15
total = wage + taxCost

#5a. Display customer's name.
print("\nWork order summary for customer: "+str(customerName))
#5b. Display Labour hours.
print("Labour cost: ${0:.2f}".format(wage))
#5c. Display parts cost.
print("Parts cost: ${0:.2f}".format(taxCost))
#5d. Display total cost.
print("Total cost: ${0:.2f}".format(total))
