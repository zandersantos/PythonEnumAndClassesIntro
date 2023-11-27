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
    def __init__(self,LoanAmount: float, Rate: MortgageRate, Frequency: int, Amortization: int):
         # if LoanAmount is less then or equalto 0, raise ValueError
        if self.LoanAmount <= 0:
            raise ValueError("The Loan Amount must be positive")
        self.LoanAmount = LoanAmount
            
        #if Rate is not in MortgageRate enum, raise ValueError
        if self.Rate not in MortgageRate():
            raise ValueError("The Rate provided is invalid")
        self.Rate = Rate
            
        #if Frequency is not in MortgageFrequency, raise ValueError
        if self.Frequency not in MortgageFrequency():
            raise ValueError("The Frequency provided is invalid")
        self.Frequency = Frequency
            
        #if Amortization is not in the VALID_AMORTIZATION, raise ValueError
        if self.Amortization not in VALID_AMORTIZATION():
            raise ValueError("The Amortization provided is invalid")
        self.Amortization = Amortization

