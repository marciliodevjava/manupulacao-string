url = 'bytebank.com/cambio?moedaOrigem=real'
indice_interrogação = url.find('?')
print(url)

url_divisor = url[indice_interrogação]
print(url_divisor)

url_base = url[0:19]
print(url_base)

url_parametros = url[indice_interrogação + 1:36]
print(url_parametros)
