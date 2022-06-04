salary = 92000
monthly_salary = 5300

print(monthly_salary)

rent_future =  1795
home_expenses =  50+100+60
credit_bills =  200
loan_payments =  610+333+440+250

print(loan_payments+credit_bills)

def required_exp(rent_future, home_expenses, loan_payments, credit_bills):
   return rent_future+home_expenses+loan_payments+credit_bills

def discretionary(money_in, money_out):
   return money_in - money_out

total_expense = required_exp(rent_future,home_expenses,loan_payments,credit_bills)
usable_balance = discretionary(monthly_salary, total_expense)

food = 500
fuel = 150
general = 250
insurance = 54+150+25+17
phone = 180

non_essential_exp = food+fuel+general+insurance+phone

print(usable_balance)
print(non_essential_exp)
print(usable_balance - non_essential_exp)