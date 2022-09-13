def calc_nopat(ebit,tax_rate):
   return(ebit*(1.0-tax_rate))

def calc_fcf(nopat,end_toc,beg_toc):
   return(nopat-(end_toc-beg_toc))

def calc_roa(net_income, preferred_dividends, avg_total_assets):
   return((net_income-preferred_dividends)/avg_total_assets)

def calc_roe(net_income, preferred_dividends, avg_total_common_equity):
   return ((net_income-preferred_dividends)/avg_total_common_equity)

def calc_fullcapsales(actual_sales, actual_used_cap):
   return (actual_sales/actual_used_cap)

def calc_tvm_fv(pv,r,n):
   return (pv * ((1+r)**n))

def calc_tvm_ear(i,n):
   return ((1+i/n)**n)-1

investment_a = calc_tvm_ear(0.10,12)
investment_b = calc_tvm_ear(0.1015,2)

if investment_a > investment_b:
   print(f"investment_a is the better option with an effective annual return of {investment_a}")
else:
   print(f"investment_b is the better option with an effective annual return of {investment_b}")