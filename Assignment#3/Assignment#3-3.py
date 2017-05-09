__author__ = 'Minsu Lee'
#print top of the half line
for value in range(9):
    print(" "*(9-value) + "0"*(value*2+1))
#print bottom of the half line
for value in range(10):
    print(" "*(value) + "0"*(20-(value*2+1)))