import sys
import interpreter


def getFileContent(path):
    with open(path, 'r') as theFile:
        data = theFile.read()
        return data


args = sys.argv

if len(args) != 2:
    print('Error! Wrong number of arguments')
    exit()

try:
    print(interpreter.toJson(getFileContent(args[1])))
except FileNotFoundError:
    print('File not found!')
