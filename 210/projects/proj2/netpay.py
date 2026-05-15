# CIS 210 Project 2
# Author: Quinn Smiley
# Credits: N/A
# Creating tax() and netpay() functions.

def tax(gross_pay):
    return gross_pay * 0.15

# print(tax(200))
# print(tax(125))

def netpay(hours_worked):
    gross_pay = hours_worked * 16.25
    tax_amount = gross_pay - tax(gross_pay)
    return round(tax_amount, 2)

# print(netpay(1))
# print(netpay(40))

def main():
    '''Net pay program driver.'''
    print('For 1 hour of work, netpay is: ', netpay(1))
    print('For 40 hours of work, netpay is: ', netpay(40))
    return None
if __name__ == '__main__':
   main()