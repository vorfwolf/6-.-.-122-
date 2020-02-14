from enum import Enum

while True:
    class converter(Enum):
        USD = 1
        EUR = 2
        CZK = 3
        PLN = 4

    USD = 24.58
    EUR = 26.9
    CZK = 1.08
    PLN = 6.31

    while True:
        try:
            x = float(input('Amount of money: '))
            p = input('Currency: ')
            break
        except ValueError:
            print('Кількість грошей може бути задана лише числом.')
    if x <= 0:
        print('Кількість грошей має бути більше 0')
    elif x > 0:
        if p == 'USD' or p == 'EUR' or p == 'CZK' or p == 'PLN':
            if (p == converter.USD.name):
                print(f'{x} USD = {USD*x:.2f} грн.')
            elif (p == converter.EUR.name):
                print(f'{x} EUR = {EUR*x:.2f} грн.')
            elif (p == converter.CZK.name):
                print(f'{x} CZK = {CZK*x:.f} грн.')
            elif (p == converter.PLN.name):
                print(f'{x} PLN = {PLN*x:.2f} грн.')
        else:
            print('Введіть лише одну з доступних валют')
