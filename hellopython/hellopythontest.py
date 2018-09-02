import unittest
from hellopython import *

class TestHelloWorld(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello python')

if __name__ == '__main__':
    unittest.main()
