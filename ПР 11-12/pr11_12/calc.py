# https://gist.github.com/maxkibble/1f0b4de51576ae75356c6a61b7aa1544
from operator import add, sub, mul, truediv


class Calculator(object):
    op = {'+': add, '-': sub, '*': mul, '/': truediv}

    def to_suffix(self, s):
        st = []
        ret = ''
        tokens = s.split()
        for tok in tokens:
            if tok in ['*', '/']:
                while st and st[-1] in ['*', '/']:
                    ret += st.pop() + ' '
                st.append(tok)
            elif tok in ['+', '-']:
                while st and st[-1] != '(':
                    ret += st.pop() + ' '
                st.append(tok)
            elif tok == '(':
                st.append(tok)
            elif tok == ')':
                while st[-1] != '(':
                    ret += st.pop() + ' '
                st.pop()
            else:
                ret += tok + ' '
        while st:
            ret += st.pop() + ' '
        return ret

    def eva(self, s):
        st = []
        tokens = s.split()
        for tok in tokens:
            if tok not in self.op:
                st.append(float(tok))
            else:
                n1 = st.pop()
                n2 = st.pop()
                st.append(self.op[tok](n2, n1))
        return st.pop()

    def evaluate(self, string):
        return self.eva(self.to_suffix(string))


def calc(s):
    c = Calculator()
    return c.evaluate(s)
