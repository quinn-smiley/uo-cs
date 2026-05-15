# File: est_tax.py
def taxable(income, exemptions, exempt_amount, deduct_amount):
    """Adjust gross income to taxable income by applying the
    standard deduction and exemptions.
    Args:
    income: gross income for which the tax is being computed
    exemptions: the number of personal exemptions
    exempt_amount: the dollar amount for each exemption
    deduct_amount: the dollar amount for the standard deduction
    Returns:
    TODO: Should this function return a value or print
    the result??
    >>> taxable(43000, 1, 12550, 12550)
    17900
    """
    # TODO: Write the function code here,
    # pay special attention to the return
    ti = income - (exemptions * exempt_amount) - deduct_amount
    return ti

#print(taxable(43000, 1, 12550, 12550))

def est_tax(income, exemptions):
    """Computes and prints an estimate for federal income tax.
    It assumes a simple standard deduction of $12500
    and a flat tax rate of 20%.
    Args:
    income: income for which the tax is being computed
    exemptions: number of exemptions claimed by the taxpayer
    Returns:
    The due tax for the given income and number of exemptions.
    >>> est_tax(43000, 1)
    3580.0
    """
    # Constants for the standard exemption and deduction (USD)
    STD_DEDUCT = 12550
    STD_EXEMPT = 12550
    # Constant for the flat tax rate of 20%
    TAX_RATE = .20
    # Calculate federal tax by adjusting reported income and
    # applying the tax rate
    tax_inc = taxable(income, exemptions, STD_EXEMPT, STD_DEDUCT)
    est_tax = tax_inc * TAX_RATE
    print('Estimated tax is:', est_tax)
    return est_tax

#print(est_tax(43000, 1))