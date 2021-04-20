# Comentarios usando hastag
#_STRINGS
# O comando abaixo mesmo em hastag o python consegue interpretar as acentuãções latinas
# -*- coding: utf-8 -*-
print ("Hello_World")
"""print ("Hello_World") ou usando 3 aspas"""
print ("ÇÂõ")

#variável
mensagem = "Hello World"
print (mensagem)
#variáveis não aceitam espaços nem caracteres especiais(^~!?/) apenas ligando por underlines(_), além da diferença entre caixa alta
# O igual (=) é um operador de atribuição

#_NUMBER(Integer,Float)
print(2 + 2) #soma
print(1 - 2) #subtração
print(8 / 5) #divisão
print(6 * 2) #multiplicação
print(2 ** 3) #expoenciação
print(10 % 3) #valor do resto de uma divisão

var1 = 1 #variável integer
var2 = 1.1 #variável float
var3 = "Sou uma string" #variavel string
var4 = True #Boolean True
var4 = False #Boolean True

print(var1)
print(var2)
print(var3)
print(var4)
#Em python ele atribui o ultimo valor se a variável for igual


x = 2
y = 3
z = 2

#Operadores Relacionais
print (x == y) # Igual
print (x != y) # Diferente
print (x > y) # Maior que
print (x < y) # Menor que
print (x >= y) # Maior ou igual a
print (x <= y)  # Menor ou igual a



#Operadores Lógicos
print (x == y and x == z) #AND
print (x == y or x == z)  #OR
print (x == y and x == z) #NOT


a = 5
b = 5
#Comandos Condicionais
if a > b :		#IF
	print ("A variável A é maior que B")
elif b > a :	#ELSE IF
	print ("A variável B é maior que A")
else :			#ELSE
	print ("A e B são iguais")


#Laços de repetição (WHILE da linguagem C)
i = 0
while i <= 10:
	print (i)
	i += 1 # i = i+1


#Laços de repetição (FOR da linguagem C)
for i in range(10):
	print(i)


#Laços de repetição com ARRAYS
lista1 = [9,99,999,9999,99999]
lista2 = ["Hello","World","!"]
lista3 = [0, "Hello", "ZEQUINHA", 9.99, "?", True]

for i in lista1:
	print(i)

for i in lista2:
	print(i)

for i in lista3:
	print(i)


#FOR e RANGE
for i in range(10,20,2): #começa do valor 10, vai até o 20 - 1, pulando de 2 em 2
	print(i)


#Concatenação de Strings
a = "Zeca"
b = "Johnsons"
concatenar = a + " " + b
tamanho = len(concatenar)
print(concatenar)

#Tamanho de Strings
seq = "UWIDAWIUDJSDIOUHSJIOLSIKHDAWIOJIOIWJD"

print(len(seq)) #Função len vai numerar todos os caracteres

#Navegação entre o índice

seq = "CGAT CGAC TAGC TCAC TACT AGCT ACGA"

letra = seq[1] #vai exibir o valor da posição 1, no caso a letra (G)
print(letra)


#Imprimir um pedaço da string
seq = "CGATCGACTAGCTCACTACTAGCTACGA"

print(seq[0:4]) #Escolhe de onde começa no caso (0) e até onde vai (4)


#Strings em Python são objetos, podendo aplicar métodos apartir de um ponto(.) o nome do método e parentêses()

seq = "CGATCGACTAGCTCACTACTAGCTACGA"
seq = seq.lower() #Esse método .lower() serve para deixar a string em caixa baixa
print(seq)

seq = seq.upper() #Esse método .upper() serve para deixar a string em caixa alta
print(seq)

seq = "\n cgatcgactagctcactactagctacga \n"
seq = seq.strip() #Esse método .strip() serve para remover espaços ou querbras de linha do começo e do fim de uma string
print(seq)

seq = "CGAT CGAC TAGC TCAC TACT AGCT ACGA"
seq = seq.split() #Esse método .split() serve para converter uma string em lista
print(seq)

seq = "CGAT CGAC TAGC TCAC TACT AGCT ACGA"
busca = seq.find("TCAC") #Esse método .find() serve para encontrar o que está dentro do parênteses () e buscar o primeiro índice da posição dele na string
print(busca)

