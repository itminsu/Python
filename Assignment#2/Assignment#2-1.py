__author__ = 'w0293156'
#Declare Variable
number = 0                    #int variable
length = 0.00                 #float variable
width = 0.00                  #float variable
woodType= " "                #str variable
drawer = 0                    #int variable
cost = 200.00                 #float variable
surfaceCharge = 50            #int variable
mahoganyCharge = 150          #int variable
oakCharge = 125               #int variable
drawerCharge = 30             #int variable
surfaceChargeThreshold = 750  # int variable

#Enter the information of the desk from user
number= int(input("Enter order number: "))
length= float(input("Enter length of desk (inches): "))
width = float(input("Enter width of desk (inches: "))
woodType = input("Enter type of wood (mahogany,oak,pine): ")
drawer= int(input("Enter number of drawers: "))

#Declare surface variable
surface = length * width

#Size of surface
if surface > surfaceChargeThreshold:

    cost = cost + surfaceCharge

#Type of wood
if woodType == "mahogany":

    cost = cost + mahoganyCharge
elif woodType == "oak":

    cost = cost + oakCharge

else:

    cost = cost

#Extra charge adding drawer
cost = cost + (drawer * drawerCharge)

#print result
print("Total cost is: ${0:.2f}".format(cost))


