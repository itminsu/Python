__author__ = 'w0293156'
#Declare Variable
useageOfWater= 0.00 #float variable
total = 0.00 #float variable
charge10 = 15 #int variable
charge12 = 0.0175 #float variable
charge23 = 0.02 #float variable
charge30 = 70 #int variable

#Enter the useage of water from user
useageOfWater = float(input("Enter usage of water (cubic feet): "))

#Condition of charges
if useageOfWater  <= 1000 :
    total = charge10

elif useageOfWater <= 2000:
    total = charge12 * useageOfWater

elif useageOfWater <= 3000:
    total = charge23 * useageOfWater

elif useageOfWater > 3000:
    total = charge30

#Display the result
print("Total charge is ${0:.2f}".format(total))
