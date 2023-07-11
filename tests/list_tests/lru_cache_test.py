import unittest
from typing import Optional, Callable

from datastax.Lists import LRUCache


class TestLRUCache(unittest.TestCase):

    def setUp(self) -> None:
        self.operations: list[str] = []
        self.parameters: list[list[int]] = []

    def test_case1(self):
        self.operations = ['LRUCache', 'put', 'put', 'put', 'put', 'put',
                           'get', 'put', 'get', 'get', 'put', 'get', 'put',
                           'put', 'put', 'get', 'put', 'get', 'get', 'get',
                           'get', 'put', 'put', 'get', 'get', 'get', 'put',
                           'put', 'get', 'put', 'get', 'put', 'get', 'get',
                           'get', 'put', 'put', 'put', 'get', 'put', 'get',
                           'get', 'put', 'put', 'get', 'put', 'put', 'put',
                           'put', 'get', 'put', 'put', 'get', 'put', 'put',
                           'get', 'put', 'put', 'put', 'put', 'put', 'get',
                           'put', 'put', 'get', 'put', 'get', 'get', 'get',
                           'put', 'get', 'get', 'put', 'put', 'put', 'put',
                           'get', 'put', 'put', 'put', 'put', 'get', 'get',
                           'get', 'put', 'put', 'put', 'get', 'put', 'put',
                           'put', 'get', 'put', 'put', 'put', 'get', 'get',
                           'get', 'put', 'put', 'put', 'put', 'get', 'put',
                           'put', 'put', 'put', 'put', 'put', 'put']

        self.parameters = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10],
                           [13], [2, 19], [2], [3], [5, 25], [8], [9, 22],
                           [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9],
                           [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1],
                           [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4],
                           [12, 24], [5, 18], [13], [7, 23], [8], [12],
                           [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18],
                           [1, 7], [6], [9, 29], [8, 21], [5], [6, 30],
                           [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
                           [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3],
                           [9], [6], [3, 4], [1], [10], [3, 29], [10, 28],
                           [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9],
                           [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15],
                           [12], [9, 19], [2, 15], [3, 16], [1], [12, 17],
                           [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7],
                           [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22],
                           [7, 24], [9, 26], [13, 28], [11, 26]]

        expected = [None, None, None, None, None, None, -1, None, 19, 17, None,
                    -1, None, None, None, -1, None, -1, 5, -1, 12, None, None,
                    3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None,
                    None, None, -1, None, -1, 24, None, None, 18, None, None,
                    None, None, -1, None, None, 18, None, None, -1, None, None,
                    None, None, None, 18, None, None, -1, None, 4, 29, 30,
                    None, 12, -1, None, None, None, None, 29, None, None, None,
                    None, 17, 22, 18, None, None, None, -1, None, None, None,
                    20, None, None, None, -1, 18, 18, None, None, None, None,
                    20, None, None, None, None, None, None, None]

        self.assertEqual(self.operate(), expected)

    def test_case2(self):
        self.operations = ['LRUCache', 'get', 'put', 'get', 'put', 'put',
                           'get', 'get']
        self.parameters = [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
        expected = [None, -1, None, -1, None, None, 2, 6]
        self.assertEqual(self.operate(), expected)

    def test_case3(self):
        self.operations = ['LRUCache', 'put', 'put', 'put', 'put', 'get',
                           'get']
        self.parameters = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
        expected = [None, None, None, None, None, -1, 3]
        self.assertEqual(self.operate(), expected)

    def test_case4(self):
        self.operations = ['LRUCache', 'put', 'put', 'get', 'put', 'get',
                           'put', 'get', 'get', 'get']

        self.parameters = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1],
                           [3], [4]]
        expected = [None, None, None, 1, None, -1, None, -1, 3, 4]
        self.assertEqual(self.operate(), expected)

    def test_case5(self):
        self.operations = ['LRUCache', 'put', 'put', 'put', 'put', 'get',
                           'get', 'get', 'get', 'put', 'get', 'get', 'get',
                           'get', 'get']
        self.parameters = [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2],
                           [1], [5, 5], [1], [2], [3], [4], [5]]
        expected = [None, None, None, None, None, 4, 3, 2, -1, None, -1, 2, 3,
                    -1, 5]
        self.assertEqual(self.operate(), expected)

    def operate(self) -> list[Optional[int]]:
        lru_cache = LRUCache(*self.parameters[0])
        function: dict[str, Callable] = {
            'put': lru_cache.put,
            'get': lru_cache.get
        }
        result: list[Optional[int]] = [None]
        for operation, param in zip(self.operations[1:], self.parameters[1:]):
            res = function[operation](*param)
            result.append(res)
        return result


if __name__ == '__main__':
    unittest.main()
