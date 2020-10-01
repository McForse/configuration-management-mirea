from MyLexer import MyLexer
from MyParser import MyParser

data = '''
(var1 var2 (var3 var4 (var5 var6)) (var7 ("fsfdfdsfsf" 543534)) (var9))
'''
# var1 (var0 var01) (var2 (var3 var4))
lexer = MyLexer()
for token in lexer.tokenize(data):
    print(token)

print('\nParsing:')
parser = MyParser()
result = parser.parse(lexer.tokenize(data))
print(result)