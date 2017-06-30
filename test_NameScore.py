import unittest
from NameScore import NameScore

class NameScoreTest(unittest.TestCase):
    
    def test_NameScore1(self):
        file_data = '"CDEF","ABC","FIJK"'
        expected_value = [6, 36, 108]
        value = NameScore(file_data)
        self.assertEqual(value, expected_value)

    def test_NameScore2(self):
        file_data = '"CGABQZX"'
        expected_value = [80]
        value = NameScore(file_data)
        self.assertEqual(value, expected_value)

    def test_NameScore3(self):
        file_data = '"","AB","ZOIU"'
        expected_value = [3,142]
        value = NameScore(file_data)
        self.assertEqual(value, expected_value)

    def test_NameScore4(self):
        file_data = '"!!!!","@@=+","FIJK"'
        expected_value = [36]
        value = NameScore(file_data)
        self.assertEqual(value, expected_value)

    def test_NameScore5(self):
        file_data = '"CDEF","ABC","FIJK","99678"'
        expected_value = [6, 36, 108]
        value = NameScore(file_data)
        self.assertEqual(value, expected_value)

if __name__ == '__main__':
    unittest.main()
