url = 'bytebank.com/cambio?moedaOrigem=real'
indice_interrogação = url.find('?')
parametros = indice_interrogação + 1
tamanho = len(url)
print(url)

url_divisor = url[indice_interrogação]
print(url_divisor)

url_base = url[0:indice_interrogação]
print(url_base)

url_parametros = url[parametros:tamanho]
print(url_parametros)
