class ExtratorURL:    
    def __init__(self, url):
        self.url = ExtratorURL.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        return url.strip()
    
    def valida_url(self):
        if self.url == "":
            raise ValueError('A URL está vazia')
    
    def get_url_base(self):
        url = self.url

        index_simbolo_query = url.find('?')

        return url[:index_simbolo_query]
    
    def get_url_params(self):
        url = self.url

        index_simbolo_query = url.find("?")

        return url[index_simbolo_query+1:]

extrator = ExtratorURL("http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")

print(extrator.get_url_base())
print(extrator.get_url_params())