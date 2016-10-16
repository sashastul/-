# -*- coding: utf-8 -*-
chislo = int(input("Введите число \n"))
olsihc = (chislo/100) + (chislo/10 - (chislo/100)*10)*10 + (chislo - (chislo/100)*100 - (chislo/10 - (chislo/100)*10)*10)*100
print(olsihc)