dias_seguidos = 21

completou_dias = input(f" você completou {dias_seguidos} dias seguidos no desafio? (sim/não):").strip().upper()

if dias_seguidos >= 21:
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ.")


elif dias_seguidos >= 1:
    print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO.")

else:
    print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
