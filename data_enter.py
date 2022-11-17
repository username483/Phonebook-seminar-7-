def indata():
    data = []
    name = input(print('Введите имя: '))
    data.append(name)
    last_name =  input(print('Введите фамилию: '))
    data.append(last_name)
    phone_number = input(print('Введите телефон: '))
    data.append(phone_number)
    description = input(print('Введите описание: '))
    data.append(description)

    return data