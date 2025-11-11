import pandas as pd

DADOS = {
    "nome": ["Ana", "Bruno", "Carlos", "Diona"],
    "idade": [23, 35, 45, 29],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"]
}


def criar_dataframe(dados: dict) -> pd.DataFrame:
    """Cria DataFrame a partir de dicionário."""
    return pd.DataFrame(dados)


def filtrar_por_cidade(df: pd.DataFrame, cidade: str) -> pd.DataFrame:
    """Filtra DataFrame por cidade."""
    return df[df["Cidade"].str.lower() == cidade.lower()]


def main() -> None:
    """Função principal do programa."""
    df = criar_dataframe(DADOS)
    
    print("DataFrame completo:")
    print(df)
    
    df_salvador = filtrar_por_cidade(df, "salvador")
    print("\nMoradores de Salvador:")
    print(df_salvador)


if __name__ == "__main__":
    main()