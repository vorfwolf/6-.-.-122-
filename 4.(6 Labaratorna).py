while True:
    while True:
        try:
            time = int(input('Введіть час, який горить світлофор: '))
            if(time>0):
                pass
            else:
                print('Час може бути заданим лише натуральним числом.')
                print()
                continue
            break
        except ValueError:
            print('Ви можете ввести лише ціле число.')
            print()

    if time > 0:
        if time % 6 == 1 or time % 6 == 2 or time % 6 == 3:
            print('Горить зелений сигнал світлофора')
        elif time % 6 == 4:
            print('Горить жовтий сигнал світлофора')
        elif time % 6 == 5 or time % 6 == 0:
            print('Горить червоний сигнал світлофора')
    else:
        print('Час має бути більше 0')
