"""Расчет заработных плат, ФОТ, налогов и прочее"""
# Импорт всех key и values из списка Dictionaries
from Dictionaries import *

# Создание списка заработной платы всех сотрудников
list_salary = [values['salary'] for values in list_all_employees]

# Создание списка id всех сотрудников
list_id = [values['id'] for values in list_all_employees]

# Объявление переменных для расчета налогов, взносов и прочего
NDFL = 0.13 # Ставка НДФЛ
Soc_con = 0.3 #Суммарно все социлаьные взносы

def FOT(array):
    """ФОТ"""
    sum_salary=0
    for value in array:
        sum_salary+=float(value['salary'])
    return(sum_salary)

def NDFL_for_all_employees(array):
    """НДФЛ для всех сотрудников"""
    sum_salary_with_NDFL=0
    for value in array:
        sum_salary_with_NDFL+=float(value['salary']*NDFL)
    return(sum_salary_with_NDFL)

def Soc_con_for_all_employees(array):
    """Соцвзносы для всех сотрудников"""
    sum_salary_with_Soc_con=0
    for value in array:
        sum_salary_with_Soc_con+=float(value['salary']*Soc_con)
    return(sum_salary_with_Soc_con)

def max_salary(array):
    """Максимальная заработная плата"""
    max_salary_all = max(list_salary)
    return(max_salary_all)

def min_salary(array):
    """Минимальная заработная плата"""
    min_salary_all = min(list_salary)
    return(min_salary_all)

def avg_salary():
    """Средняя заработная плата"""
    sum_salary_all = sum(list_salary)
    avg_salary_all = (sum_salary_all/len(list_salary))
    return(avg_salary_all)

def count_employee(array):
    """Количество сотрудников"""
    count_all_employee = len(list_id)
    return(count_all_employee)
















