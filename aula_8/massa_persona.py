from faker import Faker  # importa a biblioteca faker para gerar dados fictícios
import csv  # importa o módulo csv para trabalhar com arquivos csv
from datetime import datetime  # importa datetime para obter o ano atual

IDADE_MINIMA = 18  # define a idade mínima para geração de personas
IDADE_MAXIMA = 65  # define a idade máxima para geração de personas
ANO_ATUAL = datetime.now().year  # obtém o ano atual do sistema
CAMPOS_CSV = ["Nome", "Data de Nascimento", "Idade", "Cidade"]  # define as colunas do arquivo csv


def criar_persona(fake: Faker) -> dict:  # função que cria uma persona com dados fictícios
    """Cria uma persona com dados fictícios."""
    nascimento = fake.date_of_birth(minimum_age=IDADE_MINIMA, maximum_age=IDADE_MAXIMA)  # gera data de nascimento aleatória
    return {  # retorna um dicionário com os dados da persona
        "Nome": fake.name(),  # gera um nome fictício
        "Data de Nascimento": nascimento.strftime("%d/%m/%Y"),  # formata a data no padrão brasileiro
        "Idade": ANO_ATUAL - nascimento.year,  # calcula a idade baseada no ano atual
        "Cidade": fake.city()  # gera uma cidade fictícia
    }


def gerar_personas(quantidade: int) -> list[dict]:  # função que gera uma lista de personas
    """Gera lista de personas."""
    fake = Faker("pt_BR")  # inicializa o faker em português do brasil
    return [criar_persona(fake) for _ in range(quantidade)]  # cria uma lista com a quantidade especificada de personas


def salvar_csv(nome_arquivo: str, quantidade: int) -> None:  # função que salva personas em arquivo csv
    """Salva personas em arquivo CSV."""
    personas = gerar_personas(quantidade)  # gera a lista de personas
    
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:  # abre o arquivo para escrita
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_CSV)  # cria um escritor de csv baseado em dicionários
        escritor.writeheader()  # escreve o cabeçalho no arquivo
        escritor.writerows(personas)  # escreve todas as linhas (personas) no arquivo
    
    print(f"Arquivo '{nome_arquivo}' criado com {quantidade} personas!")  # exibe mensagem de confirmação


if __name__ == "__main__":  # verifica se o script está sendo executado diretamente
    salvar_csv("personas.csv", 20000)  # chama a função para criar o arquivo com 20000 personas