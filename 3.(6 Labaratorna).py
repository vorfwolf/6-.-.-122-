from enum import Enum

while True:
    class month(Enum):
        January = 1
        February = 2
        March = 3
        April = 4
        May = 5
        June = 6
        July = 7
        August = 8
        September = 9
        October = 10
        November = 11
        December = 12


    class season(Enum):
        Winter = 1
        Spring = 2
        Summer = 3
        Autumn = 4

    while True:
        try:
            s = month [input ('Month: ')]
            break
        except KeyError:
            print('Ви можете задати лише один із 12 місяців (англійською мовою)')
            print()

    if (s == month.January or s == month.February or s == month.December):
        print(f'Пора року: {season.Winter.name}')
    elif (s == month.March or s == month.April or s == month.May):
        print(f'Пора року: {season.Spring.name}')
    elif (s == month.June or s == month.July or s == month.August):
        print(f'Пора року: {season.Summer.name}')
    elif (s == month.September or s == month.October or s == month.November):
        print(f'Пора року: {season.Autumn.name}')
