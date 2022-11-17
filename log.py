def loger1(name, last_name, phone_number, description):
    with open('file1.txt', 'a') as data:
        name = name + '\n'
        last_name = last_name + '\n'
        phone_number = phone_number + '\n'
        description = description + '\n'
        data.write(name, last_name, phone_number, description)

def loger2(name, last_name, phone_number, description):
    with open('file2.txt', 'a') as data:
        name = name + ' ;'
        last_name = last_name + ' ;'
        phone_number = phone_number + ' ;'
        description = description + ' ;'
        data.write(name, last_name, phone_number, description)
