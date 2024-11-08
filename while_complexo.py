#while usando uma condição complexa 
'''
x, y = 5, 15

while x < 10 and y > 10:
    print(f"x: {x}, y: {y}")

    x += 1 #incrementando em 1 
    y -= 1 #decrementando em 1 

print("loop concluido")
print(f"valores finais - x: {x}, y: {y}")
'''

#while usando uma condição complexa


numero_secreto1 = 7  # Define o primeiro número secreto
numero_secreto2 = 3  # Define o segundo número secreto

tentativas = 5  # Número total de tentativas permitidas

adivinhou1 = False  # Variável para verificar se o primeiro número foi adivinhado
adivinhou2 = False  # Variável para verificar se o segundo número foi adivinhado

# Loop que continua enquanto houver tentativas e pelo menos um dos números não tiver sido adivinhado
while tentativas > 0 and (not adivinhou1 == True or not adivinhou2 == True):

    print(f"tentativas restantes: {tentativas}")  # Exibe quantas tentativas restam

    # Recebe os palpites do usuário para os dois números secretos
    palpite1 = int(input("adivinhe o primeiro numero secreto (1-10): "))
    palpite2 = int(input("adivinhe o segundo numero secreto (1-10): "))

    # Verifica se o primeiro palpite está correto
    if palpite1 == numero_secreto1:
        print("voce adivinhou o primeiro numero!")
        adivinhou1 = True  # Atualiza a variável para indicar que o primeiro número foi adivinhado

    # Verifica se o segundo palpite está correto
    if palpite2 == numero_secreto2:
        print("voce adivinhou o segundo numero!")
        adivinhou2 = True  # Atualiza a variável para indicar que o segundo número foi adivinhado

    # Se o jogador não tiver adivinhado ambos os números, ele perde uma tentativa
    if not adivinhou1 == True or not adivinhou2 == True:
        print("tente novamente.")
        tentativas -= 1  # Diminui o número de tentativas restantes

# Verifica se o jogador conseguiu adivinhar ambos os números antes de acabar as tentativas
if adivinhou1 == True and adivinhou2 == True: 
    print("parabens voce adivinhou ambos os numeros")
else: 
    # Se o jogador não adivinhou ambos os números, exibe os números secretos
    print(f"Voce perdeu. os numeros secretos eram {numero_secreto1}, e {numero_secreto2}")
