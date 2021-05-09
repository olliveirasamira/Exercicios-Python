#Crie um programa que leia um numero real qualquer e mostre na tela sua porção inteira.

import math
n = float(input('Digite um número'))
int = math.floor(n)
print ('O numero é : {} e sua porção inteira é {}'.format(n, int))
