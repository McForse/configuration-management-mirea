from hypothesis import given
import hypothesis.strategies as st

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "Tree(val=%s, left=%s, right=%s)" % (self.val, self.left, self.right)


# TODO
#@given(...)
def test_tree():
    pass


test_tree()
