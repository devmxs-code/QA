def gerar_mensagem_cupom(nome: str, mes: str, valor: float, desconto: int, cupom: str) -> str:
    """Gera mensagem de cupom de desconto."""
    return f"Olá, {nome}, em {mes}, você realizou uma compra no valor de R$ {valor:.2f} e ganhou um desconto de {desconto}% em sua próxima compra. Use o cupom {cupom}."


if __name__ == "__main__":
    print(gerar_mensagem_cupom("Paula Martins", "janeiro", 500.00, 10, "paulaé10"))