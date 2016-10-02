##unit test
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'

if __name__ == '__main__':
    unittest.main()


'''
ERROR: test_attrerror (__main__.TestDict)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "E:\Python27\python ex\unit test.py", line 33, in test_attrerror
    value = d.empty
  File "E:\Python27\python ex\mydict.py", line 10, in __getattr__
    raise AttributeError(r"'dict'object has no attribuate '%S'"%key)
ValueError: unsupported format character 'S' (0x53) at index 33

----------------------------------------------------------------------
Ran 5 tests in 0.098s

FAILED (errors=1)
>>> 
'''
