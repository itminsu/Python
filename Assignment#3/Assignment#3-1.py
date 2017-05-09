__author__ = 'Minsu Lee'
#declare the List
numbers = [ ]
#loop to get 5 numbers
for value in range(5):
    numbers.append(int(input("Enter value #" + str(value + 1) + ": ")))
#Print the reverse order
print("---------------------------------------------------")
print("Numbers in reverse order")
numbers.reverse()
for value in range(len(numbers)):
    print(numbers[value])
numbers.reverse()
print("---------------------------------------------------")
#make a function to get average
def average(nums):
    total = sum(nums)
    return total / len(nums)
averageOfNumbers = float(average(numbers))
#print greater numbers than average
print("The average of the number is: " + str(averageOfNumbers))
print("---------------------------------------------------")
print("Numbers that are greater than the average")
#loop to get greater number than average
for value in range(len(numbers)):
    if numbers[value] > averageOfNumbers:
        print(numbers[value])