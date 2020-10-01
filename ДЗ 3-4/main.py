from MyLexer import MyLexer
from MyParser import MyParser

data = '''
(var1 var2 var3)
'''
lexer = MyLexer()
for token in lexer.tokenize(data):
    print(token)

print('\nParsing:')
parser = MyParser()
result = parser.parse(lexer.tokenize(data))
print(result)