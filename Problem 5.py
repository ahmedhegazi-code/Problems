year = int(input ('Enter a year'))
def is_leap(year):
    if year %4 != 0 :
        return False 
    elif year %100 != 0 :
        return True 
    elif year %100 !=0 : 
        return False 
    else :
        return False 

if is_leap(year):
    print(f"{year} Leap year ")
else:
    print(f"{year} Not aleap year ")
    