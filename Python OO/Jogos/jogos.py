import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("escolha o seu jogo")
    print("*********************************")

    print('(1) forca (2) advinhação')

    jogo = int(input('qual você quer jogar?'))

    if(jogo == 1):
        print('jogando forca')
        forca.jogar()
    elif(jogo == 2):
        print('jogando advinhação')
        adivinhacao.jogar()

if(__name__ == '__main__'):
    escolhe_jogo()