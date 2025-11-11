# script_exercicio.py
# 1) Crie uma tupla com 5 dados
tupla = ("maçã", "banana", "laranja", "uva", "melancia")
print("Tupla original:", tupla)

# 2) Altere a tupla para uma lista
lista = list(tupla)  # converte tupla -> lista
print("Lista convertida:", lista)

# 3) Insira 2 dados extras a essa lista
# podemos usar append (um por um) ou extend (lista de itens)
lista.append("abacaxi")      # insere um elemento no final
lista.append("pera")         # insere outro elemento no final
# alternativamente: lista.extend(["abacaxi", "pera"])
print("Lista após inserir 2 dados:", lista)

# 4) Remova o primeiro dado da lista
# duas formas: del lista[0] ou lista.pop(0)
primeiro_removido = lista.pop(0)  # remove e retorna o primeiro item (index 0)
print("Removi o primeiro dado:", primeiro_removido)
print("Lista agora:", lista)

# 5) Remova o último dado da lista
ultimo_removido = lista.pop()  # sem índice remove o último
print("Removi o último dado:", ultimo_removido)
print("Lista agora:", lista)

# 6) Faça um print com o primeiro dado da lista
# acessando pelo índice 0
if lista:  # verifica se lista não está vazia
    print("Primeiro dado atual da lista:", lista[0])
else:
    print("A lista está vazia, nenhum primeiro dado para mostrar.")

# 7) Faça um print com a quantidade de dados da lista
print("Quantidade de dados na lista:", len(lista))

# 8) Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
pessoa = {
    "Nome": "Carlos Silva",
    "Idade": 30,
    "Profissão": "Desenvolvedor"
}
print("Dicionário criado:", pessoa)

# 9) Imprima somente o valor contido na chave Nome do dicionário
# usando acesso por chave (vai gerar KeyError se chave não existir)
print("Valor da chave 'Nome':", pessoa["Nome"])
# alternativa segura: pessoa.get("Nome")
