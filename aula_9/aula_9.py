import requests

def verificar_frete_gratis(cep):
    """Verifica se o CEP informado pertence às regiões Norte ou Nordeste."""
    REGIAO_NORTE = {"AC", "AM", "AP", "PA", "RO", "RR", "TO"}
    REGIAO_NORDESTE = {"AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"}
    
    # Limpa o CEP, removendo traços e espaços
    cep = cep.replace("-", "").strip()

    # Validação simples
    if not cep.isdigit() or len(cep) != 8:
        return "CEP inválido. Deve conter 8 dígitos numéricos."

    # Consulta API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return "Erro na consulta. Tente novamente mais tarde."

    dados = resposta.json()

    if "erro" in dados:
        return "CEP não encontrado."

    estado = dados["uf"]

    if estado in REGIAO_NORTE or estado in REGIAO_NORDESTE:
        return f"Frete grátis disponível para {estado} ({dados['localidade']})."
    else:
        return f"Frete não disponível para {estado} ({dados['localidade']})."


# Programa principal
if __name__ == "__main__":
    cep_usuario = input("Digite seu CEP: ")
    resultado = verificar_frete_gratis(cep_usuario)
    print(resultado)
