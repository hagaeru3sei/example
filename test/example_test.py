# -*- coding: utf-8 -*-
import unittest
from example import *

class TestExample(unittest.TestCase):
    
    def test_example(self):

        """ Example test """

        try:
            print "Example test"
            self.assertTrue(True)
        except Exception, e:
            print "fail."
            self.fail(e)

def suite():
    suite = unittest.TestCase()
    suite.addTests(unittest.makeSuite(TestExample))
    return suite
