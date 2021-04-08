import unittest
import myfunc

class TestMyFunc(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_addition(self): 
        self.assertEqual(myfunc.test_add(5), 6)
  
    def test_subtraction(self):
        self.assertEqual(myfunc.test_subtract(5), 4)

if __name__ == '__main__':
    unittest.main()
