from datetime import date, datetime

class MyCalendar:
	def __init__(self, *args):
		self.datas = []
		self.add_holiday(*args)

	def add_holiday(self, *args):
		for data in args:
			d = self.valida_data(data)
			if d:
				self.datas.append(d)
		self.datas = list(set(self.datas))

	def check_holiday(self, data) -> bool:
		return self.valida_data(data) in self.datas

	def valida_data(self, data):
		if isinstance(data, date):
			return data
		elif isinstance(data, str):
			try:
				return datetime.strptime(data, '%d/%m/%Y').date()
			except:
				return None