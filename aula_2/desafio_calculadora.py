import math  # importa o módulo math para operações matemáticas


def calcular_operacoes(valor: int) -> dict[str, float]:  # função que calcula operações matemáticas de um valor
    """Calcula operações matemáticas de um valor."""
    return {  # retorna um dicionário com os resultados
        "dobro": valor * 2,  # calcula o dobro do valor
        "triplo": valor * 3,  # calcula o triplo do valor
        "quadrado": valor ** 2,  # calcula o quadrado do valor
        "raiz_quadrada": math.sqrt(valor),  # calcula a raiz quadrada do valor
        "raiz_cubica": valor ** (1/3)  # calcula a raiz cúbica do valor
    }


def exibir_resultados(valor: int, resultados: dict[str, float]) -> None:  # função que exibe os resultados formatados
    """Exibe resultados formatados."""
    print(f"O dobro do valor informado é: {resultados['dobro']}")  # exibe o dobro
    print(f"O triplo do valor informado é: {resultados['triplo']}")  # exibe o triplo
    print(f"O valor informado ao quadrado é: {resultados['quadrado']}")  # exibe o quadrado
    print(f"A raiz quadrada do valor informado é: {resultados['raiz_quadrada']:.2f}")  # exibe a raiz quadrada com 2 casas decimais
    print(f"A raiz cúbica do valor informado é: {resultados['raiz_cubica']:.2f}")  # exibe a raiz cúbica com 2 casas decimais


def main() -> None:  # função principal do programa
    """Função principal do programa."""
    valor = int(input("Informe um valor: "))  # solicita um valor ao usuário
    resultados = calcular_operacoes(valor)  # calcula as operações matemáticas
    exibir_resultados(valor, resultados)  # exibe os resultados


if __name__ == "__main__":  # verifica se o script está sendo executado diretamente
    main()  # chama a função principal