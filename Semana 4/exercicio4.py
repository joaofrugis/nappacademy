import datetime

hoje = datetime.datetime.today()

birthdate = '08/07/2014'

birthdate = datetime.datetime.strptime(birthdate, '%d/%m/%Y')

total = hoje - birthdate
print("A data do jogo foi 08/07/2014")
print(f"Ja se passaram {total.days} dias")