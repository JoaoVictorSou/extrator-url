import requests

class ConversorMoeda:
    # atributo estático, moedas aceitas pelo conversor
    moedas = ['USD',
              'BRL']

    def __init__(self, moeda_origem, moeda_destino, quantidade=0):
        self.__moeda_origem = self.valida_moedas_em_conversor(moeda_origem)
        self.__moeda_destino = self.valida_moedas_em_conversor(moeda_destino)
        self.__quantidade = self.valida_quantidade(quantidade)

    # método que irá converter o valor informado nos atributos do objeto
    def converter(self):
        # consumo de API para pegar o valor atual das moedas
        endpoit = 'https://economia.awesomeapi.com.br/json/last/'
        response = requests.get(f"{endpoit}/{self.__moeda_origem}-{self.__moeda_destino}")
        conversao = response.json()

        # retorno do valor da conversão da moeda, considerando o valor do cambio e a quantidade imposta
        return float(conversao[f'{self.__moeda_origem}{self.__moeda_destino}']['ask']) * self.__quantidade

    # método que pode ser utilizado pela própria classe para ver se uma quantia informada por ser entendido como dinheiro
    @staticmethod
    def valida_quantidade(quantidade):
        tipo_quantidade = type(quantidade)
        if (tipo_quantidade is float) or (tipo_quantidade is int):
            if quantidade >= 0:
                return quantidade

        raise ValueError(
            'erro: quantidade da moeda deve ser um valor numérico maior que zero residente do conjutos dos reais.')

    # método que pode ser utilizado pela própria classe para a consulta de um tipo válido no conversor
    @staticmethod
    def valida_moedas_em_conversor(moeda):
        if moeda in ConversorMoeda.moedas:
            return moeda

        raise ValueError('moeda escolhida não existe nos tipos do conversor.')

    @property
    def moeda_origem(self):
        return self.__moeda_origem

    @property
    def moeda_destino(self):
        return self.__moeda_destino

    @property
    def quantidade(self):
        return '{:.2f}'.format(self.__quantidade)

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self.__quantidade = self.valida_quantidade(nova_quantidade)