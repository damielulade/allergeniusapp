import unittest
from src.routes import sum_two
from src.firebase import db


class Test(unittest.TestCase):

    def test_add_and_remove_data(self):
        data = {"data": "this is some test data"}
        db.child("test").push(data)
        query = db.child("test").get()
        for r in query.each():
            self.assertEqual(data, r.val())
        db.child("test").remove()


if __name__ == '__main__':
    unittest.main()

