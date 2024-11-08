"""
escopo de variaveis 
variaveis locais vs globais
uso global
uso nonlocal (em funções alinhadas )
"""

#variavel local so mexe dentro da função a global em qualquer lugar do cod
variavel_global = "eu sou uma variavel global"

def funcao_exemplo():
    variavel_local = "eu sou uma variavel local"
    print(variavel_local)
    print(variavel_global)
funcao_exemplo()

#inicializa com 0
contador = 0 
#define a função
def incrementar_contador ():
    #informando que é uma variavel global
    global contador 
    #incrementando o contador
    contador += 1
    #imprimindo na tela
    print(contador)
#chamando a função incrementar pela primeira vez
incrementar_contador ()
#chamando a função incrementar pela segunda vez
incrementar_contador ()
#chamando a função incrementar pela terceira vez
incrementar_contador ()


#uso do nonlocal (em funções alinhadas)

def funcao_externa():

    variavel_externa = "eu sou externa"
    print(variavel_externa)
    
    def funcao_interna():

        nonlocal variavel_externa

        variavel_externa = "eu fui modificada pela funçao interna"

        print(variavel_externa)

    funcao_interna()

    print(variavel_externa)

funcao_externa()

"""
funções como objetos de primeira classe 

atribuindo funções a variaveis
passando funções como argumentos
retornando funções de outras funções
"""
#atribuindo funções a variaveis

def saudacao():

    return "ola, mundo"

cumprimentar = saudacao

print(cumprimentar())

#passando funções como argumentos

def saudacao_nome(nome):

    return f"ola, {nome}"

def cumprimentar (funcao, nome):

    return funcao (nome)

print(cumprimentar(saudacao_nome, "alice"))

#retornando funções de outras funções

def nivel_saudacao(nivel):
    def saudacao_basica():
        return "oi"
    
    def saudacao_avancada():

        return "ola como voce esta?"
    if nivel == "basico":
       return saudacao_basica
    else:
        return saudacao_avancada
    
cumprimento = nivel_saudacao ("teste")
print(cumprimento())