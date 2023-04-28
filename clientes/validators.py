import re
#validações especificas redirecionadas para os Serializers

def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11

def nome_valido(nome):
    return nome.isalpha( ), nome.isspace( )

def rg_valido(numero_rg):
    return len(numero_rg) == 5 or len(numero_rg) >= 9

def celular_valido(numero_celular):
    """verifica se o número é valido (11 98766-1717)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,numero_celular)
    return resposta