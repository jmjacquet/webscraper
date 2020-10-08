lista = [(1,2),(11,2),(4,55),(5,6),{'hola':"chau"}]


add10 = lambda x,y,z: x*y+10-z

import logging

log = logging.getLogger(__name__)



# try:
#     l=lista[9]
# except Exception as e:
#     log.error(e,exc_info=True)


import json
d = dict(nombre="juanma",apellido="jacquet",edad=38)
d2 = {v:(x.capitalize() if isinstance(x,str) else x) for (v,x) in d.items()}
lista_json = json.dumps(d2,indent=4,sort_keys=True)
print(lista_json)