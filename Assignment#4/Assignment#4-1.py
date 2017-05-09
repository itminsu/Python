__author__ = 'w0293156'
#import function
import csv
import random

def toLowerCase(str):
    list_str = list(str)
    for i in range(len(list_str)):
        list_str[i] = list_str[i].lower()
    return ''.join(list_str)

def toUpperCase(str):
    list_str = list(str)
    for i in range(len(list_str)):
        list_str[i] = list_str[i].upper()
    return ''.join(list_str)

def fileRead(fileName): # Read a file and store it in a list and then return that list.
    myCSVFile = None
    try:
        with open(fileName,"r") as myCSVFile:
            dataFromFile = csv.reader(myCSVFile)
            list_fileContents = []
            for row in dataFromFile:
                for value in row:
                    list_fileContents.append(value)
        return list_fileContents
    except IOError:
        print("Error writing to file!")
    except PermissionError:
        print("Incorrect permissions, cannot write to file.")
    except:
        print("Some other error occurred")
    finally:
        myCSVFile.close()

def fileWrite(fileName,list_fileContents):
    myFile = None   # Set myFile to nothing to start
    try:
        myFile = open(fileName, "w")     # Attempt to open the file
        upperLine = random.randint(1,len(list_fileContents)) # Determine which line is gonna be converted into capital letters

        # Loop through list, from 1 to length of list, using ONE-based counter, instead of zero-based
        for i in range(1, len(list_fileContents) + 1):
           # If it's not on the final row, add the line break.
            if i != len(list_fileContents):
                if i == upperLine: # If encounter upperline, change that into uppercase
                    line = str(i) + ': '+ toUpperCase(list_fileContents[i - 1]) + "\n"
                    myFile.write(line)
                    print(line, end="") # write to the console ...
                else: # Otherwise, change that into lowercase
                    line = str(i) + ': '+ toLowerCase(list_fileContents[i - 1]) + "\n"
                    myFile.write(line)
                    print(line, end="")

            # Skip writing the line break on the very last row, so we don't finish with an empty line
            else:
                if i == upperLine: # If encounter upperline, change that into uppercase
                    line = str(i) + ': '+ toUpperCase(list_fileContents[i - 1])
                    myFile.write(line)
                    print(line, end="")
                else: # Otherwise, change that into lowercase
                    line = str(i) + ': '+ toLowerCase(list_fileContents[i - 1])
                    myFile.write(line)
                    print(line, end="")
#Display error message
    except IOError:
        print("IOError - cannot write a file!")
    except PermissionError:
        print("PermissionErro - cannot write a file.")
    except:
        print("Error occurred")
    finally:
        myFile.close()

#Function to convert a file
def convertFile(fileName,newFileName):
    list_fileContents = fileRead(fileName)
#Print a New file
    fileWrite(newFileName,list_fileContents)

#Run the files
fileName = "Assignment#4-1_OldFile.txt"
newFileName = "Assignment#4-1_NewFile.txt"
#Convert the files
convertFile(fileName,newFileName)