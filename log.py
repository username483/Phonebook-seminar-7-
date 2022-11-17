from data_enter import indata

input = indata()

def loger_csv():
    with open('Phonebook1.csv', 'a', encoding = 'utf-8') as data:
        data.write(f'{input[0]};{input[1]};{input[2]};{input[3]}\n')

def loger_txt():
    with open('Phonebook2.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {input[0]}\nИмя: {input[1]}\nНомер телефона: {input[2]}\nОписание: {input[3]}\n\n')
