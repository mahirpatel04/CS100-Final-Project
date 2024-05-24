import calendar
from datetime import date, timedelta


megalst = []
td = date.today()
for i in range(100):
    td += timedelta(days=1)
    megalst.append(td)
    
    


    
    
c = calendar.Calendar()

yr = 2024
mth = 5
day = 17
lst30Days = [4, 6, 9, 11]
lst31Days = [1, 3, 5, 7, 8, 10, 12]

'''

for i in range(365):
    if mth in lst30Days:
        if day + 1 > 30:
            mth += 1
            day = 0
            print(f"{mth}/{day + i}/{yr}")
    
    
    
    

for month in range(12):
    if month in lst30Days:
        for i in range(365):
            if mth in lst30Days:
                if day + 1 > 30:
                    mth += 1
                    day = 0
                    print(f"{mth}/{day + i}/{yr}")
    elif month in lst31Days:
        pass
    
    elif month == 2:
        if yr % 4 == 0:
            pass
            # this is leap yr
            
        else:
            # this is normal yr
            pass'''