class ExtratoUrl:
    def __init__(self, url):
        self.__url = self.sanetiza_url(url)
        self.valida_url()

    def sanetiza_url(self, url):
        return url.strip()

    def valida_url(self):
        if self.__url == '':
            raise ValueError('A URL está vazia.')

    def url_base(self):
        indice_interrogação = self.__url.find('?')
        url_base = self.__url[: indice_interrogação]
        return url_base

    def get_url_parametros(self):
        pass

    def get_url_completa(self):
        return self.__url

extrator_url = 'bytebank.com/cambio?moedaOrigem=real'

url = ExtratoUrl(extrator_url)

print(f'URL Completa: {url.get_url_completa()}')
print('URL Base: {}'.format(url.url_base()))
