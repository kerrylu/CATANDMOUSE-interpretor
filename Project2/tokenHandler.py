from scanner import keywords, punctuationSymbols, symbolTable

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
        