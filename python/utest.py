import unittest

class TestStringMethods(unittest.TestCase):
  @staticmethod
  def abc():
    try:
      1/0
    except:
      pass

  @staticmethod
  def bcd():
    pass

  @classmethod
  def setUpClass(cls):
    print("--setUpClass stage")

  @classmethod
  def tearDownClass(cls):
    print("--tearDownClass stage")

  def setUp(self):
    print("--setUp stage")

  def tearDown(self):
    print("--tearDown stage")

  def test_upper(self):
    self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
    self.assertTrue('FOO'.isupper())
    self.assertFalse('Foo'.isupper())

  def test_split(self):
    s = 'hello world'
    self.assertEqual(s.split(), ['hello', 'world'])
    # check that s.split fails when the separator is not a string
    with self.assertRaises(TypeError):
      s.split(2)

  def test_raise(self):
    print("test_raises")
    self.assertRaises(self.abc())
    self.assertRaises(self.bcd())
    self.assertRaises(lambda x: None)

if __name__ == '__main__':
  unittest.main()

