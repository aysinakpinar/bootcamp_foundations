def calculate_tax_for_the_shire(grossPay):
    return grossPay * 0.2

def calculate_tax_for_mirkwood(grossPay):
    return grossPay * 0.9

def calculate_tax_for_mordor(grossPay):
    return grossPay * 0.9 + 500

def calculate_tax_for_zero(grossPay):
    return 0
def calculate_fixed_rate_tax(grossPay):
    return 1000
def report_pay(gross_pay, calculate_tax):
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax
    return f"Your gross pay was {gross_pay}, minus {tax} makes your net pay {net_pay}"

print("Frodos's Pay:")
print(report_pay(5000.0, calculate_tax_for_the_shire))
print("zero tax calculated")
print(report_pay(2000.0, calculate_tax_for_zero))
print("fixed rate tax calculate")
print(report_pay(10000, calculate_fixed_rate_tax))
