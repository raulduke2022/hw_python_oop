import datetime as dt
USD_RATE = 60
EURO_RATE = 90

class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        sum = 0
        today = dt.datetime.now().date() #получаем сегодняшний день без времени
        for i in self.records:
            someday = dt.datetime.strptime(i.date, '%d.%m.%Y').date() #получаем дату без времени из record
            if someday == today:
                sum += i.amount
        return sum

    def get_today_remained(self):
        wasted = Calculator.get_today_stats(self)
        remained = self.limit - wasted
        return remained

    def get_week_stats(self):
        sum = 0
        today = dt.datetime.now().date()  # получаем сегодняшний день без времени
        for i in self.records:
            someday = dt.datetime.strptime(i.date, '%d.%m.%Y').date()  # получаем дату без времени из record
            if (someday - today).days <= 7 and (someday - today).days >= 0:
                sum += i.amount
        return sum


class CashCalculator(Calculator):

    def get_today_stats(self):
        sum = super().get_today_stats()
        return f'Потрачено {sum} рублей'

    def get_today_cash_remained(self, currency):
        remained = super().get_today_remained()
        if currency == "usd":
            saldo = f'{round(remained/USD_RATE,2)} USD'
        elif currency == "rub":
            saldo = f'{remained} руб'
        elif currency == "eur":
            saldo = f'{round(remained/EURO_RATE,2)} Euro'
        if remained > 0:
            return f'На сегодня осталось {saldo}'
        elif remained == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {saldo}'

    def get_week_stats(self):
        sum = super().get_week_stats()
        return f'За неделю было потрачено {sum} рублей'


class CaloriesCalculator(Calculator):

    def get_today_stats(self):
        sum = super().get_today_stats()
        return f'Съедено {sum} калорий'


    def get_calories_remained(self):
        remained = super().get_today_remained()
        if remained > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remained} кКал'
        return f'Хватит есть!'


    def get_week_stats(self):
        sum = super().get_week_stats()
        return f'За неделю было потрачено {sum} калорий'


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now().strftime("%d.%m.%Y")):
        self.amount = amount
        self.comment = comment
        self.date = date


# cash = CashCalculator(1000)
#
# # для CashCalculator
# r1 = Record(amount=145, comment="Безудержный шопинг", date="16.02.2023")
# r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="15.02.2023")
# r3 = Record(amount=1200, comment="Катание на такси", date="15.02.2023")
#
# cash.add_record(r1)
# cash.add_record(r2)
# cash.add_record(r3)
# print(cash.get_today_stats())
# print(cash.get_today_remained('usd'))
# print(cash.get_week_stats())
#
#
# # print(cash.get_today_remained())
#
# calory = CaloriesCalculator(1000)
#
# # для CaloriesCalculator
# r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="16.02.2023")
# r5 = Record(amount=84, comment="Йогурт.", date="16.02.2023")
# r6 = Record(amount=1140, comment="Баночка чипсов.", date="15.02.2023")
#
# print()
# calory.add_record(r4)
# calory.add_record(r5)
# calory.add_record(r6)
# print(calory.get_today_stats())
# print(calory.get_today_remained())
# print(calory.get_week_stats())
#


# cash_calculator = CashCalculator(1000)
#
# # дата в параметрах не указана,
# # так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
# cash_calculator.add_record(Record(amount=145, comment="кофе"))
# # и к этой записи тоже дата должна добавиться автоматически
# cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# # а тут пользователь указал дату, сохраняем её
# cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
#
# print(cash_calculator.get_today_cash_remained("rub"))
# # должно напечататься
# # На сегодня осталось 555 руб


if __name__ == "__main__":
    limit = 1000
    cash_calculator = CashCalculator(limit)
    calories_calculator = CaloriesCalculator(limit)

    # записи для денег
    r1 = Record(amount=145, comment='кофе')
    r2 = Record(amount=300, comment='Серёге за обед')
    r3 = Record(
        amount=3000,
        comment='Бар на Танин день рождения',
        date='08.11.2022')

    # записи для калорий
    r4 = Record(
        amount=118,
        comment='Кусок тортика. И ещё один.')
    r5 = Record(
        amount=84,
        comment='Йогурт.')
    r6 = Record(
        amount=1140,
        comment='Баночка чипсов.',
        date='24.02.2019')

    cash_calculator.add_record(r1)
    cash_calculator.add_record(r2)
    cash_calculator.add_record(r3)

    calories_calculator.add_record(r4)
    calories_calculator.add_record(r5)
    calories_calculator.add_record(r6)

    # вывод результатов
    print(cash_calculator.get_today_cash_remained('rub'))
    print(calories_calculator.get_calories_remained())