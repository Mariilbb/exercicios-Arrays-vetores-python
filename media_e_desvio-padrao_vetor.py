def isdigit_(caractere):
    # Verifica se o código ASCII do caractere está no intervalo correspondente aos dígitos (48 a 57)
    if 48 <= ord(caractere) <= 57:
        return True
    else:
        return False

# Exemplo de uso:
caractere = '5'
if isdigit_(caractere):
    print(f"{caractere} é um dígito.")
else:
    print(f"{caractere} não é um dígito.")













