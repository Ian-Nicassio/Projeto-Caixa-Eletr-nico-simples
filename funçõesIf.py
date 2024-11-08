#python função if ou seja função Se

numero1 = 90
numero2 = 12
#se a variavel numero 1 é maior que a variavel numero 2
if numero1 > numero2:
    print ("o numero da variavel 1 é maior que o numero da variavel 2")

#python função if ... elif
numero3 = 6
numero4 = 6
#elif - SeNao se
if numero3 > numero4:
    print("o numero da variavel 3 é maior que o numero da variavel 4")
elif numero3 == numero4:
    print("o numero da variavel 3 é igual ao numero da variavel numero 4")

numero_secreto = 7

chute = int (input("tente adivinhar o numero entre 1 e 10: "))

if numero_secreto == chute:
    print("voce acertou")
else:
    print("voce errou")

#ex de votação
#pergunta a idade do usuario
idade = int (input("digite sua idade:"))
#verifica se a idade é maior ou igual a 18
if idade >= 18:
    print("voce é elegivel para votar")
else:
    print("voce nao é elegivel para votar")


#função if... elif ... else
#se...  senao se ... senao

numero5 = 9
numero6 = 6

if numero5 > numero6:
    print(f"o {numero5} é maior que o {numero6}")

elif numero5 == numero6:
    print(f"o {numero5} é igual ao {numero6}")

else:
    print(f"o {numero5} é menor que o {numero6}")
    
#duas condições simultaneas
numero7 = 50
numero8 = 21
numero9 = 200

if numero7 > numero8 and numero9 > numero7:
    print("as duas condições sao verdadeiras")

#ex de notas 
nota = float(input("insira a nota entre 1 - 100: "))
if nota >= 90 and nota <= 100:
    print ("excelente")
elif nota >= 70 and nota <= 89:
    print("bom")
elif nota >= 50 and nota <= 69:
    print("satisfatorio")
else:
    print("insuficiente")


valor_da_compra = float(input("insira o valor da sua compra: "))


if valor_da_compra > 1000:
     desconto =  0.20 * valor_da_compra
     print("voce recebeu 20% de desconto")

elif valor_da_compra >= 500 and valor_da_compra <= 1000:
     desconto =  0.10 * valor_da_compra
     print("voce recebeu 10% de desconto")
    
else:
     desconto = 0
     print("voce nao recebeu desconto")

valor_final = valor_da_compra - desconto
print(f"valor do desconto: r$ {desconto: .2f}")
print(f"valor final da compra: r$ {valor_final: .2f}")

#if ... or
#se ... ou

numero10 = 19
numero11 = 150
numero12 = 18

if numero10 > numero11 or numero10 > numero12:
    print(f"o {numero10} é maior que {numero11} ou o {numero10} maior que o {numero12}!")

condicao1 = input("Voce tem um convite vip? (sim/nao): ")
condicao2 = input("voce esta na lista de convidados? (sim/nao): ")
condicao3 = input("voce é um membro do clube? (sim/nao): ")

if condicao1 == "sim" or condicao2  == "sim" or condicao3  == "sim":
    print ("Bem vindo a festa")
else:
    print("desculpe, voce nao pode entrar")


n1 = int (input("digite um numero: "))
verifica_numero = n1 % 2

if verifica_numero == 0:
    print(f"o numero {n1} é par")
else:
    print(f"o numero {n1} é impar")

#estrutura condicional ternaria 

idade = 18
status = "adulto" if idade >= 18 else "menor de idade"
print(status)

#mudamos tudo para uma unica linha 
numero = 42
resultado = "par" if numero % 2 == 0 else "impar"
print(resultado)

categoria = 100
resultado = "baixa"  if  categoria < 50 else "media" if categoria < 80 else "alta"
print(resultado)