seq = "CGAT CGAC TAGC TCAC TACT AGCT ACGA"
seq = seq.replace("TAGC","ATCG") #Esse método .replace() serve para trocar de valor do primeiro para o segundo dentro do parênteses ()
print(seq)


#Modularização/Funções
def soma(a,b):		#def é uma sintaxe para definir uma função E que pode ser usada APENAS nesse escopo, ou seja, não é global
	return a+b

def multiplicacao(a,b):		#def é uma sintaxe para definir uma função E que pode ser usada APENAS nesse escopo, ou seja, não é global
	return a*b

s = soma(2, 3)
m = multiplicacao(4, 5)

print(soma(s, m))	#aqui é onde ocorre a chamada da função



#ARQUIVOS(Leitura, Criação)
arq = open("arquivo.txt")
print(arq.readline()) 		#imprime a primeira linha do texto

arq = open("arquivo.txt")
linhas = arq.readlines() 
for linha in linhas:
	print(linhas)			#imprime todas as linhas do texto colocando em uma lista

arq = open("arquivo.txt")
texto_completo = arq.read() 
print(texto_completo)		#imprime todo o conteúdo do texto com a mesma formatação



w = open("arquivo2.txt", "w")	#cria um arquivo com o nome na primeira aspas, mas com conteúdo em branco

w.write("Isso é tudo pe-pe-p-pessoal")	#escreve no arquivo o que está entre aspas

w.close()


#LISTAS
minha_lista1 = ["abacaxi, melancia, maçã"]
minha_lista2 = [4,0,1,5,9]
minha_lista3 = ["Zeca", 4, True, 9.9999]

for item in minha_lista3:
	print(item)		#Imprime todos os itens da lista um por linha

tamanho = len(minha_lista3)
print(tamanho)		#Imprime a quantidade de itens da lista

minha_lista3.append("ZEQUINHA")	#adiciona o que está entre aspas no final da lista
print(minha_lista3)


if 4 in minha_lista2:
	print("4 esta na lista")

del minha_lista1[:]	 #remove todo conteúdo da lista
print(minha_lista1)


#ORDERNAR LISTAS(.sort)
lista = [3,4,47,5,17,9,3,4,7,8]

lista.reverse()	#inverte a posição inicial da lista
print(lista)

lista.sort()	#organiza a lista em ordem crescente e de A - Z
print(lista)

lista.sort(reverse=True)	#organiza a lista em ordem decrescente e de Z - A
print(lista)



#DICIONÀRIOS(arrays associativos)
meu_dicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}
print(meu_dicionario["A"])

for chave in meu_dicionario:
	print(chave+":"+meu_dicionario[chave])



#NÙMEROS ALEATÓRIOS
import random

numero = random.randint(0, 10)	#vai escolhe um numero qualquer entre os 2 que foi fornecido no parênteses
print(numero)

b = numero

lista = [3,6,4,7,4]
numero = random.choice(lista)	#escolhe apenas os números dentro da lista
print(numero)

random.seed(1)	#codigo de um valor específico, nunca muda
numero = random.randint(0, 10)
print(numero)


#TRATAMENTO DE EXCEÇÕES
a = 2

try:	#tente excecutar essa linha abaixo
	print(a/b)
except:	#se não conseguir faça essa
	print("Não é permitida divisão por 0")


#LIST COMPREHENSION
#Usando laço
x = [1,2,3,4,5]
y = [i**2 for i in x]

print(x)
print(y)

#
z = [i for i in x if i%2==1]
print(z)


#Função Enumerada
lista = ["abacate", "bola", "cachorro"]
for i, nome in enumerate(lista):
	print(i, nome)


#Função MAP
def dobro(x):
	return x*2

valor = [1,2,3,4,5,6]
valor_dobrado = (map(dobro, valor))

print(list(valor_dobrado))


#Função Reduce, recebe uma lista e retorna um único valor para ela
from functools import reduce

def soma(x, y):
	return x+y

lista = [1, 3, 5, 10, 20]

soma = reduce(soma,lista)
print(soma)


#Função ZIP, concatenar 2 listas ou mais
lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$1,00", "R$2,00", "R$5,00", "R$10,00", "R$120,00"]

for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)