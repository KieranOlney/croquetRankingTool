from random import randint

def main():
    exampleInput =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]] 
    exampleOutput = leagueDecider(exampleInput)
    print("Example Input Result :",exampleOutput)
    randomInput = randInputGenerator(randint(5,200))
    randomOutput = leagueDecider(randomInput)
    print("Here is what we are putting into our decider :\n",randomInput)
    print("Here is what we are getting back :\n",randomOutput)
    return

def leagueDecider(playerList):
    leagueList = []
    for i in range(len(playerList)):
        if playerList[i][0] >= 55 and playerList[i][1] > 7:
            leagueList.append("Senior")
        else:
            leagueList.append("Open")
    return leagueList

def randInputGenerator(length):
    randomOutput = []
    for i in range(length):
        newPlayer = []
        newPlayer.append(randint(18,99))
        newPlayer.append(randint(-2,26))
        randomOutput.append(newPlayer)
    return randomOutput

main()