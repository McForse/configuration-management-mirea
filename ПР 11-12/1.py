def unique_elements(lst):
    """
    Количество элементов в списке, встречающихся только один раз
    >>> unique_elements([1, 2, 1, 3, 3])
    1
    >>> unique_elements([1, 2, 2, 1, 3, 5, 5, 5, 6, 7, 3, 9])
    3
    >>> unique_elements([])
    None
    """
    if lst:
        return len([x for x in set(lst) if lst.count(x) == 1])
    else:
        return None


def test_unique_elements():
    assert unique_elements([1, 2, 1, 3, 3]) == 1
    assert unique_elements([1, 2, 2, 1, 3, 5, 5, 5, 6, 7, 3, 9]) == 3
    assert unique_elements([]) is None
