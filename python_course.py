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

# num = 89457645897791
#
# min=9
# max=0
# while num != 0:
#     last_digit = num % 10
#     if min>last_digit :
#         min=last_digit
#     if max<last_digit :
#        max=last_digit
#     num = num // 10
# print(min)
# print(max)


#
# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break
# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20
# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)
# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')


# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)
# m=int(input())
# n=int(input())
# if m<n:
#     for i in range(m, n+1):
#         print(i)
# if m>n:
#     for i in range(m, n-1, -1):
#         print(i)
# if m==n:
#     print(n)
# n=int(input())
# for i in range(1,n):
#     for j in range(3):
#         print(n, end=' ')
#     print()


# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)

# n = int(input())
# i=0
# summ=0
# while i < n:
#     num= int(input())
#     summ+=num
#     i+=1
# print(summ)
# x = [1, 2, 3]
# y = x
# y.append(4)
#
# s = "123"
# t = s
# t = t + "4"
#
# print(str(x) + " " + s)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)


# i = 1
# while i > 0:
#     num= int(input())
#     i +=1
#     if num < 10:
#             continue
#     if num > 100:
#             break
#     print(num)
#
# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)
#
# a = [1, 2, 3]
# b = a
# # значения списка b?
#
# a[1] = 10
# # значения списка b?
#
# b[0] = 20
# # значения списка a?
#
# a = [5, 6]
# # значения списка b?
# print(a)
# print(b)
# 
# num = int(input())
# last_digit1=num % 10
# has_seven = False  # сигнальная метка
# min = 9
# max = 0
# summ = 0
# count = 0
# proizv = 1
# while num != 0:
#     last_digit = num % 10
#     summ += last_digit
#     count += 1
#     summ += last_digit
#     proizv *= last_digit
#     num = num // 10
#     #
#     #
#     # if last_digit == 7:
#     #     has_seven = True
# sredn=summ/count
# first=last_digit
# summ_f_l=first+last_digit1
# print(summ, summ, proizv, sredn, first, summ_f_l, sep='\n')
# while num != 0:
#     last_digit = num % 10
#     if min > last_digit:
#         min = last_digit
#     if max < last_digit:
#         max = last_digit
#     num = num // 10

# n=int(input())
# for i in range(n):
# #     print('*' * 19, end ='\n' )
# m,p,n= int(input()), int(input()), int(input())
# for i in  range (n):
#     Day= m * (p / 100 + 1) ** i
#     print(i+1, Day)

# n=int(input())
# for i in range(n):
#     for j in range(9):
#         print((i+1), "+", (j+1), "=",(i+1) + (j+1) )
#     print()
# Решите уравнение в натуральных числах 28n + 30 k + 31 m = 36528n+30k+31m=365.
# total = 0
# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 11):
#             if 28*n+30*k+31*m == 365:
#                 total += 1
#                 print('n =', n, 'm =', m, "k", k)
# print('Общее количество натуральных решений =', total)


# m=int(input())
# n=int(input())
# for i in range(m+1,n, -1 ):
#     if i%2 !=0:
#         print(i)
# # if m<n:
#     for i in range(m, n+1):
#         print(i)
# if m>n:
#     for i in range(m, n-1, -1):
#         print(i)
# if m==n:
#     print(n)

num = int(input())
product = 1
while num != 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10
