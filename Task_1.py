salary = lambda w, m, r = 0: w * m + r

work_hours = int(input('Введите кол-во часов, которое сотрудник работал: '))
money_per_hour = int(input('Введите ставку в час: '))
reward = input('Введите премию: ')

print(salary(work_hours, money_per_hour, int(reward) if reward != '' else 0))
