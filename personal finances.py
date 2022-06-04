old_salary = 79100
old_net_mo = 4632
pct_takehome = old_net_mo/(old_salary/12)
salary = 92000*1.1
projected_monthly = salary * pct_takehome / 12

rent_future =  1300
home_expenses =  231.56/2
credit_bills =  350
loan_payments =  1645-610

def required_exp(rent_future, home_expenses, loan_payments, credit_bills):
   return rent_future+home_expenses+loan_payments+credit_bills

def discretionary(money_in, money_out):
   return money_in - money_out

total_expense = required_exp(rent_future,home_expenses,loan_payments,credit_bills)
usable_balance = discretionary(projected_monthly, total_expense)

food = 500
fuel = 150
general = 350
insurance = 300
phone = 150

non_essential_exp = food+fuel+general+insurance+phone

print(usable_balance)
print(non_essential_exp)
print(usable_balance - non_essential_exp)