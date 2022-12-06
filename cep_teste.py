
from pycep_correios import get_address_from_cep, WebService

cep = input('CEP: ')
address = get_address_from_cep(cep, webservice=WebService.CORREIOS)
print(address)
