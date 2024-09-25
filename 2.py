# Escreva um programa que verifique, em uma string, a existência da letra ‘a’,
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que
# ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de
# sua preferência ou pode ser previamente definida no código;

def contador(s):
    contador = 0
    for char in s:
        if char == 'a' or char == 'A':
            contador += 1
    return contador

string_usuario = input("Digite uma string para verificar a letra 'a': ")
quantidade = contador(string_usuario)

if quantidade > 0:
    print(f"A letra 'a' está presente {quantidade} vez(es) na string.")
else:
    print(f"A letra 'a' não está presente na string.")