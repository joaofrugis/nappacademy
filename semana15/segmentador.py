def open_csv(file):
	for linha in open(file):
		yield linha

file = open_csv("./projeto/candidatura.csv")

headers = next(file)
cand_year = {}

while True:
	try:
		cand = next(file)
	except StopIteration:
		del file
		break

	year = cand.split(",")[0]
	if year not in cand_year:
		cand_year[year] = []
	cand_year[year].append(cand)


for year,cand in cand_year.items():
	csv_data = "".join(cand)
	with open('projeto/eleicao_{}.csv'.format(year), "w") as csv:
		csv.write(headers + csv_data)