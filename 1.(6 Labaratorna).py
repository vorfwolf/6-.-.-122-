import datetime

days = range(1, 32)
mounths = range(1, 13)
years = range(1901, 2021)

while True:
    try:
        d, m, y = int(input('day:')), \
                  int(input('mounth:')), \
                  int(input('year:'))
        if d>0 and m>0 and y>0:
            pass
        else:
            print('Час може бути заданим лише натуральним числом')
            print()
            continue
        break
    except ValueError:
        print('Ви можете ввести лише ціле число')
        print()
        continue

if d in days and m in mounths and y in years:
    date = datetime.datetime(y, m, d)
    newdate = date - datetime.timedelta(days=1)
    print('Дата попереднього дня {:%Y.%m.%d}'.format(newdate))
    newdate1 = date + datetime.timedelta(days=1)
    print('Дата наступного дня {:%Y.%m.%d}'.format(newdate1))
else:
    print('Заданий день, місяць, рік не відповідають умовам')
