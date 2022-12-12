import random
ganaste=False
opc=['piedra','papel','tijera']
juego=0
while ganaste!=True:
    pc= random.randint(0,2)
    juego=int(input('''que prefieres elegir 
1.Piedra 
2.papel
3. tijera
4. salir'''))
    if juego==4:
        print('fin del juego')
        break
    elif juego==1 and opc[pc]=='tijera' or juego==2 and opc[pc]=='piedra' or juego==3 and opc[pc]=='papel':
        print(f'ganaste, oponente saco: {opc[pc]}') 
        ganaste=True
    elif juego==pc:
        print(f'empate, oponente saco: {opc[pc]}')
        ganaste==False
    else:
        print(f'perdiste, oponente saco: {opc[pc]}')
        ganaste=False