#url query params
#base ? parâmetros
url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100".split('?')
[url_base, url_parametros] = url

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