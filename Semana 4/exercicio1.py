import datetime

hoje = datetime.datetime.today()

birthdate = '14/01/95'

birthdate = datetime.datetime.strptime(birthdate, '%d/%m/%y')

total = hoje - birthdate
print(f"Dias de vida:{total.days}") 