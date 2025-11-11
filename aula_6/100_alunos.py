def verificar_time(matricula: int) -> str:
    """Verifica qual time o aluno pertence baseado na matrícula (par/ímpar)."""
    return "VOCÊ ESTÁ NO TIME AZUL" if matricula % 2 == 0 else "VOCÊ ESTÁ NO TIME AMARELO"


def main() -> None:
    """Função principal do programa."""
    matricula = int(input("Digite o número da sua matrícula: "))
    print(verificar_time(matricula))


if __name__ == "__main__":
    main()