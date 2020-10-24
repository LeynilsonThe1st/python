print("*************************************")
print("*****      Jogo da Forca         ****")
print("*************************************")

palavra_secreta = "Geladeira".upper()
letras_acertadas=["_", "_", "_", "_", "_", "_", "_", "_", "_"]

acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while (not enforcou and not acertou):

    chute = str(input("Qual letra? ")).upper()
    posicao = 0
    if chute in palavra_secreta:
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
    else:
        erros += 1

    acertou = "_" not in letras_acertadas
    enforcou = erros == 6
    print(letras_acertadas)
    print(erros)

if acertou :
    print("Voce ganhou!!")
else:
    print("Voce perdeu!!")

print("Fim do jogo")
