# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:05:13 2018

@author: prithvisekhp
"""

import unittest 
from WebScraperForTAGv1 import jobsiteIndeed
# import palindromeCheck
skill = "embedded+systems"
location = "Bengaluru%2C+Karnataka"
resultLinks = []

class MyTest(unittest.TestCase):
    def test_my_function(self):
        #self.assertEqual(jobsiteIndeed(skill, location, resultLinks), 0)
        self.assertEqual(jobsiteIndeed(skill, location, resultLinks), 1)
       
        
        
        
if __name__ == '__main__':
    unittest.main()   
