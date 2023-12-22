# Returns a formatted array containing the lines of the input file
def getInput():
    try:
        formattedArray = []
        input = open("input.txt", "r")
        for line in input:
            formattedArray.append(line.strip())
        input.close()
        return formattedArray
    except:
        print("An issue occurred with reading the input file.")
        import sys
        sys.exit()
    finally:
        input.close()

# Gets the calibration values
def getCalibrationValues():
    input = getInput() # get input 2D array
    sum = 0 # hold sum
    
    for line in input: # check each line, find calibration values
        
        numbers = "" # string to hold all found digits
        characterCounter = 0 # looping variable initialization
        
        while (characterCounter < len(line)): # find individual digits
            
            if (line[characterCounter].isdigit()): # character is a digit
                numbers += line[characterCounter]
                
            if ((len(line) - characterCounter) >= 3): # line is at least 3 chars long
                
                if (line[characterCounter:characterCounter + 3] == "one"):
                    numbers += '1'
                    
                elif (line[characterCounter:characterCounter + 3] == "two"):
                    numbers += '2'
                    
                elif (line[characterCounter:characterCounter + 3] == "six"):
                    numbers += '6'
                    
            if ((len(line) - characterCounter) >= 4): # line is at least 4 chars long
                
                if (line[characterCounter:characterCounter + 4] == "four"):
                    numbers += '4'
                
                elif (line[characterCounter:characterCounter + 4] == "five"):
                    numbers += '5'
                
                elif (line[characterCounter:characterCounter + 4] == "nine"):
                    numbers += '9'
            
            if ((len(line) - characterCounter) >= 5): # line is at least 5 chars long
                
                if (line[characterCounter:characterCounter + 5] == "three"):
                    numbers += '3'
                
                elif (line[characterCounter:characterCounter + 5] == "seven"):
                    numbers += '7'
                
                elif (line[characterCounter:characterCounter + 5] == "eight"):
                    numbers += '8'
                    
            characterCounter += 1 # increment loop variable
        
        # Add first and last characters of numbers string to sum as an integer
        sum += int(numbers[0] + numbers[len(numbers) - 1])
    return sum
    
# Entry Point
if __name__ == "__main__":
    print("The sum of all calibration values is",end=" ")
    print(getCalibrationValues(),end=".\n")