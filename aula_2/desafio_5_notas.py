def calcular_media(notas: list[float]) -> float:  # função que calcula a média de uma lista de notas
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas)  # retorna a soma das notas dividida pela quantidade


def coletar_notas(quantidade: int = 4) -> list[float]:  # função que coleta notas do usuário
    """Coleta notas do usuário."""
    return [float(input(f"Digite a {i+1}ª nota: ")) for i in range(quantidade)]  # retorna uma lista com as notas digitadas


def main() -> None:  # função principal do programa
    """Função principal do programa."""
    nome = input("Digite seu nome: ")  # solicita o nome do usuário
    notas = coletar_notas()  # coleta as notas do usuário
    media = calcular_media(notas)  # calcula a média das notas
    
    print("\n--- Resultado ---")  # exibe cabeçalho do resultado
    print(f"{nome}, sua média é {media:.2f}")  # exibe o nome e a média com 2 casas decimais


if __name__ == "__main__":  # verifica se o script está sendo executado diretamente
    main()  # chama a função principal
