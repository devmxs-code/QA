def exibir_apresentacao(nome: str, idade: int) -> None:  # função que exibe apresentação pessoal formatada
    """Exibe apresentação pessoal formatada."""
    print(f"Olá, eu sou {nome} e tenho {idade} anos.")  # exibe mensagem de apresentação com nome e idade


if __name__ == "__main__":  # verifica se o script está sendo executado diretamente
    nome = "marcelo"  # define o nome da pessoa
    idade = 30  # define a idade da pessoa
    exibir_apresentacao(nome, idade)  # chama a função para exibir a apresentação