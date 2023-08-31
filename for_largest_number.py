def teste():
    num = float(input("Digite um nº: "))
    return num

last = 0

for _ in range(5):
    num = teste()
    if num > last:
        last = num

print("Maior número:",last)