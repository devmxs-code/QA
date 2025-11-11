
# Validar dominio do email.
'@jogajuntoinstituto.org'

def verificar_dominio(email_usuario):
    """Verifica se o domínio '@jogajuntoinstituto.org' está contido no e-mail."""
    
    
    DOMINIO_ALVO = "@jogajuntoinstituto.org"
    
    
    if DOMINIO_ALVO in email_usuario:
        return True
    else:
        return False


while True:
    email_digitado = input("Digite seu e-mail para verificação: ").strip()

 
    if verificar_dominio(email_digitado):
        print(f"\n SUCESSO! O e-mail '{email_digitado}' é VÁLIDO para o instituto.")
    else:
        print(f"\n FALHA! O e-mail '{email_digitado}' NÃO contém o domínio correto.")
        break
    

