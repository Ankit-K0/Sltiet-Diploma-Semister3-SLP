#to print current year , month and date


#import date from datetime module 
from datetime import date

#declare a variable to get current year , month and date
today = date.today()

#print year
print("current year",today.year)

#print month    
print("current month",today.month)

#print date
print("current day",today.day)
