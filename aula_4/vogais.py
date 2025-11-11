"""Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário.

Implementem uma função que receba uma palavra qualquer (string) como entrada.
O programa deve imprimir o número total de vogais na palavra.
Solicitação de Entrada:

Implementem a solicitação de entrada de uma palavra (string).
Contagem de Vogais:

Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.
Imprima o número total de vogais na palavra."""

# função vogais
def contar_vogais(palavra):
    
    # definir as vogais
    vogais = "aeiouAEIOU"
    contador = 0
    # percorrer cada letra na palavra
    for letra in palavra:
        if letra in vogais:
            contador += 1
            
        return contador
        
        # solicitar entrada do usuario
        palavra_usuario = input("DIGITE UMA PALAVRA:").strip()
        total_vogais = contar_vogais(palavra_usuario)
        print(f" palavra " "{palavra_usuario}" "tem {total_vogais} vogais.")
        