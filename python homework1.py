# -*- coding: utf-8 -*-
print("Сколько Вам лет?")
x = int(input())
if 0 <= x < 18:
	print("Вы юноша")
elif 18 <= x < 45:
	print("Вы молодой")
elif 45 <= x < 60:
	print("Вы среднего возраста")
elif 60 <= x < 75:
	print("Вы пожилой")
elif 75 <= x < 90:
	print("Вы старец")
elif 90 <= x:
	print("Вы долгожитель")
else:
	print("Неправильно введен возраст")