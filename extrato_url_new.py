import re

class ExtratoUrl:
    def __init__(self, url):
        self.__url = self.sanetiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.__url)

    def __str__(self):
        return str(self.__url)

    def __eq__(self, other):
        return self.__url == other

    def sanetiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.__url:
            raise ValueError('A URL está vazia.')
        else:
            padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
            match = padrao_url.match(self.__url)
            url = padrao_url.search(self.__url)
            print("URL: ", url.group())

    def url_base(self):
        indice_interrogação = self.__url.find('?')
        url_base = self.__url[: indice_interrogação]
        return url_base

    def get_url_parametros(self):
        pass

    def get_url_completa(self):
        return self.__url

    def get_divisor(self):
        indice_interrogação = self.__url.find('?')
        return self.__url[indice_interrogação]

    def get_divisor_url(self):
        divisor = self.__url.find('/')
        return self.__url[divisor]

    def get_divisor_cambio(self):
        divisor = self.__url.find('/') + 1
        cambio = self.__url.find('?')
        return self.__url[divisor:cambio]

    def get_parametro(self):
        divisor = self.__url.find('?') + 1
        return self.__url[divisor:]

    def get_valor(self):
        divisor = self.__url.find('=') + 1
        return self.__url[divisor]


extrator_url = 'bytebank.com/cambio?moedaOrigem=real'
url = ExtratoUrl(extrator_url)
url_dois = ExtratoUrl(extrator_url)

print(f'Tamanho da URL: {len(extrator_url)}')
print(f'URL: {extrator_url}')

print(f'São iguais: {url == url_dois}')

print(f'ID: {id(url)}')
print(f'ID: {id(url_dois)}')

# print(f'URL Completa: {url.get_url_completa()}')
# print('URL Base: {}'.format(url.url_base()))
# print("Divisor ?: {}".format(url.get_divisor()))
# print('Divisor /: {}'.format(url.get_divisor_url()))
# print(f'Cambio: {url.get_divisor_cambio()}')
# print(f'Parametros: {url.get_parametro()}')
# print(f'Valor Cambio: {url.get_valor()}')
