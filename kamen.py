from random import randrange




tah_pocitace = randrange(0, 3)

# 0== kámen, 1== nůžky, 2 == Papír

tah_cloveka = input('Kámen, nůžky nebo papír?')

if tah_pocitace == 0: 
    if tah_cloveka == 'kámen' or tah_cloveka == 'kamen' or tah_cloveka == 'Kámen'or tah_cloveka == 'Kamen':
        print('Plichta')
    elif tah_cloveka == 'nuzky' or tah_cloveka == 'nůžky' or tah_cloveka == 'Nůžky' or tah_cloveka == 'nuzky':
        print('Prohral jsi')
    elif tah_cloveka == 'papír' or tah_cloveka == 'papir' or tah_cloveka == 'Papir' or tah_cloveka == 'papír':
        print('Vyhrál jsi')
    else: 
        print('Neumíš hrát hru?')
elif tah_pocitace == 1:
    if tah_cloveka == 'kámen' or tah_cloveka == 'kamen' or tah_cloveka == 'Kámen'or tah_cloveka == 'Kamen':
        print('Vyhrál jsi')
    elif tah_cloveka == 'nuzky' or tah_cloveka == 'nůžky' or tah_cloveka == 'Nůžky' or tah_cloveka == 'nuzky':
        print('Plichta')
    elif tah_cloveka == 'papír' or tah_cloveka == 'papir' or tah_cloveka == 'Papir' or tah_cloveka == 'papír':
        print('Prohrál jsi')
    else: 
        print('Neumíš hrát hru?')
else: 
    if tah_cloveka == 'kámen' or tah_cloveka == 'kamen' or tah_cloveka == 'Kámen'or tah_cloveka == 'Kamen':
        print('Prohrál jsi')
    elif tah_cloveka == 'nuzky' or tah_cloveka == 'nůžky' or tah_cloveka == 'Nůžky' or tah_cloveka == 'nuzky':
        print('Vyhral jsi')
    elif tah_cloveka == 'papír' or tah_cloveka == 'papir' or tah_cloveka == 'Papir' or tah_cloveka == 'papír':
        print('Plichta')
    else: 
        print('Neumíš hrát hru?')

print('Děkujeme že hrajete s námi')