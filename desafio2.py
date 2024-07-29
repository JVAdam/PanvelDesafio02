## Variável global
alfabeto = "abcdefghijklmnopqrstuvwyz"

## Funções
def encript(mensagem, posicoes):
    msg = ""
    for i in mensagem:
        if i in alfabeto:
            i_indice = alfabeto.index(i)
            msg += alfabeto[(i_indice + posicoes) % len(alfabeto)]
        else:
            msg += i

    return msg

def decript(mensagem, posicoes):
    msg = ""

    for i in mensagem:
        if i in alfabeto:
            i_indice = alfabeto.index(i)
            msg += alfabeto[(i_indice - posicoes) % len(alfabeto)]
        else:
            msg += i

    return msg

## ------------------------------------------
## Main
print("===== CRIPTOGRAFIA DE MENSAGEM =====")
while True:
    opc = int(input("1 - Criptografar\n2 - Descriptografar\n0 - Sair \n-> "))

    if(opc == 0):
        print("Encerrando...")
        break

    if(opc == 1):
        mensagem = input("Mensagem a ser criptografada: ")
        mensagem = mensagem.lower()
        posicao = int(input("Quantas posições você deseja avançar: "))
        resultado = encript(mensagem, posicao)
        print("Resultado: " + resultado + "\n====================================")

    if(opc == 2):
        mensagem = input("Mensagem a ser descriptografada: ")
        mensagem = mensagem.lower()
        posicao = int(input("Quantas posições você deseja retornar: "))
        resultado = decript(mensagem, posicao)
        print("Resultado: " + resultado + "\n====================================")