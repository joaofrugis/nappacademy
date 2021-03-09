import datetime

birth_date = '14/01/95'

birth_date = datetime.datetime.strptime(birth_date, '%d/%m/%y')


age = (datetime.datetime.today() - birth_date) // datetime.timedelta(days=365.2425)

print(age)