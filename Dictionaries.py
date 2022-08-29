# Создание списка со словарями
users = [
    {'id': '1', 'name': 'Vitalui', 'age': '27', 'salary': '375000.50'},
    {'id': '2', 'name': 'Xenia', 'age': "25", 'salary': '325000'},
    {'id': '3', 'name': 'Max', 'age': "26", 'salary': '15500050'},
    {'id': '4', 'name': 'Mike', 'age': "29", 'salary': '150000'},
    {'id': '5', 'name': 'Liza', 'age': '25', 'salary': '100000'}
]
# Создание нового списка с заработными платами сотрудником
a = []
for i in users:
    i['salary']= float(i['salary'])
    a.append(i['salary'])

# Проверка списка
print(sum(a))

