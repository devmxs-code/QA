# Promoção da Farmácia MINHA FARMA

# Entrada: valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verificação da promoção
print("\n=== NOTA FISCAL ===")

if valor_compra >= 100:
    # Caso o cliente atinja o valor mínimo da promoção
    print("SUA SAÚDE É O QUE IMPORTA.")
    print("APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R$10 REAIS DE DESCONTO.")
else:
    # Caso não atinja o valor mínimo
    print("OBRIGADO POR ESCOLHER A MINHA FARMA.")
    print("VOCÊ SABIA QUE COMPRAS ACIMA DE R$100 REAIS GERAM UM VOUCHER DE R$10 REAIS DE DESCONTO PARA A PRÓXIMA COMPRA?")

print("====================")
print(f"Valor da compra: R$ {valor_compra:.2f}")
