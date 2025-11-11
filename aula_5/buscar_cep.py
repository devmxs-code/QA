import requests  # importa a biblioteca requests para fazer requisições http
from typing import Optional, Dict  # importa tipos para type hints

BASE_URL = "https://viacep.com.br/ws"  # define a url base da api viacep
INTEGRANTES = {  # dicionário com os integrantes e seus ceps
    "Marcelo": "11630099",  # cep do marcelo
    "Isla": "11630097"  # cep da isla
}


def formatar_cep(cep: str) -> str:  # função que remove caracteres não numéricos do cep
    """Remove caracteres não numéricos do CEP."""
    return ''.join(filter(str.isdigit, cep))  # retorna apenas os dígitos do cep


def validar_cep(cep: str) -> bool:  # função que valida o formato do cep
    """Valida formato do CEP (deve ter 8 dígitos)."""
    cep_limpo = formatar_cep(cep)  # formata o cep removendo caracteres não numéricos
    return len(cep_limpo) == 8  # retorna true se o cep tiver 8 dígitos


def buscar_dados_cep(cep: str) -> Optional[Dict[str, str]]:  # função que busca dados completos do cep
    """Busca dados completos do CEP usando API ViaCEP."""
    cep_formatado = formatar_cep(cep)  # formata o cep
    
    if not validar_cep(cep_formatado):  # verifica se o cep é válido
        return None  # retorna none se o cep for inválido
    
    url = f"{BASE_URL}/{cep_formatado}/json/"  # monta a url da requisição
    
    try:  # tenta fazer a requisição
        resposta = requests.get(url, timeout=5)  # faz a requisição get com timeout de 5 segundos
        resposta.raise_for_status()  # levanta exceção se houver erro na requisição
        dados = resposta.json()  # converte a resposta para json
        
        # verifica se cep foi encontrado (api retorna erro quando não encontra)
        if dados.get("erro"):  # verifica se a api retornou erro
            return None  # retorna none se o cep não foi encontrado
        
        return dados  # retorna os dados do cep
    except requests.RequestException:  # captura exceções de requisição
        return None  # retorna none em caso de erro


def buscar_cidade_por_cep(cep: str) -> str:  # função que busca apenas a cidade pelo cep
    """Busca cidade através do CEP usando API ViaCEP."""
    dados = buscar_dados_cep(cep)  # busca os dados completos do cep
    
    if dados:  # verifica se os dados foram encontrados
        return dados.get("localidade", "Cidade não encontrada")  # retorna a cidade
    return "CEP inválido ou não encontrado"  # retorna mensagem de erro


def exibir_dados_completos(dados: Dict[str, str]) -> None:  # função que exibe dados completos do cep
    """Exibe dados completos do CEP formatados."""
    print("\n" + "="*50)  # exibe linha separadora
    print("DADOS DO CEP")  # exibe título
    print("="*50)  # exibe linha separadora
    print(f"CEP: {dados.get('cep', 'N/A')}")  # exibe o cep
    print(f"Logradouro: {dados.get('logradouro', 'N/A')}")  # exibe o logradouro
    print(f"Complemento: {dados.get('complemento', 'N/A')}")  # exibe o complemento
    print(f"Bairro: {dados.get('bairro', 'N/A')}")  # exibe o bairro
    print(f"Cidade: {dados.get('localidade', 'N/A')}")  # exibe a cidade
    print(f"Estado: {dados.get('uf', 'N/A')}")  # exibe o estado
    print(f"IBGE: {dados.get('ibge', 'N/A')}")  # exibe o código ibge
    print(f"DDD: {dados.get('ddd', 'N/A')}")  # exibe o ddd
    print("="*50)  # exibe linha separadora


def buscar_cep_interativo() -> None:  # função que permite buscar cep de forma interativa
    """Permite buscar CEP de forma interativa."""
    while True:  # loop infinito
        cep = input("\nDigite o CEP (ou 'sair' para encerrar): ").strip()  # solicita o cep ao usuário
        
        if cep.lower() == 'sair':  # verifica se o usuário quer sair
            print("Encerrando...")  # exibe mensagem de encerramento
            break  # sai do loop
        
        if not validar_cep(cep):  # verifica se o cep é válido
            print("CEP inválido! Digite um CEP com 8 dígitos.")  # exibe mensagem de erro
            continue  # continua o loop
        
        dados = buscar_dados_cep(cep)  # busca os dados do cep
        
        if dados:  # verifica se os dados foram encontrados
            exibir_dados_completos(dados)  # exibe os dados completos
        else:  # se os dados não foram encontrados
            print("CEP não encontrado. Verifique se o CEP está correto.")  # exibe mensagem de erro


def main() -> None:  # função principal do programa
    """Função principal do programa."""
    print("="*50)  # exibe linha separadora
    print("CONSULTA DE CEP - VIA CEP API")  # exibe título
    print("="*50)  # exibe linha separadora
    
    # busca ceps dos integrantes
    print("\n--- Integrantes ---")  # exibe cabeçalho
    for nome, cep in INTEGRANTES.items():  # percorre os integrantes
        dados = buscar_dados_cep(cep)  # busca os dados do cep
        if dados:  # verifica se os dados foram encontrados
            print(f"\n{nome} (CEP: {dados.get('cep', cep)})")  # exibe o nome e cep
            print(f"  Cidade: {dados.get('localidade', 'N/A')}")  # exibe a cidade
            print(f"  Estado: {dados.get('uf', 'N/A')}")  # exibe o estado
            print(f"  Bairro: {dados.get('bairro', 'N/A')}")  # exibe o bairro
        else:  # se os dados não foram encontrados
            print(f"\n{nome}: CEP não encontrado")  # exibe mensagem de erro
    
    # modo interativo
    print("\n" + "="*50)  # exibe linha separadora
    opcao = input("\nDeseja buscar outro CEP? (s/n): ").strip().lower()  # solicita opção ao usuário
    
    if opcao == 's':  # verifica se o usuário quer buscar outro cep
        buscar_cep_interativo()  # chama a função interativa


if __name__ == "__main__":  # verifica se o script está sendo executado diretamente
    main()  # chama a função principal