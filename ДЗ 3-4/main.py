from MyLexer import MyLexer
from MyParser import MyParser

data = 'test_var = 5 // Комментарий'

lexer = MyLexer()
parser = MyParser()

print('Token list:')

for token in lexer.tokenize(data):
    print('Token(type=%r, value=%r)' % (token.type, token.value))

print('\nParsing:')
result = parser.parse(lexer.tokenize(data))
print(result)