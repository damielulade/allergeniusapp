import unittest
from app import sum_two


class Test(unittest.TestCase):

    def test_calc(self):
        value = sum_two(4, 5)
        self.assertEquals(sum_two, 9)


if __name__ == '__main__':
    unittest.main()
