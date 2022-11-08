for i in range(5):
    print('Řádek', i)

for i in range (12):
    if i%2 != 0:
        print(i)

for i in range(1, 5):
    print(i, 'na druhou je', i**2)

for radek in range(5):
    for sloupec in range(5):
        print('x ', end='')
    print()

for cislo in range(1, 5):
    for cinitel in range (1, 5):
        print(cislo * cinitel, ' ', end='')
    print()


for i in range(1, 5):
    print('x ' * i)

for i in range(1, 5):
    for j in range (0,i):
        print('x ', end='')
    print()

for i in range (0, 11, 2):
	print(i+1)