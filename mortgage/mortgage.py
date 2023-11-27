"""
Description: A class meant to manage Mortgage options.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class Mortgage:
    """
    attributes: 
    - Loan Amount (float): The amount of the mortgage loan.
    - Rate (MortgageRate): The annual interest rate.
    - Frequency (int): The number of payments per year.
    - Amortization (int): The number of years to repay the mortgage loan.
    """
    def __init__(self,LoanAmount, Rate, Frequency, Amortization):
         # if LoanAmount is less then or equalto 0, raise ValueError
        if LoanAmount <= 0:
            raise ValueError("The Loan Amount must be positive")
        self._LoanAmount = LoanAmount
            
        #if Rate is not in MortgageRate enum, raise ValueError
        if not isinstance(Rate, MortgageRate):
            raise ValueError("The Rate provided is invalid")
        self.Rate = Rate
            
        #if Frequency is not in MortgageFrequency, raise ValueError
        if not isinstance(Frequency, MortgageFrequency):
            raise ValueError("The Frequency provided is invalid")
        self.Frequency = Frequency
            
        #if Amortization is not in the VALID_AMORTIZATION, raise ValueError
        if Amortization not in VALID_AMORTIZATION:
            raise ValueError("The Amortization provided is invalid")
        self.Amortization = Amortization
        
    @property
    def LoanAmount(self):
        return self._LoanAmount
    
    @LoanAmount.setter
    def LoanAmount(self,amount):
        if amount > 0:
            self._LoanAmount = amount
            
        elif amount <= 0:
            raise ValueError("Loan must be positive")
        
    @property
    def Frequency(self):
        return self._Frequency
    
    @Frequency.setter
    def Frequency(self,rate):
        if not isinstance(rate, MortgageFrequency):
            raise ValueError("Frequency provided is invalid")
        self._Frequency = rate

        
            