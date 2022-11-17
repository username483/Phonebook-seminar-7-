def csv_create():
    with open ('Phonebook1.csv', 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')