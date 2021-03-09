import datetime

hoje = datetime.datetime.today()

add = datetime.timedelta(days=17)

final_date = hoje + add

print(final_date)