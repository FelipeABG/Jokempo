import random 
import pwinput


def VitoriaPC1():
    global PlacarP1
    PlacarP1 += 1
    print(f'''        ---------------JoKenPo---------------
            Computador 1 escolheu {Player1}.
            Computador 2 escolheu {Player2}.
            logo, Computador 1 venceu!
            Placar: Computador 1 - {PlacarP1} x {PlacarP2} - Computador 2''')
def VitoriaPC2():
    global PlacarP2
    PlacarP2 += 1
    print(f'''        ---------------JoKenPo---------------
            Computador 1 escolheu {Player1}.
            Computador 2 escolheu {Player2}.
            logo, Computador 2 venceu!
            Placar: Computador 1 - {PlacarP1} x {PlacarP2} - Computador 2''')
def VitoriaPC():
    global PlacarP2
    PlacarP2 += 1
    print(f'''        ---------------JoKenPo---------------
            Jogador 1 escolheu {Player1}.
            Computador escolheu {Player2}.
            logo, Computador venceu!
            Placar: Jogador 1 - {PlacarP1} x {PlacarP2} - Computador''')
def VitoriaP1():
    global PlacarP1
    PlacarP1 += 1
    print(f'''        ---------------JoKenPo---------------
            Jogador 1 escolheu {Player1}.
            Jogador 2 escolheu {Player2}.
            logo, Jogador 1 venceu!
            Placar: Jogador 1 - {PlacarP1} x {PlacarP2} - Jogador 2''')
def VitoriaP2():
    global PlacarP2
    PlacarP2 += 1
    print(f'''        ---------------JoKenPo---------------
            Jogador 1 escolheu {Player1}.
            Jogador 2 escolheu {Player2}.
            logo, Jogador 2 venceu!
            Placar: Jogador 1 - {PlacarP1} x {PlacarP2} - Jogador 2''')
def empate():
    print(f'''        ---------------JoKenPo---------------
            Jogador 1 escolheu {Player1}.
            Jogador 2 escolheu {Player2}.
            logo, houve empate!
            Placar: Jogador 1 - {PlacarP1} x {PlacarP2} - Jogador 2''')
def erro():
    print('''        ---------------JoKenPo---------------
            Opção inválida!''')

PlacarP1 = 0
PlacarP2= 0
menu = 0

jogo = ['Pedra', 'Papel', 'Tesoura']
Continuar = ['S', 'N']

while menu <1 or menu >3:
    menu = int(input('''        ---------------JoKenPo---------------
            Este jogo oferece 3 modos de jogo:
            1 - Jogador vs jogador
            2 - Jogador vs computador
            3 - Computador vs computador
            Selecione qual modo deseja jogar: '''))

if menu == 1:
    while True:
        while True:
            Player1 = pwinput.pwinput('''        ---------------JoKenPo---------------
            Entre as opções:
            -Pedra
            -Papel
            -Tesoura
            Jogador 1, escolha sua jogada: ''').capitalize()
            Player2 = pwinput.pwinput('''        ---------------JoKenPo---------------
            Entre as opções:
            -Pedra
            -Papel
            -Tesoura
            Jogador 2, escolha sua jogada: ''').capitalize()
            if Player1 in jogo and Player2 in jogo:
                break
            else:
                erro()
        if Player1 == 'Pedra' and Player2 == 'Tesoura':
            VitoriaP1()
        elif Player1 == 'Pedra' and Player2 == 'Papel':
            VitoriaP2()
        elif Player1 == 'Papel' and Player2 == 'Pedra':
            VitoriaP1()
        elif Player1 == 'Papel' and Player2 == 'Tesoura':
            VitoriaP2()
        elif Player1 == 'Tesoura' and Player2 == 'Papel':
            VitoriaP1()
        elif Player1 == 'Tesoura' and Player2 == 'Pedra':
            VitoriaP2()
        elif Player1 == Player2:
            empate()
        while True:
            ContinuarJogando = input('''        ---------------JoKenPo---------------
            Deseja continuar jogando [S/N]? ''').capitalize()
            if ContinuarJogando in Continuar:
                break
            else:
                erro()
        if ContinuarJogando == 'N':
            print('''        ---------------JoKenPo---------------
                Obrigado por jogar!''')
            break 
if menu == 2:
    while True:
        while True:
            Player1 = pwinput.pwinput('''        ---------------JoKenPo---------------
            Entre as opções:
            -Pedra
            -Papel
            -Tesoura
            Jogador 1, escolha sua jogada: ''').capitalize()
            if Player1 in jogo:
                break
            else:
                erro()
        Player2 = random.choice(jogo)
        if Player1 == 'Pedra' and Player2 == 'Tesoura':
            VitoriaP1()
        elif Player1 == 'Pedra' and Player2 == 'Papel':
            VitoriaPC()
        elif Player1 == 'Papel' and Player2 == 'Pedra':
            VitoriaP1()
        elif Player1 == 'Papel' and Player2 == 'Tesoura':
            VitoriaPC()
        elif Player1 == 'Tesoura' and Player2 == 'Papel':
            VitoriaP1()
        elif Player1 == 'Tesoura' and Player2 == 'Pedra':
            VitoriaPC()
        else:
            empate()
        while True:
            ContinuarJogando = input('''        ---------------JoKenPo---------------
            Deseja continuar jogando [S/N]? ''').capitalize()
            if ContinuarJogando in Continuar:
                break
            else:
                erro()
        if ContinuarJogando == 'N':
            print('''        ---------------JoKenPo---------------
                Obrigado por jogar!''')
            break
if menu == 3:
    while True:
        Player1 = random.choice(jogo)
        Player2 = random.choice(jogo)
        if Player1 == 'Pedra' and Player2 == 'Tesoura':
            VitoriaPC1()
        elif Player1 == 'Pedra' and Player2 == 'Papel':
            VitoriaPC2()
        elif Player1 == 'Papel' and Player2 == 'Pedra':
            VitoriaPC1()
        elif Player1 == 'Papel' and Player2 == 'Tesoura':
            VitoriaPC2()
        elif Player1 == 'Tesoura' and Player2 == 'Papel':
            VitoriaPC1()
        elif Player1 == 'Tesoura' and Player2 == 'Pedra':
            VitoriaPC2()
        else:
            empate()
        while True:
            ContinuarJogando = input('''        ---------------JoKenPo---------------
            Deseja continuar jogando [S/N]? ''').capitalize()
            if ContinuarJogando in Continuar:
                break
            else:
                erro()
        if ContinuarJogando == 'N':
            print('''        ---------------JoKenPo---------------
                Obrigado por jogar!''')
            break