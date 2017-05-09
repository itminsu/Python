__author__ = 'w0293156'
#1.Declare Variable
miles = 0        #int variable
yards = 0        #int variable
feet = 0         #int variable
inches = 0       #int variable
totalInches = 0  #int variable
totalMetres = 0  #int variable
kilometres= 0.00 #float variable
#2a.Enter the number of miles
miles = input("Enter the number of miles: ")
#2b.Enter the number of yards
yards = input("Enter the number of yards: ")
#2c.Enter the number of feet
feet = input("Enter the number of feet: ")
#2d.Enter the number of inches
inches = input("Enter the number of inches: ")
#3.Calculate
totalInches = 63360*int(miles)+36*int(yards)+12*int(feet)+int(inches)
totalMetres = totalInches/39.37
kilometres = float(totalMetres)/1000

metr = 0.00 #float variable
metr = (kilometres - (kilometres//1)) * 1000
cent = 0.00 #float variable
cent = (metr - (metr //1)) * 100
print("\nThe metric length is "+str(round(kilometres))+" kilometres, "
      +str(round(metr//1))+" metres, and "+str(round(cent,1))+" centimetres")
