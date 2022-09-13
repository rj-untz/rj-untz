salary = 92000
monthly_salary = salary/12
net_takehome_rate = .7136
net_monthly_salary = monthly_salary * net_takehome_rate

print(net_monthly_salary)

rent_future =  1995
home_expenses =  50+100+60
credit_bills =  550
loan_payments =  610+333+440+51+65

print(loan_payments+credit_bills)

def required_exp(rent_future, home_expenses, loan_payments, credit_bills):
   return rent_future+home_expenses+loan_payments+credit_bills

def discretionary(money_in, money_out):
   return money_in - money_out

ru_req_exp = required_exp(rent_future,home_expenses,loan_payments,credit_bills)
usable_balance = discretionary(net_monthly_salary, ru_req_exp)

food = 600
fuel = 150
general = 500
insurance = 54+150+25+17
phone = 190

non_essential_exp = food+fuel+general+insurance+phone

print(usable_balance)
print(non_essential_exp)
print(usable_balance - non_essential_exp)