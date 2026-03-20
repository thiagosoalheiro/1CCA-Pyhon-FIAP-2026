from numba.core.cgutils import printf

print ("Olá Mundo")
print(7 + 4)
print("print 7 + 4")
print ("7" + "4") # CONTATENAÇÃO DE STRINGS

# COMENTÁRIO DE UMA LINHA

'''
Comentários de 
múliplas
linhas
'''

# VARIÁVEIS
nome = "Thiago"
idade = 18 # int
peso = 68.4 # float

print(nome, idade, peso)
print(f"Oiii {nome}!!!!")

# INPUT - SIMULAÇÃO DE UM FORMS NO CMD
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))

nova_idade = idade + 1

print(nome, idade)
print(idade + 1)
