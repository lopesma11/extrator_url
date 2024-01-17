import re

class ExtratorURL:
    def __init__(self, url):
        '''Salva a URL em um atributo do objeto (self.url = url) e verifica se a url é válida'''
        self.url = self.sanitiza_url(url)
        self.valida_url()
    def sanitiza_url(self, url):
        '''Retorna a URl removendo espaços em branco'''
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        '''Valida se a URL está vazia'''
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError('A URl não é válida.')

    def get_url_base(self):
        '''Retorna a base da URL'''
        #if self.url.startswith('https') or self.url.endswith('/cambio'):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        '''Retorna os parâmetros da URL'''
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        '''Retorna o valor do parâmetro 'parametro_busca'. '''
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'Parâmetros: ' + self.get_url_parametros() + '\n' + 'URL Base: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50
print(type(VALOR_DOLAR))
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_de_conversao = int(quantidade) / VALOR_DOLAR
    print('O valor de R$' + quantidade + ' reais é igual a $' + str(round(valor_de_conversao, 2)) + ' dólares.')
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_de_conversao = int(quantidade) * VALOR_DOLAR
    print('O valor de $' + quantidade + ' dólares é igual a R$' + str(round(valor_de_conversao, 2)) + ' reais.')
else:
    print('Câmbio de {} para {} está indisponível.'.format(moeda_origem, moeda_destino))

