#url query params
#base ? parâmetros
url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100".split('?')
[url_base, url_parametros] = url

'''
STRING FATIADA (slicing)
OBS: str[x:y] o x é inclusivo e o y é excludente
OBS: str são sequências imutáveis
url_base = url[:26]
url_parametros = url[27:77]
'''

parametros = url_parametros.split('&')
valor_parametros = []

for parametro in parametros:
    indice = parametro.find('=')
    valor_parametros.append(parametro[indice+1:])

print(valor_parametros)