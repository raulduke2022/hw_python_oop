import datetime as dt


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
            # someday = dt.datetime.strptime(i.date, '%d.%m.%Y').date() #получаем дату без времени из record
            if i.date == today:
                sum += i.amount
        return sum

    def get_today_remained(self):
        wasted = Calculator.get_today_stats(self)
        remained = self.limit - wasted
        return remained

    def get_week_stats(self):
        sum = 0
        today = dt.datetime.now().date()
        offset_week = today - dt.timedelta(days=7) # получаем неделю назад дату
        for i in self.records:
            if offset_week <= i.date <= today:
                sum += i.amount
        return sum


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 86.0
    def get_today_stats(self):
        sum = super().get_today_stats()
        return f'Потрачено {sum} рублей'

    def get_today_cash_remained(self, currency):
        remained = super().get_today_remained()
        if currency == "usd":
            saldo = f'{(round(abs(remained)/self.USD_RATE,2))} USD'
        elif currency == "rub":
            saldo = f'{abs(remained)/1.0} руб'
        elif currency == "eur":
            saldo = f'{(round(abs(remained)/self.EURO_RATE,2))} Euro'
        else:
            raise ValueError('Нет такой валюты')
        if remained > 0:
            return f'На сегодня осталось {saldo}'
        elif remained == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {saldo}'

    def get_week_stats(self):
        return super().get_week_stats()


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
        return super().get_week_stats()



class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()


cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=11145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="21.02.2023"))

print(cash_calculator.get_today_cash_remained("rub"))
print(cash_calculator.get_week_stats())
# должно напечататься
# На сегодня осталось 555 руб

