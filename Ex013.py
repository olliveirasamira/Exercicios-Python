##Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento




salario = float(input('Digite o valor do salário R$'))
aumento = salario + (salario*15/100)
print ('O valor do Salário com aumento de 15% é de {}'. format(aumento))