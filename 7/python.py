# Дан файл f, содержащий различные даты. Каждая дата — это число, месяц и год. 
# Найти: а) год с наименьшим номером; б) все весенние даты; в) самую позднюю 
# дату.  

with open('data.txt') as f:
    dates = [d[:-1] for d in f.readlines()]

min_year = None

for d in dates:
    year = int(d.split(".")[2])
    if not min_year or year < min_year:
        min_year = year

print(f"a) {min_year}")

output = []
for d in dates:
    month = d.split(".")[1]
    if month in ["03", "04", "05"]:
        output.append(d)

print(f"b) {', '.join(output)}")

max_year = None
list_for_max_year = []

for d in dates:
    year = int(d.split(".")[2])
    if not max_year or year > max_year:
        max_year = year
    
for d in dates:
    if int(d.split(".")[2]) == max_year:
        list_for_max_year.append(d)

max_month = None
list_for_max_month = []

for d in list_for_max_year:
    month = int(d.split(".")[1])
    if not max_month or month > max_month:
        max_month = month
        
for d in list_for_max_year:
    if int(d.split(".")[1]) == max_month:
        list_for_max_month.append(d)

max_day = None
list_for_max_day = []
for d in list_for_max_month:
    day = int(d.split(".")[0])
    if not max_day or day > max_day:
        max_day = day
        
for d in list_for_max_month:
    if int(d.split(".")[0]) == max_day:
        list_for_max_day.append(d)

print(f"c) {list_for_max_day[0]}")
