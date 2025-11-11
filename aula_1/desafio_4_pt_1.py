def coletar_dados_usuario() -> dict:
    """Coleta dados do usuário via input."""
    return {
        "nome": input("Digite seu nome: "),
        "altura": float(input("Digite sua altura em metros (ex: 1.67): ")),
        "idade": int(input("Digite sua idade: "))
    }


def exibir_dados_usuario(dados: dict) -> None:
    """Exibe dados do usuário formatados."""
    print("\n--- Dados do Usuário ---")
    print(f"Nome: {dados['nome']}")
    print(f"Altura: {dados['altura']:.2f} m")
    print(f"Idade: {dados['idade']} anos")


if __name__ == "__main__":
    dados = coletar_dados_usuario()
    exibir_dados_usuario(dados)
