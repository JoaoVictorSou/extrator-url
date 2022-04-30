import re # Regular Expression -- RegEx

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# a partir de uma expressão regular (ou a padronização de uma expressão) será retornado o padrão em um objeto para a consulta
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
# as {} com um valor é um quantificador e indica a quantidade de vezes que o caracter do grupo aparece
# o - dentro do padrão sinaliza em qual intervalo pode aparecer
# a ? deve ser adicionada após o caracter informando que ele pode não aparece, ou entao utilizar o quantificador {0, 1}

busca = padrao.search(endereco) # Match ou None

if busca:
    cep = busca.group()

print(cep)