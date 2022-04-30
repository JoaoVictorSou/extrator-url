class ConversorMoeda:
    @staticmethod
    def valida_quantidade(quantidade):
        tipo_quantidade = type(quantidade)
        if (tipo_quantidade is float) or (tipo_quantidade is int):
            if quantidade >= 0:
                return quantidade

        raise ValueError(
            'erro: quantidade da moeda deve ser um valor numérico maior que zero residente do conjutos dos reais.')

    def __init__(self, moeda_origem, moeda_destino, quantidade=0):
        self.__moeda_origem = moeda_origem
        self.__moeda_destino = moeda_destino
        self.__quantidade = self.valida_quantidade(quantidade)

converte_real_dolar = ConversorMoeda('real', 'dolar', 1)