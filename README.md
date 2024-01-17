# Extrator de URL

Um módulo simples em Python para extrair informações de uma URL específica relacionada a câmbio.

## Uso da Aplicação

### Instalação

Não é necessário instalar nada, basta incluir o código do arquivo `extrator_url.py` no seu projeto.

## Funcionalidades

- **Validação de URL:** Verifica se a URL fornecida é válida para operações de câmbio.
- **Extração de Parâmetros:** Extrai parâmetros específicos da URL, como moeda de origem, moeda de destino e quantidade.
- **Conversão de Câmbio:** Realiza a conversão de câmbio com base nos parâmetros fornecidos.

### Exemplo de Uso

```python
from extrator_url import ExtratorURL

# Crie uma instância do ExtratorURL com uma URL válida
url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
extrator_url = ExtratorURL(url)

# Defina o valor do câmbio
VALOR_DOLAR = 5.50

# Obtenha os parâmetros da URL
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

# Realize a conversão de câmbio
if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_de_conversao = int(quantidade) / VALOR_DOLAR
    print(f'O valor de R${quantidade} reais é igual a ${round(valor_de_conversao, 2)} dólares.')
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_de_conversao = int(quantidade) * VALOR_DOLAR
    print(f'O valor de ${quantidade} dólares é igual a R${round(valor_de_conversao, 2)} reais.')
else:
    print(f'Câmbio de {moeda_origem} para {moeda_destino} está indisponível.')

