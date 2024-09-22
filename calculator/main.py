import calendar

def visocos(date):
    if calendar.isleap(int(date)) == True:
        print('The year is a leap year')
    else:
        print('The year is not a leap year')


def weak_day(year, month, day):
    if calendar.weekday(year, month, day) == 0:
        print('It is Monday')
    elif calendar.weekday(year, month, day) == 1:
        print('It is Tuesday')
    elif calendar.weekday(year, month, day) == 2:
        print('It is Wednesday')
    elif calendar.weekday(year, month, day) == 3:
        print('It is Thursday')
    elif calendar.weekday(year, month, day) == 4:
        print('It is Friday')
    elif calendar.weekday(year, month, day) == 5:
        print('It is Saturday')
    elif calendar.weekday(year, month, day) == 6:
        print('It is Sunday')

print('''What shall we do?
0 - Check if the year is a leap year
1 - Check the day of the week by date''')
choose = input('Enter your answer: ')

if choose == '0':
    date = input('Enter the year: ')
    if len(date) > 4:
        print('Invalid date!')
    else:
        visocos(date)
elif choose == '1':
    day = int(input('Enter the day: '))
    month = int(input('Enter the month: '))
    year = int(input('Enter the year: '))
    weak_day(year, month, day)
elif choose == '':
    print('Come again!')


# SECOND METHOD!
def visocos(chislo):
    if calendar.isleap(int(chislo)) == True:
        print('The year is a leap year')
    else:
        print('The year is not a leap year')


def weak_day(year, month, day):
    if calendar.weekday(year, month, day) == 0:
        print('It is Monday')
    elif calendar.weekday(year, month, day) == 1:
        print('It is Tuesday')
    elif calendar.weekday(year, month, day) == 2:
        print('It is Wednesday')
    elif calendar.weekday(year, month, day) == 3:
        print('It is Thursday')
    elif calendar.weekday(year, month, day) == 4:
        print('It is Friday')
    elif calendar.weekday(year, month, day) == 5:
        print('It is Saturday')
    elif calendar.weekday(year, month, day) == 6:
        print('It is Sunday')

print('''What shall we do?
0 - Check if the year is a leap year
1 - Check the day of the week by date''')
choose = input('Enter your answer: ')
chislo = input('Enter the date: ')

if len(chislo) < 5:
    visocos(chislo)
elif len(chislo) > 5 and len(chislo) < 11:
    if len(chislo) == 9:
        day = int(chislo[:2])
        month = int(chislo[2:5])
        year = int(chislo[4:])
        weak_day(year, month, day)
    elif len(chislo) == 10:
        day = int(chislo[:2])
        month = int(chislo[2:5])
        year = int(chislo[5:])
        weak_day(year, month, day)
    elif len(chislo) == 8:
        day = int(chislo[0])
        month = int(chislo[2:4])
        year = int(chislo[5:])
        weak_day(year, month, day)
else:
    print('Come again!')
