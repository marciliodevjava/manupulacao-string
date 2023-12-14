import re

class ValidadorUrl():
    def __init__(self):
        self.__url = 'https://bytebank.com.br/cambio'

# https://www.bytebank.com.br/cambio
    def padrao_url(self):

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.__url)
        url = padrao_url.search(self.__url)

        if not match:
            raise ValueError("A url não é válida.")
        else:
            base = url.group()
            print("URL é válida!")
            return base

url = ValidadorUrl()

print(url.padrao_url())
