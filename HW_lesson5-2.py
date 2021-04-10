"""
Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года.
Склонением пренебречь (2000 года, 2010 года)
"""

date = '09.04.2021'

d, m, y = date.split('.')

day = {
    '01': 'First',
    '02': 'Second',
    '03': 'Third',
    '04': 'Forth',
    '05': 'Fifth',
    '06': 'Sixth',
    '07': 'Seventh',
    '08': 'Eighth',
    '09': 'Ninth',
    '10': 'Tenth',
    '11': 'Eleventh'
}

month = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

result = (f'{day[d]} {month[m]} {y} year')
print(result)
