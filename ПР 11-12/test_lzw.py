from hypothesis import given
from hypothesis.strategies import integers, builds, recursive


class Node:
    def __init__(self, val, child=None):
        self.left = None
        self.right = None
        self.val = val
        if child:
            if child.val < self.val:
                self.left = child
            else:
                self.right = child

    def insert(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
        return self

    def height(self):
        if self.val is not None:
            l_height = self.left.height() if self.left else 0
            r_height = self.right.height() if self.right else 0
            if l_height > r_height:
                return l_height + 1
            else:
                return r_height + 1
        else:
            return 0

    def contains(self, val):
        if self.val is None:
            return False
        elif val == self.val:
            return True

        return self.left.contains(val) if val < self.val else self.right.contains(val)

    def print(self, level=0):
        if self.right:
            self.right.print(level + 1)
        print('\t' * level, end='')
        print(self.val, end='〈\n')
        if self.left:
            self.left.print(level + 1)


@given(x=recursive(builds(Node, integers()), lambda child: builds(Node, integers(), child), max_leaves=10))
def test_property(x):
    # Вывод дерева
    x.print()
    print('-' * 10)

    # Проверки на высоту
    assert 0 < x.height() <= 11

    old_height = x.height()
    new_height = x.insert(100).height()
    assert new_height == old_height or new_height == old_height + 1

    # Проверка на поиск по ключу
    x.insert(5)
    assert x.contains(5) is True


test_property()
