#Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escreva o nome escolhido.
import random
n1= str( (input ('Digite o nome do primeiro aluno:'))
n2= input ('Digite o nome do segundo aluno:')
n3= input ('Digite o nome do terceiro aluno')
n4=input ('Digite o nome do quarto aluno')
sorteado = random.choice(n1,n2,n3,n4)
print(sorteado)
