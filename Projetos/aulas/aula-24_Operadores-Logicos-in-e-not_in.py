# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# variavel_a = 1 or 0
# variavel_b = 0 or 1
# print(variavel_a, variavel_a)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# nome = 'Maria Carmo'
 
# if ' ' in nome:
#     print(f'O nome {nome} tem espaços.')
# else:
#     print(f'O nome {nome} NÃO tem espaços.')
   # -------------------------------------------------------------------------------------------------------------------------------------------------------- 
# numero = 10
 
# if numero > 1:
#     if numero > 2:
#         if numero > 3:
#             print('Número maior que 3')
#         else:
#             print('Número menor que 3')
#     else:
#         print('Número menor que 2')
# else:
#     print('Número menor que 1')
# --------------------------------------------------------------------------------------------------------------------------------------------------------