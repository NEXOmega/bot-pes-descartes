day=int(input("Jours : "))
month=int(input("Mois : "))
year=int(input("Année : "))

print(f"Aujourd'hui on est le {day} {month} {year}")
def get_next_day(day, month, year):
    if(day >= 31 and (month in [1,3,5,7,8,10,12])):
        update_month_year(1, month, year)

    elif(day >= 30 and (month in [4,6,9,11])):
        update_month_year(1, month+1, year)

    elif(day == 29 and year%4==0):
        update_month_year(1, month+1, year)

    elif (day == 28):
        update_month_year(1, month+1, year)
    else:
        update_month_year(day+1, month, year)

def update_month_year(day, month, year):
    if(month >= 12):
        month=1
        year +=1
    print(f"Demain nous seront le {day} {month} {year}")

get_next_day(day, month, year)