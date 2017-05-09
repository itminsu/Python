__author__ = 'Minsu Lee'

names = [ ]
votes = [ ]
numberOfCandidates = 0
count = 1

numberOfCandidates = int(input("Enter the number of candidates in the election: "))
print()

while count <= numberOfCandidates:
    names.append(input("Enter the name of candidate #"+ str(count) + ":"))
    votes.append(int(input("Enter the number of votes for candidate #"+ str(count) + ":")))
    print()
    count += 1
    if count > numberOfCandidates:
        break;
phrase = " "
print("-----------------------------------------------")
for steps in range(len(names)):
    percent = (votes[steps] / sum(votes) * 100)
    if votes[steps] == max(votes):
        phrase = "First Place!"
    elif votes[steps] == min(votes):
        phrase = "Last Place...HAHAHAHAHA!"
    else:
        phrase = " "
    print(str(names[steps])+ " "*(20-len(names[steps])) + " - " + str(round(percent))+"%" + " "+ str(phrase))
