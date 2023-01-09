from tkinter import N


class CouponBond:

    def __init__(self, principal, rate, maturity, interest_rate):
        self.principal = principal
        self.rate = rate / 100
        self.maturity = maturity
        self.interest_rate = interest_rate / 100

    def present_value(self, x, n):
        return x / (1 + self.interest_rate)**N

    def calculate_price(self):
        
        price = 0