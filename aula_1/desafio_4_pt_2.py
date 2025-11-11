def exibir_dados_usuario(nome: str, altura: float, idade: int) -> None:
    """Exibe dados do usuário formatados."""
    print("\n--- Dados do Usuário ---")
    print(f"Nome: {nome}")
    print(f"Altura: {altura:.2f} m")
    print(f"Idade: {idade} anos")


if __name__ == "__main__":
    exibir_dados_usuario("Marcelo", 1.67, 30)
