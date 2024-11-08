#imprimindo as posições das letras
posicao_letra = "python"
print(posicao_letra[0])
print(posicao_letra[1])
print(posicao_letra[2])
print(posicao_letra[3])
print(posicao_letra[4])

#slice
frase = "ola, mundo!"
#obterndo uma parte da string
parte = frase[4:8]
print(parte)
#obtendo os primeiros 5 caracteres da str
primeiros = frase [:5]
print(primeiros)
#obtendo os ultimos 6 caracteres da str
ultimos = frase[-6:]
print(ultimos)

#verifica se a palavra python esta em "palavra"
palavra = "o modulo de python é muito legal"
print("python" in palavra)

#if = se
palavra = "o modulo de python é muito legal"
if "python" in palavra:
    print("sim a a palavra python esta presente" )

#strip = usamos para remover espaços em branco do inicio e do final da frase
palavra = "      o modulo de python é muito legal     "
print(palavra.strip())

#split = divide a frase em palavras usando espaço em branco como separador
texto = "ola, como vai voce?"
palavras = texto.split()
print (palavras)

#junta elementos de uma lista como uma unica string
mensagem = ['ola,', 'como', 'vai', 'voce?']
frase2 = ' '.join (mensagem)
print(frase2)

#strip removeu todos os carcteres de */multiplicação
texto2 = "******ola!******"
texto_strip = texto2.strip('*')
print(texto_strip)








