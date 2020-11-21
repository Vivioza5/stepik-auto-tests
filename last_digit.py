num=int(input())
sum1=0
sum2=0
num1=[]
num2=[]
for i in range(3):
    last_digit = num % 10
    num = num // 10
    num1.append(last_digit)
    sum1+=last_digit
# for i in range(3):
#     last_digit = num % 10
#     num = num // 10
#     num2.append(last_digit)
#     sum2+=num2[i]
a=max(num1)
b=min(num1)

c=sum1-(a+b)
if a-b==c:
    print('Число интересное')
else:
    print('Число не интересное')
print(sum1)
print(a, b, c)

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
