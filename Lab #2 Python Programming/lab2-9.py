day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_of_year(day, month, year):
  if is_leap(year): day_in_month[2] += 1
  return sum(day_in_month[:month]) + day


def day_in_year(year):
  return 366 if is_leap(year) else 365


def check_day(day, month, year):
  if is_leap(year): day_in_month[2] += 1
  if 1 <= month <= 12:
    if 1 <= day <= day_in_month[month]:
      return True
    else:
      return False
  else:
    return False


def date_diff(date1, date2):
  day1, month1, year1 = (int(i) for i in date1.split("-"))
  day2, month2, year2 = (int(i) for i in date2.split("-"))
  if check_day(day1, month1, year1) and check_day(day2, month2, year2):
    date1 = day_of_year(day1, month1, year1)
    date2 = day_of_year(day2, month2, year2)
  else:
    return -1
  if year1 == year2:
    return abs(date1 - date2)
  else:
    days = 1
    for year in range(year1, year2):
      days += day_in_year(year)
    days += date2 - date1
    return days
