import unittest
from NameScore import NameScore

class NameScoreTest(unittest.TestCase):
    
    def test_NameScore(self):
        self.assertEqual(NameScore("name.dat"), [6,36,108])

if __name__ == '__main__':
    unittest.main()