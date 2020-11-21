
# num=int(input())
# sum1=0
# sum2=0
# num1=[]
# num2=[]
# for i in range(3):
#     last_digit = num % 10
#     num = num // 10
#     num1.append(last_digit)
#     sum1+=last_digit
# # for i in range(3):
# #     last_digit = num % 10
# #     num = num // 10
# #     num2.append(last_digit)
# #     sum2+=num2[i]
# a=max(num1)
# b=min(num1)
#
# c=sum1-(a+b)
# if a-b==c:
#     print('Число интересное')
# else:
#     print('Число не интересное')
# print(sum1)
# print(a, b, c)

# for i in range(3):
#     last_digit = num % 10
#     num = num // 10
#     sum2+=last_digit
# if sum1==sum2:
#     print('Счастливый')
# else:
#     print('Обычный')
#
# print(num1)
# print(num2)

# Если хочется получить список именно из чисел, то можно затем элементы списка по одному преобразовать в числа:
# a = input().split()
# for i in range(len(a)):
#     a[i] = int(a[i])
# part2
# a = [int(s) for s in input().split()]

#
# a1,a2,a3,a4,a5=float(input()),float(input()),float(input()),float(input()),float(input())
# summ=abs(a1)+abs(a2)+abs(a3)+abs(a4)+abs(a5)
# print(summ)


# p1,p2,q1,q2=int(input()),int(input()),int(input()),int(input())
# manh=abs(p1-q1)+abs(p2-q2)
# print(manh)

# n= int(input())
# fact=1
# for i in range(n):
#     fact*=i+1
# print(fact)
# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
# proizv=1
# for i in  range(10):
#     i=int(input())
#     if i!=0:
#         proizv*=i
# print(proizv)

# Сумма делителей

# n= int(input())
# summ=0
#
# for (i) in  range(1, n+1):
#     if n%i==0:
#         summ+=i
# print(summ)

n= int(input())
summ=0
for (i) in  range(1, n+1):
    if i%2==0:
        summ-=i
    else:
        summ+=i
print(summ)
