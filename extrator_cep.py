import re

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Tio de janeiro, RJ, 23440120"

# 5 digitos +- hifen(opcional)

padrao_cep = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

buscar = padrao_cep.search(endereco)

if buscar:
    cep = buscar.group()
    print("CEP: ", cep)
else:
    print("CEP não encontrado")
