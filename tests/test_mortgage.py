"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
import unittest
from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class MortgageTests(unittest.TestCase):
    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            
            Mortgage(0.0,MortgageRate(1),MortgageFrequency(1),VALID_AMORTIZATION[1])
        
        with self.assertRaises(ValueError):
            
            Mortgage(-1.0,MortgageRate(1),MortgageFrequency(1),VALID_AMORTIZATION[1])
            
    def test_invalid_rate_value(self):
        with self.assertRaises(ValueError):
            
            Mortgage(10.0,34324,MortgageFrequency(1),VALID_AMORTIZATION[1])
    
    def test_invalid_freq_value(self):
        with self.assertRaises(ValueError):
            
            Mortgage(10.0,MortgageRate(1),13,VALID_AMORTIZATION[1])
                  
    def test_invalid_amort_value(self):
        with self.assertRaises(ValueError):
            
            Mortgage(10.0,MortgageRate(1),MortgageFrequency(1),23)
        

if __name__ == "__main__":
    unittest.main()



