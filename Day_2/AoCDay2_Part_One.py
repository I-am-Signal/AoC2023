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
def isPossible(currentGame):
    currIndex = 3 # first color at index 3
    while (currIndex < len(currentGame)): # check every cube from each hand in the game
        
        # not a possible game
        if (not ((currentGame[currIndex] == "red" and int(currentGame[currIndex - 1]) <= 12) or 
           (currentGame[currIndex] == "green" and int(currentGame[currIndex - 1]) <= 13) or 
           (currentGame[currIndex] == "blue" and int(currentGame[currIndex - 1]) <= 14))):
            return 0
        
        currIndex += 2 # still possible, continue search
    return int(currentGame[1]) # all values in game are possible


# Main Method
def main():
    sum = 0
    for game in getInput():
        sum += isPossible(game)
    
    print("The sum of the game IDs of games that were possible is %s." % sum)


# Entry Point
if __name__ == "__main__":
    main()