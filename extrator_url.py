url = 'bytebank.com/cambio?moedaOrigem=real'
url = url.strip()
url = "     "

# Validação da url
# Sanitização da url
url = url.replace(" ", "")

if url == "":
    raise ValueError('Valor da URL está vazia')
else:
    indice_interrogação = url.find('?')
    parametros = indice_interrogação + 1
    tamanho = len(url)
    print('URL Completa: {}'.format(url))

    url_divisor = url[indice_interrogação]
    print(f"Divisor de URL: {url_divisor}")

    url_base = url[0:indice_interrogação]
    print(f'URL Base: {url_base}')

    cambio = url_base.find('/') + 1
    barra = url_base.find("/")
    print(f'/: {url_base[barra]}')
    url_cambio = url_base[cambio:]
    print(f'Cambio: {url_cambio}')

    url_parametros = url[parametros:tamanho]
    print(f'URL Parametros: {url_parametros}')

    real = url_parametros.find('=') + 1
    url_real = url_parametros[real:]
    print(f'Valor Real: {url_real}')
