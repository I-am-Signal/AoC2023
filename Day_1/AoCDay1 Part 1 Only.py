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
        for character in line: # find individual digits
            if (character.isdigit()):
                numbers += character
                
        # Add first and last characters of numbers string to sum as an integer
        sum += int(numbers[0] + numbers[len(numbers) - 1])
    return sum
    
# Entry point
if __name__ == "__main__":
    print("The sum of all calibration values is",end=" ")
    print(getCalibrationValues(),end=".\n")