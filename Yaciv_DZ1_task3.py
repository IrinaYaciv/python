# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на
# экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

numbers = input("Введите число от 1 до 100:  ")
exceptions = [11, 12, 13, 14]
for num in range(100):
    num = num + 1
    if num in exceptions:
        print(num, "процентов")
    elif num % 10 == 1:
        print(num, "процент")
    elif num % 10 > 1 and num % 10 < 5:
        print(num, "процента")
    else:
        print(num, "процентов")

