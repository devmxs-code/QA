numero = int(input("digite um numero para ver a tabuada "))

# estrutura da tabuada
print(f"\n tabuada do {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("\n tabuada concluída") 