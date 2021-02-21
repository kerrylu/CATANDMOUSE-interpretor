import argparse

# initialize symbol table
symbolTable = {}
# create table of keywords and their associated types
keywords = {
    'begin': 'begin',
    'halt': 'halt',
    'cat': 'cat',
    'mouse': 'mouse',
    'clockwise': 'clockwise',
    'move': 'move',
    'north': 'north',
    'south': 'south',
    'east': 'east',
    'west': 'west',
    'hole': 'hole',
    'repeat': 'repeat',
    'size': 'size',
    'end': 'end'
}
punctuationSymbols = {
    ';': ';'
}

# scanner
def findTokens(file):
    for line in file:
        line = line.strip()
        temp = 0
        string = ''
        isComment = False
        for x in range(len(line)):
            if line[x] == '/' and line[x+1] and line[x+1] == '/':
                isComment = True
            if isComment:
                continue
            if x == len(line)-1 or line.strip()[x] == ' ':
                if x == len(line)-1:
                    string = line[temp:x+1]
                    temp = x+1
                else:
                    string = line[temp:x]
                    temp = x
    # iterate character by character and check if the string is a token
            if isToken(string):
                if string in keywords:
                    print(keywords[string])
                elif string in punctuationSymbols:
                    print(punctuationSymbols[string])
                elif 0 <= len(string) <= 3:
                    isInteger = True
                    for i in range(len(string)):
                        if not string[i].isdigit():
                            isInteger = False
                    if isInteger:
                        if string not in symbolTable:
                            symbolTable[string] = ('integer', string, int(string))
                    else:
                        if string not in symbolTable:
                            symbolTable[string.strip()] = ('variable', string, 0)
                else:
                    if string not in symbolTable:
                        symbolTable[string.strip()] = ('variable', string, 0)
                string = ''
    return



                    

                
    # if string is a keyword, return its type and None for its value

    # if string is a punctuation symbol, return its type and None for its value

    # if string is an integer, enter it into the symbol table.
    # the type of an integer is int.
    # store the character value and convert the character string to an int and then store the int value

    # if string is a variable, enter it into the symbol table
    # the type of a variable is variable.
    # character value is the name of a variable with all letters in lowercase, and its int value is 0 for now.

    return
# check if string is a token
def isToken(s):
    # TODO: Stack?
    if s == '':
        return False
    return True
# check if variable name is valid
def isValidVariableName(s):
    return

# handle tokens
def insertToken(file):
    return
# Handle Output
def printOutput():
    # print out the following information for each token in three columns: 
    # the type of token, the character value, and the integer value. 
    # If the token is not entered into the symbol table, then the character and integer values are left blank.
    return
# Error Handling
def handleError():
    # When an invalid token is found, report it as an error, list the line number the error occured on, and continue processing.
    # When an invalid token is encountered in the scanner, print an error message indicating the error and the line number, and the token, then continue scanning for the next token.
    return
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    # TODO: Prompt user for the name of CATANDMOUSE program to test
    findTokens(args.file)
    print(symbolTable)
    # TODO: execute functions on input file
