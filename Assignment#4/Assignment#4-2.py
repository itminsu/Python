__author__ = 'w0293156'
import csv
#Function to read a file and store in a list and then return.
def readQuiz(fileName):
    myCSVFile = None
    try:
        with open(fileName,"r") as myCSVFile:
            dataFile = csv.reader(myCSVFile,delimiter="\n")
            fileContents = []
            for row in dataFile:
                for value in row:
                    fileContents.append(value)
        return fileContents
#Display error message
    except IOError:
        print("IOError - cannot write a file!")
    except PermissionError:
        print("PermissionErro - cannot write a file.")
    except:
        print("Error occurred")
    finally:
        myCSVFile.close()

#Function to run a quiz
def runQuiz(listOfQuiz):
    count = 0
    score = 0
    while count < len(listOfQuiz):
        list_eachQuestion = listOfQuiz[count].split(',')

        print('\n'+list_eachQuestion[0])
        print('a) ' + list_eachQuestion[1])
        print('b) ' + list_eachQuestion[2])
        print('c) ' + list_eachQuestion[3])
        print('d) ' + list_eachQuestion[4])
        choice = input('Choice (a-d): ').upper()
        if choice != 'A' and choice != 'B' and choice != 'C' and choice != 'D':
            print('\nEnter a letter \"a-d\"')
            continue
        elif choice == list_eachQuestion[5]:
            score += 1
        count += 1
    return score

#Run the files
fileName = "Assignment#4-2_Quiz.txt"
listOfQuiz = readQuiz(fileName)
# Read a quiz file and store in a list
lengthOfQuiz = len(listOfQuiz)
# Run a quiz function
score = runQuiz(listOfQuiz)
#Print the result
print("\nYour score is: {0}/{1} ({2:.0%})".format(score,lengthOfQuiz,score/lengthOfQuiz))
