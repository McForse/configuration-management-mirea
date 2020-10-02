from MyLexer import MyLexer
from MyParser import MyParser

data = '''
(var1 (var3 (var5 (var6))) (var7 (var8 (543534))) (var9))
'''
lexer = MyLexer()

for token in lexer.tokenize(data):
    print(token)

print('\nParsing:')
parser = MyParser()
result = parser.parse(lexer.tokenize(data))
print(result)