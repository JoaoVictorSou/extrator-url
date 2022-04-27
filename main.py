# URL query params
# Base ? parâmetros
url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

# Sanitização da str e validação da URL
if url.strip() == '':
    raise ValueError("A url esta vazia")

# Separando a base e os query parâmetros
[url_base, url_parametros] = url.split('?')

'''
STRING FATIADA (slicing)
OBS: str[x:y] o x é inclusivo e o y é excludente
OBS: str são sequências imutáveis
'''

parametro = 'quantidade'

if parametro in url_parametros:
    index_parametro = url_parametros.find(parametro)
    index_valor = index_parametro + len(parametro) + 1
    index_comercial = url_parametros.find('&', index_parametro)
    valor = ''

    if (url_parametros.find('&', index_parametro) == -1):
        valor = url_parametros[index_valor:]
    else:
        valor = url_parametros[index_valor:index_comercial]

    print(valor)