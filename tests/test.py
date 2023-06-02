import unittest

try:
    from src.routes import sum_two
except ModuleNotFoundError:
    import sys
    from os.path import abspath, dirname
    sys.path.append(abspath(dirname(__file__)) + '/../src')
    from routes import sum_two


class Test(unittest.TestCase):

    def test_calc(self):
        value = sum_two(4, 5)
        self.assertEqual(value, 9)


if __name__ == '__main__':
    unittest.main()


# import unittest
# from routes import sum_two
#
#
# class Test(unittest.TestCase):
#
#     def test_calc(self):
#         value = sum_two(4, 5)
#         self.assertEquals(value, 9)
#
#
# if __name__ == '__main__':
#     unittest.main()
