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

    # os dundle methods, ou magic methods, são chamados pelo python no interpretador. Fazem parte da estrutura da linguagem

    def __len__(self):
        return len(self.url)

    # todo objeto do python implementa __str__ por padrão, retornando o tipo e o endereço da memória.
    def __str__(self):
        return self.url + "\n" + f"Base: {self.get_url_base()}" + "\n" + f"Parâmetros: {self.get_url_params()}"

    # em uma classe, de forma padrão, é implementado como a comparação dos endereços dos objetos na memória
    def __eq__(self, other):
        return self.url == other.url

url = 'www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
extrator = ExtratorURL(url)

print(f"Valor do parâmetro 'quantidade': {extrator.get_valor_parametro('quantidade')}")
print(f"Tamanho da URL no extrator: {len(extrator)}")

# o print chama str() para puder imprimir
print(f"Conteúdo do extrator: {extrator}")

# o == chama o método __eq__()
print(f"São iguais? ", extrator == ExtratorURL(url))

# is é uma palavra especial que compara os endereços na memória
print(f"São os mesmos? ", extrator is ExtratorURL(url))

