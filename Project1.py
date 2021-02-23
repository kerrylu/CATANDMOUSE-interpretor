# Project1.py
# Scans input file of language CATANDMOUSE and identifies all tokens and prints their associated information

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
# create table of punctuationSymbols and their associated types
punctuationSymbols = {
    ';': ';'
}

# scanner
def findTokens(file):
    lineCounter = 1 # initialize lineCounter at 1 as according to the project doc
    for line in file:
        line = line.strip() # remove whitespace
        start = 0   # initalize the start index of the token string that we want to check
        string = '' # initialize token string
        isComment = False   # tracks whether the line is a comment or not
        for x in range(len(line)):
            # comment check
            if line[x] == '/' and line[x+1] and line[x+1] == '/':
                isComment = True
            # skip everything if comment
            if isComment:
                continue
            punctuationWarning = False
            punctuation = ''
            # tokens are separated by whitespace, end of line, and end of file
            if x == len(line)-1 or not line.strip()[x].isalnum():  # x is the index of the line that separates tokens
                if x != len(line)-1 and line.strip()[x] != ' ':
                    if line.strip()[x] in punctuationSymbols:
                        if line.strip()[x-1] != ' ':
                            print('Warning, need space between ' + str(line.strip()[x]) + ' and ' + str(line[start:x]))
                            punctuationWarning = True
                            punctuation = line.strip()[x]
                    else:
                        print('Warning, invalid character: ' + str(line.strip()[x]) + ' after ' + str(line[start:x]))
                    string = line[start:x]
                    start = x+1
                elif x == len(line)-1:    # x marks end of line
                    if line.strip()[x] in punctuationSymbols:
                        if line.strip()[x-1] != ' ':
                            print('Warning, need space between ' + str(line.strip()[x]) + ' and ' + str(line[start:x]))
                            punctuationWarning = True
                            punctuation = line.strip()[x]
                            string = line[start:x]
                    elif not line.strip()[x].isalnum():
                        print('Warning, invalid character: ' + str(line.strip()[x]) + ' after ' + str(line[start:x]))
                        string = line[start:x]
                    else:
                        # since x is at the end of the line, we don't need to set an upper bound
                        string = line[start:]
                else:   # x marks whitespace
                    # set upper bound so that string has no whitespace
                    string = line[start:x]
                    # we need to update start because we are still iterating through the same line and don't want redundant strings
                    start = x+1
            # iterate character by character and check if the string is a token
            string = string.lower()     # language is case insensitive
            if isToken(string):         # filters out pure whitespace
                if not isValidToken(string):    # handles invalid tokens
                    print('Error, line number ' + str(lineCounter) + ', invalid token: ' + string)
                else:
                    # if string is a keyword, return its type and None for its value
    
                    # if string is a punctuation symbol, return its type and None for its value

                    # if string is an integer, enter it into the symbol table.
                    # the type of an integer is int.
                    # store the character value and convert the character string to an int and then store the int value

                    # if string is a variable, enter it into the symbol table
                    # the type of a variable is variable.
                    # character value is the name of a variable with all letters in lowercase, and its int value is 0 for now.

                    isVariable = True   # tracks if the token is a variable
                    if string in keywords:  # string is a keyword
                        isVariable = False
                    elif string in punctuationSymbols:  # string is a punctuationSymbol
                        isVariable = False
                    elif 0 < len(string) <= 3:  # strings made up solely of integers are integer tokens if their length is 3 or less 
                                                # and variables if length greater than 3
                        isInteger = True    # tracks if the token is an integer
                        for i in range(len(string)):
                            if not string[i].isdigit():     # if any of the characters in the string are not integerss, then the token is not an integer type
                                isInteger = False 
                        if isInteger:   # integer types are inserted into the symbol table differently from variable types
                            if string not in symbolTable:
                                symbolTable[string] = ('integer', string, int(string))
                        else:   # if variable
                            if string not in symbolTable:
                                symbolTable[string.strip()] = ('variable', string, 0)
                    else:   # string is a variable
                        if string not in symbolTable:
                            symbolTable[string.strip()] = ('variable', string, 0)
                    # Handle formatting of printing the output
                    # print out the following information for each token in three columns: 
                    # the type of token, the character value, and the integer value. 
                    # If the token is not entered into the symbol table, then the character and integer values are left blank.
                    if isVariable:  # encompasses variables and integers
                        print(symbolTable[string.strip()][0] + '  ' + symbolTable[string.strip()][1] + '  ' + str(symbolTable[string.strip()][2]))
                    else:   # keywords and punctuationSymbols are printed differently than variables and integers
                        print(string.strip())
                    if punctuationWarning:
                        print(punctuation)
                string = '' # reinitialize string
        lineCounter += 1    # iterate lineCounter
                
    return 0

# check if string is a token
def isToken(s):
    if s.strip() == '': # filters out whitespace
        return False
    return True

# filters out edge cases
def isValidToken(s):
    # punctuation is not alphanumeric so we need to return True before any other checks
    if s == ';':
        return True
    # edge case: if string starts with 0, then the length of the string must be 1
    if s[0] == 0 and len(s) > 1:
        return False
    for ch in s:
        if not ch.isalnum():    # all characters in valid tokens should be alphabetical or digits
            return False
    return True

if __name__ == "__main__":
    # Prompt user for the name of CATANDMOUSE program to test
    file = open('./' + input('Enter file name: '), 'r')
    print('TYPE' + '  ' + 'CH VALUE' + '  ' + 'INT VALUE')
    print('====  ' + '========  ' + '=========')
    findTokens(file)        # find and handle tokens
    file.close()