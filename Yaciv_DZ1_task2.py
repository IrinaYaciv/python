# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b, не создавая новый список.

numbers = list((range(1, 1000, 2)))
numbers_amount = []
seventeen_lst = []
seventeen_lst_amount = []
for idx in range(len(numbers)):
    numbers[idx] = numbers[idx] ** 3
    first_num = numbers[idx] // 100000000
    second_num = (numbers[idx] % 100000000) // 10000000
    third_num = ((numbers[idx] % 100000000) % 10000000) // 1000000
    four_num = (((numbers[idx] % 100000000) % 10000000) % 1000000) // 100000
    five_num = ((((numbers[idx] % 100000000) % 10000000) % 1000000) % 100000) // 10000
    six_num = (((((numbers[idx] % 100000000) % 10000000) % 1000000) % 100000) % 10000) // 1000
    seven_num = ((((((numbers[idx] % 100000000) % 10000000) % 1000000) % 100000) % 10000) % 1000) // 100
    eighth_num = (((((((numbers[idx] % 100000000) % 10000000) % 1000000) % 100000) % 10000) % 1000) % 100) // 10
    nine_num = ((((((((numbers[idx] % 100000000) % 10000000) % 1000000) % 100000) % 10000) % 1000) % 100) % 10)
    idx = idx + 1
    A = [first_num, second_num, third_num, four_num, five_num, six_num, seven_num, eighth_num, nine_num]
    #print(A)
    #print(sum(A))
    if sum(A) % 7 == 0:
        numbers_amount.append(sum(A))
print(numbers)
print(sum(numbers_amount))

#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.
for value in numbers:
    seventeen_lst.append(value + 17)
for idx in range(len(seventeen_lst)):
    first_num = seventeen_lst[idx] // 100000000
    second_num = (seventeen_lst[idx] % 100000000) // 10000000
    third_num = ((seventeen_lst[idx] % 100000000) % 10000000) // 1000000
    four_num = (((seventeen_lst[idx] % 100000000) % 10000000) % 1000000) // 100000
    five_num = ((((seventeen_lst[idx] % 100000000) % 10000000) % 1000000) % 100000) // 10000
    six_num = (((((seventeen_lst[idx] % 100000000) % 10000000) % 1000000) % 100000) % 10000) // 1000
    seven_num = ((((((seventeen_lst[idx] % 100000000) % 10000000) % 1000000) % 100000) % 10000) % 1000) // 100
    eighth_num = (((((((seventeen_lst[idx] % 100000000) % 10000000) % 1000000) % 100000) % 10000) % 1000) % 100) // 10
    nine_num = ((((((((seventeen_lst[idx] % 100000000) % 10000000) % 1000000) % 100000) % 10000) % 1000) % 100) % 10)
    idx = idx + 1
    A = [first_num, second_num, third_num, four_num, five_num, six_num, seven_num, eighth_num, nine_num]
    #print(A)
    #print(sum(A))
    if sum(A) % 7 == 0:
        seventeen_lst_amount.append(sum(A))
print(seventeen_lst)
print(sum(seventeen_lst_amount))

