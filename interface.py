import log, data_enter

def button_click():
    print('Введите "0" если ходите ввести данные')
    print('Введите "1" если хотите просмотреть данные')
    flag = int(input())
    if flag == 0:
        data_enter.indata()
        print('Введите "0" если ходите ввести данные')
        print('Введите "1" если хотите просмотреть данные')
    else:
         log.loger1() + '\n'
         log.loger2()
    