import unittest

from Dict import Dict

class UnitTest(unittest.TestCase):

    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d,a,1)
        self.assertEqual(d,b,'test')
        self.assertTrue(isinstance(d,dict))

