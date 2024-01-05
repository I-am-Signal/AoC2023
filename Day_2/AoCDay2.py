# Returns a array containing the formatted lines of the input file
def getInput():
    try:
        formattedArray = []
        input = open("input.txt", "r")
        
        # format the line, put it into the formatted array of lines
        for line in input:
            line = line.strip().split(" ")
            
            counter = 1
            while (counter < len(line)):
                if(',' in line[counter] or 
                   ';' in line[counter] or 
                   ':' in line[counter]):
                    line[counter] = line[counter][0:len(line[counter])-1]
                counter += 2
            formattedArray.append(line)
            
        input.close()
        return formattedArray
    except:
        print("An issue occurred with reading the input file.")
        import sys
        sys.exit()
    finally:
        input.close()


# checks every color in every game
def getPower(currentGame):
    # track each color cube's highest count
    redHi = 0
    greenHi = 0
    blueHi = 0
    
    currIndex = 3 # first color at index 3
    while (currIndex < len(currentGame)): # check every cube from each hand in the game
        
        # find the highest count of each color in the current game
        if (currentGame[currIndex] == "red"):
            redHi = max(redHi, int(currentGame[currIndex - 1]))
            
        elif (currentGame[currIndex] == "green"):
            greenHi = max(greenHi, int(currentGame[currIndex - 1]))
            
        elif (currentGame[currIndex] == "blue"):
            blueHi = max(blueHi, int(currentGame[currIndex - 1]))
        
        currIndex += 2 # game is still possible, continue search
    return redHi * greenHi * blueHi # calculate and return power total


# Main Method
def main():
    sum = 0
    for game in getInput():
        sum += getPower(game)
    
    print("The sum of the powers of the games is %s." % sum)


# Entry Point
if __name__ == "__main__":
    main()