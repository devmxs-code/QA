# formulario
nome_pet = input('digite o nome do dog: ')
idade_humana_pet = int(input('digite a idade humana do dog: '))
porte = input('digite o porte (P/M/G): ').upper()
quantidade_banhos = int(input('quantos banhos em 12 meses: '))

# padrao de idade do cachorro
idade_cachorro = idade_humana_pet * 7

# script
if porte == 'G':
    lucro_total = quantidade_banhos * (75 - 20)
elif porte == 'M':
    lucro_total = quantidade_banhos * (60 - 15)
elif porte == 'P':
    lucro_total = quantidade_banhos * (50 - 5)
else:
    print('porte invalido!')
    exit()


# retorno 
print(f'Ola, {nome_pet} tem {idade_cachorro} anos e nos ultimos 12 meses o lucro com este animal foi de R$ {lucro_total:.2f}')