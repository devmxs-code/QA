IDADE_MINIMA_DIRIGIR = 18


def validar_idade(idade_str: str) -> int | None:
    """Valida e converte idade de string para inteiro."""
    if not idade_str.isdigit():
        return None
    idade = int(idade_str)
    return idade if idade >= 0 else None


def verificar_habilitacao(nome: str, idade: int) -> str:
    """Verifica se pessoa pode dirigir baseado na idade."""
    if idade < IDADE_MINIMA_DIRIGIR:
        return f"{nome}, você ainda NÃO possui idade mínima para dirigir.\nAguarde até completar {IDADE_MINIMA_DIRIGIR} anos."
    elif idade == IDADE_MINIMA_DIRIGIR:
        return f"{nome}, você acabou de atingir a idade mínima para dirigir! Parabéns!"
    else:
        return f"{nome}, você possui idade mínima para dirigir.\nLembre-se de sempre dirigir com responsabilidade."


def main() -> None:
    """Função principal do programa."""
    nome = input("Digite seu nome: ")
    idade_str = input("Digite sua idade: ")
    
    idade = validar_idade(idade_str)
    
    if idade is None:
        print("Por favor, digite uma idade válida (apenas números positivos).")
        return
    
    print(verificar_habilitacao(nome, idade))


if __name__ == "__main__":
    main()
