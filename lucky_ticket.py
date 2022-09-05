""" Функция lucky_ticket"""

check_number=input()
def is_lucky_ticket(check_number):
    list_check_number=(list(map(int,check_number)))
    left_list_check_number=(list_check_number[0:int(len(list_check_number)/2)])
    right_list_check_number=(list_check_number[int(len(list_check_number) / 2):])
    test_check_number=bool(sum(left_list_check_number)==sum(right_list_check_number))
    print(test_check_number)
if len(check_number) % 2 ==0:
    is_lucky_ticket(check_number)
else:
    print('Введите корректный номер билета')