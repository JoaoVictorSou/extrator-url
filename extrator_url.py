import re

class ExtratorURL:
    def __init__(self, url):
        self.url = ExtratorURL.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')
        else:
            # enquanto [] significa o caractere do grupo () significa a união deles
            padrao_url = re.compile("(http[s]?://)?(www.)?bytebank.com(.br)?/cambio")
            # diferentemente de padrao.search() padrao.match() retorna o objeto quando encontra a semelhança total com o padrão
            url_semelhante = padrao_url.match(self.url)

            if url_semelhante:
                print(url_semelhante.group())
            else:
                raise ValueError("A URL não é válida")
    
    def get_url_base(self):
        url = self.url

        index_simbolo_query = url.find('?')

        return url[:index_simbolo_query]
    
    def get_url_params(self):
        url = self.url

        index_simbolo_query = url.find("?")

        return url[index_simbolo_query+1:]

    def get_valor_parametro(self, nome_parametro):
        url_parametros = self.get_url_params()

        if nome_parametro in url_parametros:
            index_nome_parametro = url_parametros.find(nome_parametro)
            index_valor = index_nome_parametro + len(nome_parametro) + 1

            if '&' in url_parametros[index_nome_parametro:]:
                index_divisor = url_parametros.find('&', index_nome_parametro)

                return url_parametros[index_valor:index_divisor]
            else:
                return url_parametros[index_valor:]

extrator = ExtratorURL('https://www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')

print(extrator.get_valor_parametro('quantidade'))

