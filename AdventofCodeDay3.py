# Advent of Code
# Day 3 (Day 1)
# Dylan Carder
# December 3rd, 2023

# Thought process:

# need to find each number by digit in the list
# when found, we need to know the complete list of indexes the number covers
# To check each index, need to run through the following checks
# i being the outer list index, j being the inner list index
# A u B   A = i-1, j-1    u and l
# l 4 r   u = i-1, j
# C d D   B = i-1, j+1    u and r
#         l = i, j-1
#         r = i, j+1
#         C = i+1, j-1    d and l
#         d = i+1, j
#         D = i+1, j+1    d and r
# once a condition is selected, that part can be checked for a non period, non number
#           if not(list[i][j] == "." or list[i][j].isnumeric())      number to be added to final sum


# checkIndex method:
#  check if valid indexing conditions
#    check if at that index there is a non period/non number
#      return true if this is the case
#    return false otherwise
def checkIndex(currList, index, list):
    # check A index
    if currList >= 0 and index >= 0:
        # check if A is a symbol
        if not (
            list[currList - 1][index - 1].isnumeric()
            or list[currList - 1][index - 1] == "."
        ):
            return True
        
    # check B index
    if currList >= 0 and index + 1 < len(list[currList]):
        # check if B is a symbol
        if not (
            list[currList - 1][index + 1].isnumeric()
            or list[currList - 1][index + 1] == "."
        ):
            return True
        
    # check C index
    if currList + 1 < len(list) and index >= 0:
        # check if C is a symbol
        if not (
            list[currList + 1][index - 1].isnumeric()
            or list[currList + 1][index - 1] == "."
        ):
            return True
        
    # check D index
    if currList + 1 < len(list) and index + 1 < len(list[currList]):
        # check if D is a symbol
        if not (
            list[currList + 1][index + 1].isnumeric()
            or list[currList + 1][index + 1] == "."
        ):
            return True
        
    # check u index
    if currList >= 0:
        # check if u is a symbol
        if not (
            list[currList - 1][index].isnumeric() or list[currList - 1][index] == "."
        ):
            return True
        
    # check d index
    if currList + 1 < len(list):
        # check if d is a symbol
        if not (
            list[currList + 1][index].isnumeric() or list[currList + 1][index] == "."
        ):
            return True
    if index >= 0:
        # check l
        if not (
            list[currList][index - 1].isnumeric() or list[currList][index - 1] == "."
        ):
            return True
    if index + 1 < len(list[currList]):
        # check r
        if not (
            list[currList][index + 1].isnumeric() or list[currList][index + 1] == "."
        ):
            return True
    return False # if there is not a symbol around the digit


# parse Method:
#  finds the numbers in the schematics, 
#  checks if there is symbols,
#  adds number to sum if there are symbols
def parse(input):
    # find the complete number's indexes
    sum = 0
    i = 0
    while i < len(input):
        currSize = len(input[i])
        j = 0
        while j < len(input[i]):  # find any numbers
            if input[i][j] == ".":  # skip periods
                j += 1
                continue

            elif input[i][j].isnumeric():  # number found
                indexes = []  # contains the indexes of the number found
                x = j  # temporary indexing variable
                difference = 0  # difference variable to add difference back for accurate indexing
                strNum = ""  # stores string format number

                while x < len(input[i]):  # get indexes of number
                    if input[i][x].isnumeric():
                        strNum += input[i][x]
                        indexes.append(x)
                        x += 1
                        difference += 1  # keep track of difference
                        continue
                    else:  # end of number
                        break
                for index in indexes:  # check if number is part number
                    if checkIndex(
                        i, index, input
                    ):
                        sum += int(strNum)
                        break
                j += difference - 1  # update j with accurate index
            j += 1
        i += 1
    return sum


# Main Method
if __name__ == "__main__":
    engineInput = [ # engine schematics, example 1
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    engineInput2 = [ # engine schematics, example 2
        ".......42.",
        "......$...",
        "..72*.....",
        "......93#.",
        "84........",
        ".....69...",
        ".......+..",
        ".420......",
        "..-.......",
        ".......96.",
    ]

    sum = parse(engineInput)
    #sum = parse(engineInput2)
    print("The sum of the part numbers is ", end="")
    print(sum)