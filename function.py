def is_leap_year(year):
	    if (year % 400 == 0) or (year % 100 !=0 and year % 4 == 0 ):
	    	 return Ture
	    else:
	         return False
a = int (input('please input year'))
print(is_leap_year(a))
	            
	