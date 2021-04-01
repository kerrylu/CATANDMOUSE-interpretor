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
def scan(file):
    output = []
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
            punctuationWarning = False  # if there is a punctuation warning, we have to deal with the punctuation AFTER the string is preceding it is processed
            punctuation = ''    # keeps track of which punctuation we need to deal with
            # tokens are separated by whitespace, end of line, and end of file
            if x == len(line)-1 or not line.strip()[x].isalnum():  # x is the index of the line that separates tokens
                if x != len(line)-1 and line.strip()[x] != ' ':     # handles punctuation warning
                    if line.strip()[x] in punctuationSymbols:
                        if line.strip()[x-1] != ' ':
                            print('Warning, need space between ' + str(line.strip()[x]) + ' and ' + str(line[start:x]))
                            punctuationWarning = True
                            punctuation = line.strip()[x]
                    else:   # handles invalid characters
                        print('Warning, invalid character: ' + str(line.strip()[x]) + ' after ' + str(line[start:x]))
                    string = line[start:x]
                    start = x+1
                elif x == len(line)-1:    # x marks end of line
                    if line.strip()[x] in punctuationSymbols:   # handles punctuation warning
                        if line.strip()[x-1] != ' ':
                            print('Warning, need space between ' + str(line.strip()[x]) + ' and ' + str(line[start:x]))
                            punctuationWarning = True
                            punctuation = line.strip()[x]
                            string = line[start:x]
                    elif not line.strip()[x].isalnum():     # handles invalid characters
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
                else:   # valid token
                    tokenType = findType(string)    # find the type of the token
                    if string not in symbolTable:   # update symbolTable
                        insertToSymbolTable(string, tokenType)
                    # Handle formatting of printing the output
                    if tokenType != '':  # encompasses variables and integers
                        output.append((string, tokenType))
                    else:   # keywords and punctuationSymbols are printed differently than variables and integers
                        output.append((string, tokenType))
                    if punctuationWarning:  # finally deals with punctuation warnings that we came across earlier
                        print(punctuation)
                string = '' # reinitialize string
        lineCounter += 1    # iterate lineCounter
    return output

# handle insertion into symbolTable
def insertToSymbolTable(string, tokenType):
    if tokenType == 'integer':   # integer types are inserted into the symbol table differently from variable types
        symbolTable[string] = ('integer', string, int(string))
    elif tokenType == 'variable':   # if variable
        symbolTable[string.strip()] = ('variable', string, 0)
    return

# check if string is a token
def isToken(string):
    if string.strip() == '': # filters out whitespace
        return False
    return True

# filters out edge cases
def isValidToken(string):
    # punctuation is not alphanumeric so we need to return True before any other checks
    if string == ';':
        return True
    # edge case: if string starts with 0, then the length of the string must be 1
    if string[0] == 0 and len(s) > 1:
        return False
    for ch in string:
        if not ch.isalnum():    # all characters in valid tokens should be alphabetical or digits
            return False
    return True

# finds token type
def findType(string):
    isVariable = True   # tracks if the token is a variable
    if string in keywords:  # string is a keyword
        isVariable = False
    elif string in punctuationSymbols:  # string is a punctuationSymbol
        isVariable = False
    elif 0 < len(string) <= 3:  # strings made up solely of integers are integer tokens if their length is 3 or less 
                                # and variables if length greater than 3
        isInteger = True    # tracks if the token is an integer
        for i in range(len(string)):
            if not string[i].isdigit():     # if any of the characters in the string are not integers, then the token is not an integer type
                isInteger = False
        if isInteger:
            return 'integer'
    if isVariable:
        return 'variable'
    else:
        return ''
