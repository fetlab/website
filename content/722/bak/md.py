import calendar, itertools
from datetime import date, timedelta

start_date = date(2017, 1, 24)  #Should be a Tuesday
end_date   = date(2017, 5, 4)

adds = itertools.cycle((
	timedelta(2),  #Number of days from Tuesday to Thursday
	timedelta(5)   #Number of days from Thursday to Tuesday
))

cur = start_date
while cur <= end_date:
	with open(cur.isoformat() + '.md', 'w') as f:
		f.write('Title: {dow}, {mn} {d}\nDate: {date} 13:59\nHide: True\n\n'.format(
			dow=calendar.day_name[cur.weekday()],
			mn=calendar.month_name[cur.month],
			d=cur.day,
			date=cur.isoformat()))
	cur = cur + adds.next()
