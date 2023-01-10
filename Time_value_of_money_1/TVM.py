from math import exp

#Discrete model
def future_discrete_value(x, r, n):
	""" x = present value 
		r = annual interest rate
		n = number of periods interest held(years)
	"""
	return round(x*(1+r)**n, 2)


def present_discrete_value(x, r, n):
	""" x = future value 
		r = rate of return
		n = number of periods(years)
	"""
	return round(x*(1+r)**-n, 2)


# Continous model
def future_continous_value(x, r, t):
	""" x = present value 
		r = annual interest rate
		t = number of periods interest held(years)
	"""
	return round(x*exp(r*t), 2)


def present_continous_value(x, r, t):
	""" x = future value 
		r = rate of return
		t = number of periods(years)
	"""
	return round(x*exp(-r*t), 2)

if __name__ == '__main__':
	
	
	x = float(input("value of investment ($): "))
	r = float(input("Interest rate (%): "))/100
	n = int(input("Duration (years): "))
	print(f"Future value (discrete model) of x: %s {future_discrete_value(x, r, n)}")
	print(f"Present value (discrete model) of x: %s {present_discrete_value(x, r, n)}")
	print(f"Future value (continous model) of x: %s {future_continous_value(x, r, n)}")
	print(f"Present value (continous model) of x: %s {present_continous_value(x, r, n)}")
