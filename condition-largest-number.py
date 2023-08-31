num1 = input("1º num: ")
num2 = input("2º num: ")
num3 = input("3º num: ")
num = num1

if num2 > num1:
    num = num2
elif num3> num1:
    num = num3

print("Maior num:", num)