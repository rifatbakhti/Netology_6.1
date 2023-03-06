from application.salary import salary_staff
from application.db.people import staff
import datetime


def get_salary():
    for key, value in salary_staff.items():
        print(key, value)

def get_staff():
    for person in staff:
        print(person)

def main():
    today = datetime.datetime.today()
    print(today.strftime('%d/%m/%Y'))

    option = input(f'Введите команду 1, чтобы получить сотрудников с ЗП и 2, чтобы получить список сотрудников: ')
    if option == "1":
        get_salary()
    elif option == "2":
        get_staff()

    else:
        print("Не работает!")

if __name__ == '__main__':
    main()