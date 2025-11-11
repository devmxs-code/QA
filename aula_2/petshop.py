IDADE_CANINA_MULTIPLICADOR = 7
PRECOS_BANHO = {"G": 75, "M": 60, "P": 50}
CUSTOS_BANHO = {"G": 20, "M": 15, "P": 5}


def calcular_idade_canina(idade_humana: int) -> int:
    """Calcula idade canina baseada na idade humana."""
    return idade_humana * IDADE_CANINA_MULTIPLICADOR


def calcular_lucro(porte: str, quantidade_banhos: int) -> float:
    """Calcula lucro total baseado no porte e quantidade de banhos."""
    if porte not in PRECOS_BANHO:
        raise ValueError(f"Porte inválido: {porte}. Use P, M ou G.")
    
    preco = PRECOS_BANHO[porte]
    custo = CUSTOS_BANHO[porte]
    return quantidade_banhos * (preco - custo)


def main() -> None:
    """Função principal do programa."""
    nome_pet = input("Digite o nome do pet: ")
    idade_humana = int(input("Digite a idade humana do pet: "))
    porte = input("Digite o porte (P/M/G): ").upper()
    quantidade_banhos = int(input("Quantos banhos em 12 meses: "))
    
    idade_canina = calcular_idade_canina(idade_humana)
    
    try:
        lucro_total = calcular_lucro(porte, quantidade_banhos)
        print(f"{nome_pet} tem {idade_canina} anos e nos últimos 12 meses o lucro com este animal foi de R$ {lucro_total:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()