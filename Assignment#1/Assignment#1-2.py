__author__ = 'w0293156'
#1.Declare Variable
amountOfLoan = 0 #int variable
rate = 0.00      #float variable
numberOfYears = 0#int variable
monthly = 0.00   #float variable
#2a.Enter the amount of loan.
amountOfLoan = input("Enter the amount of loan: ")
#2b.Enter the interest rate.
rate= input("Enter the interest rate (%): ")
#2c.Enter the number of years.
numberOfYears = input("Enter the number of years: ")
#3.Calculate
i = float(rate)/1200
month = 12
monthly = (float(i)*int(amountOfLoan)/(1-((1+float(i))**(-int(month)*int(numberOfYears)))))
#4.Display the result.
print("\nYour monthly payment will be $ "+str(round(monthly,2)))
