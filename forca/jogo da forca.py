# jogo da forca

palavra_secreta = ['b','a','t','a','t','a']
letras_descobertas = []
passado = []
tentativas = 5
tentou = 0
ba = 0


for i in range(0, len(palavra_secreta)):
    letras_descobertas.append("*")

print('\n *** Jogo Da Forca ***\n')

acertou = False


while acertou == False:
    print(f'você tem {tentativas} tentativas\n')

    letra = input('digite uma letra: ')

    for i in range(0, len(passado)):
        if passado[i] == letra:
            print(f'\nvocê ja tentou a letra {letra}')
            ba = 1
            continue

    if ba != 1:
        passado.append(letra)

    contador = tentou

    if len(letra) > 1:
        print('Pilantra mal caráter apenas uma letra')
        tentativas -= 1
        continue
    else:
        letrinha = letra


    for i in range(0, len(letras_descobertas)):
        if letra == palavra_secreta[i]:
            letras_descobertas[i] = letra
            tentou += 1


        print(letras_descobertas[i])


    if contador == tentou:
        print(f'não tem a letra {letra} na palavra secreta')
        tentativas -= 1


    acertou = True

    for i in range(0, len(letras_descobertas)):
        if letras_descobertas[i] == '*':
            acertou = False


    if tentativas == 0:
        print(f'tentativas = {tentativas}\n\nvocê perdeu!!!')
        break


if tentativas != 0:
    print(f'Parabéns você ganhou o jogo a palavra era {palavra_secreta}')