import sys
import traceback
from GitParser import GitParser

args = sys.argv

if len(args) != 2:
    print('Error! Wrong number of arguments')
    exit()

path = args[1]

try:
    parser = GitParser(path)
except ValueError:
    traceback.print_exc()
