# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys

sys.path.append('src')
sys.path.append('test')

def example_setup(*args, **kw):
    setup(
        name = "Example",
        auther = "Nobuaki Mochizuki",
        auther_email = "hagaeru3sei@yahoo.co.jp",
        liecnse      = "GPL",
        description  = "README",
        version      = "0.1",
        packages     = find_packages(),
        test_suite   = 'example_test.suite'
    )

if __name__ == "__main__":
    try:
        example_setup()
    except Exception, e:
        print e


