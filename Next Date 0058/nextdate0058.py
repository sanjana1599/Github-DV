mon31=[1,3,5,7,8,10,12]
mon30=[4,6,9,11]
print("Enter date, month and year separated by spaces")
inp=input()
s=inp.split()
date=int(s[0])
month=int(s[1])
year=int(s[2])

def leap(y):#parameter is year
    if y % 100 == 0 and y % 400 == 0: #checking for century leap years eg 2000
        return y #returns y if it is leap year
    elif y % 100 != 0 and y % 4 == 0: #making sure years like 1900 dont print as leap year bc its divisible by 4 but not by 400
        return y
    else:
        return 0 #for non leap years

if date<1 or date>31 or month<1 or month>12:
    print("Wrong Input")

else: #if no basic wrong input, move ahead
    if month==12 and date==31:
        year=year+1
        print("1 "+"1 "+str(year))

    elif date>=28 and month==2:
        check=leap(year)
        if check == 0: #not a leap year
            if date>28: #29,20,31 feb
                print("Wrong Input:Date")
            else: #28 feb non leap year
                print("1 "+"3 "+str(year))
        else: #if its a leap year
            if date==28:
                date=date+1 #29th feb leap year
                print(str(date)+" "+str(month)+" "+str(year))
            else: #29th feb
                print("1 "+"3 "+str(year))

    elif date==30:
        if month in mon30: #months with 30 days
            month=month+1
            print("1 "+str(month)+" "+str(year))
        else:
            date=date+1
            print(str(date)+" "+str(month)+" "+str(year))

    elif date==31:
        if month in mon31: #months with 31 days 
            month=month+1
            print("1 "+str(month)+" "+str(year))
        else:
            print("Wrong Input:Date")

    else:
        date=date+1
        print(str(date)+" "+str(month)+" "+str(year))
