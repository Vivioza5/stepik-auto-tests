# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)


# num = int(input())
# has_seven = False  # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')
# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

num = 8945

min=9
max=0
while num != 0:
    last_digit = num % 10
    if min>last_digit :
        min=last_digit
    if max<last_digit :
       max=last_digit
    num = num // 10
print(min)
print(max)



