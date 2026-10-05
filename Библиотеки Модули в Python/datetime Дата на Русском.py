import datetime

d = datetime.date.today()
ru = ""
m = d.month   # Получаем номер месяца

if m == 1:
    ru = "января"
elif m == 2:
    ru = "февраля"
elif m == 3:
    ru = "марта"
elif m == 4:
    ru = "апреля"
elif m == 5:
    ru = "мая"
elif m == 6:
    ru = "июня"
elif m == 7:
    ru = "июля"
elif m == 8:
    ru = "августа"
elif m == 9:
    ru = "сентября"
elif m == 10:
    ru = "октября"
elif m == 11:
    ru = "ноября"
elif m == 12:
    ru = "декабря"

print(f"Сегодня {d.day} {ru} {d.year} года.")

# Вывод: Сегодня 20 сентября 2026 года.