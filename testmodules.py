from checkVersion import checkVersion
from overlap import overlap
import unittest

class TestoverlapMethod(unittest.TestCase):
    def test_returnsTrue(self):
        self.assertTrue(overlap((1,5),(2,6)))
    def test_returnsFalse(self):
        self.assertFalse(overlap((1,5),(6,8)))

class TestCheckVersionMethod(unittest.TestCase):
    def test_ReturnsLessThan(self):
        self.assertEqual(checkVersion('1.2','2.3'), '1.2 is less than 2.3')
    def test_ReturnsGreaterThan(self):
        self.assertEqual(checkVersion('3.3','2.3'), '3.3 is greater than 2.3')
    def test_ReturnsErrorMessage(self):
        self.assertEqual(checkVersion('foo','2.3'), 'Please call the method like this: checkVersion("float","float")')

if __name__ == '__main__':
    unittest.main()