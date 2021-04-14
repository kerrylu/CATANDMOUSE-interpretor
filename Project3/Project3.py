# Project3.py

import scanner
import parser

if __name__ == "__main__":
    # create table
    file = open('./parsedata.txt', 'r')
    table = parser.readTable(file)
    #printOutput(table)
    file.close()

    # get tokens
    file = open('./' + input('Enter file name: '), 'r')
    tokenTypes = scanner.scan(file)
    #print(tokenTypes)
    file.close()

    # parser
    ret = parser.LRParseRoutine(tokenTypes+['$'], table)   # None if error, otherwise should be an array of productions
    if ret == None:
        print('CATANDMOUSE program is not syntactically correct')
    else:
        print('CATANDMOUSE program is syntactically correct')
        parser.printOutput(ret)