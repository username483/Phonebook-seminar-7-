from os.path import exists
from csv_creation import csv_create
from log import loger_csv
from log import loger_txt

path = 'Phonebook1.csv'
valid = exists(path)
if not valid:
    csv_create()


def main():
    loger_csv()
    loger_txt()


if __name__ == '__main__':
    main()

